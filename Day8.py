import random
import pymysql


# ============ DATABASE CONNECTION FUNCTION ============
def get_connection():
    return pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database='invoice_db',
        port=3306
    )


# ============ DISPLAY SINGLE INVOICE ============
def display_invoice(products, grand_total, name, num, Mobilenumber):
    print("\n----------------Invoice----------------")
    print("Customer Name:", name)
    print("Invoice Number:", num)
    print("Phone Number:", Mobilenumber)
    print("\nProduct Name | Price | Qty | Total")

    for item in products:
        print(f"{item['Product Name']} | "
              f"{item['Product Price']} | "
              f"{item['Product Quantity']} | "
              f"{item['Item Total']}")

    print("--------------------------------------")
    print("Grand Total:", grand_total)
    print("--------------------------------------")


# ============ SAVE TO DATABASE ============
def save_to_database(products, grand_total, name, num, Mobilenumber):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO customers (invoice_number, customer_name, mobile, grand_total) VALUES (%s, %s, %s, %s)",
            (num, name, Mobilenumber, grand_total)
        )

        customer_id = cursor.lastrowid

        for item in products:
            cursor.execute(
                """INSERT INTO invoice_items 
                (customer_id, product_name, product_price, product_quantity, item_total)
                VALUES (%s, %s, %s, %s, %s)""",
                (
                    customer_id,
                    item["Product Name"],
                    item["Product Price"],
                    item["Product Quantity"],
                    item["Item Total"]
                )
            )

        conn.commit()
        conn.close()
        print("Data saved to MySQL successfully!")

    except Exception as e:
        print("Database Error:", e)


# ============ VIEW ALL RECORDS ============
def display_all_customers():
    try:
        conn = get_connection()
        cursor = conn.cursor(pymysql.cursors.DictCursor)

        cursor.execute("SELECT * FROM customers")
        customers = cursor.fetchall()

        if not customers:
            print("No records found.")
            return

        for customer in customers:
            print("\n======================================")
            print("Invoice Number:", customer["invoice_number"])
            print("Customer Name:", customer["customer_name"])
            print("Mobile:", customer["mobile"])
            print("Grand Total:", customer["grand_total"])
            print("--------------------------------------")
            print("Items:")

            cursor.execute(
                "SELECT * FROM invoice_items WHERE customer_id=%s",
                (customer["id"],)
            )

            items = cursor.fetchall()

            for item in items:
                print(f"{item['product_name']} | "
                      f"{item['product_price']} | "
                      f"{item['product_quantity']} | "
                      f"{item['item_total']}")

        conn.close()

    except Exception as e:
        print("Database Error:", e)


# ============ SEARCH BY INVOICE NUMBER ============
def search_invoice():
    try:
        invoice_no = input("Enter Invoice Number: ")

        conn = get_connection()
        cursor = conn.cursor(pymysql.cursors.DictCursor)

        cursor.execute("SELECT * FROM customers WHERE invoice_number=%s", (invoice_no,))
        customer = cursor.fetchone()

        if not customer:
            print("Invoice not found!")
            return

        print("\n========== INVOICE DETAILS ==========")
        print("Invoice Number:", customer["invoice_number"])
        print("Customer Name:", customer["customer_name"])
        print("Mobile:", customer["mobile"])
        print("Grand Total:", customer["grand_total"])
        print("-------------------------------------")
        print("Items:")

        cursor.execute("SELECT * FROM invoice_items WHERE customer_id=%s", (customer["id"],))
        items = cursor.fetchall()

        for item in items:
            print(f"{item['product_name']} | "
                  f"{item['product_price']} | "
                  f"{item['product_quantity']} | "
                  f"{item['item_total']}")

        conn.close()

    except Exception as e:
        print("Database Error:", e)


# ============ UPDATE INVOICE ============
def update_invoice():
    try:
        invoice_no = input("Enter Invoice Number to Update: ")
        while not invoice_no.isdigit():
            print("Enter valid invoice number")
            invoice_no = input("Enter Invoice Number to Update: ")

        conn = get_connection()
        cursor = conn.cursor(pymysql.cursors.DictCursor)

        cursor.execute("SELECT * FROM customers WHERE invoice_number=%s", (invoice_no,))
        customer = cursor.fetchone()

        if not customer:
            print("Invoice not found!")
            conn.close()
            return

        print("\n1. Update Customer Details")
        print("2. Update Invoice Items")
        choice = input("Enter your choice: ")

        # ================= UPDATE CUSTOMER DETAILS =================
        if choice == '1':
            new_name = input("Enter New Customer Name: ")
            new_mobile = input("Enter New Mobile: ")

            cursor.execute(
                "UPDATE customers SET customer_name=%s, mobile=%s WHERE invoice_number=%s",
                (new_name, new_mobile, invoice_no)
            )

            conn.commit()
            print("Customer details updated successfully!")

        # ================= UPDATE INVOICE ITEMS =================
        elif choice == '2':

            cursor.execute(
                "SELECT * FROM invoice_items WHERE customer_id=%s",
                (customer["id"],)
            )
            items = cursor.fetchall()

            if not items:
                print("No items found!")
                conn.close()
                return

            print("\nExisting Items:")
            for item in items:
                print(f"{item['product_name']} | "
                      f"{item['product_price']} | "
                      f"{item['product_quantity']} | "
                      f"{item['item_total']}")

            product_name = input("Enter Product Name to Update: ")

            cursor.execute(
                """SELECT * FROM invoice_items 
                   WHERE customer_id=%s AND product_name=%s""",
                (customer["id"], product_name)
            )

            item = cursor.fetchone()

            if not item:
                print("Product not found!")
                conn.close()
                return

            new_price = float(input("Enter New Price: "))
            new_quantity = int(input("Enter New Quantity: "))
            new_total = new_price * new_quantity

            cursor.execute(
                """UPDATE invoice_items 
                   SET product_price=%s, product_quantity=%s, item_total=%s 
                   WHERE id=%s""",
                (new_price, new_quantity, new_total, item["id"])
            )

            # ===== Recalculate Grand Total =====
            cursor.execute(
                "SELECT SUM(item_total) as total FROM invoice_items WHERE customer_id=%s",
                (customer["id"],)
            )

            total = cursor.fetchone()["total"]

            cursor.execute(
                "UPDATE customers SET grand_total=%s WHERE id=%s",
                (total, customer["id"])
            )

            conn.commit()
            print("Invoice item updated and grand total recalculated!")

        else:
            print("Invalid choice!")

        conn.close()

    except Exception as e:
        print("Database Error:", e)



# ============ DELETE INVOICE ============
def delete_invoice():
    try:
        invoice_no = input("Enter Invoice Number to Delete: ")

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM customers WHERE invoice_number=%s", (invoice_no,))
        conn.commit()

        if cursor.rowcount > 0:
            print("Invoice deleted successfully!")
        else:
            print("Invoice not found!")

        conn.close()

    except Exception as e:
        print("Database Error:", e)


# ================= MAIN MENU =================

while True:
    print("\n========= INVOICE SYSTEM =========")
    print("1. Create Invoice")
    print("2. View All Records")
    print("3. Search Invoice")
    print("4. Update Invoice")
    print("5. Delete Invoice")
    print("6. Exit")

    main_choice = input("Enter choice: ")

    # -------- CREATE INVOICE --------
    if main_choice == '1':

        num = random.randint(1000, 9999)
        name = input("Enter Your Name: ")

        Mobilenumber = input("Enter Number: ")
        while not Mobilenumber.isdigit() or len(Mobilenumber) != 10:
            print("Enter valid 10-digit number")
            Mobilenumber = input("Enter Number: ")

        products = []
        grand_total = 0

        while True:
            productname = input("Enter Product Name: ")

            productprice = input("Enter Product Price: ")
            while not productprice.isdigit():
                productprice = input("Enter valid price: ")

            productquantity = input("Enter Product Quantity: ")
            while not productquantity.isdigit():
                productquantity = input("Enter valid quantity: ")

            item_total = int(productprice) * int(productquantity)
            grand_total += item_total

            products.append({
                "Product Name": productname,
                "Product Price": int(productprice),
                "Product Quantity": int(productquantity),
                "Item Total": item_total
            })

            while True:
                print("\n1. Add another item")
                print("2. Remove an item")
                print("3. Update item")
                print("4. Display Invoice")
                print("5. Save & Exit")
                choice = input("Enter Your choice: ")

                if choice == '1':
                    break

                elif choice == '2':
                    remove_item = input("Enter product name to remove: ")
                    for item in products:
                        if item["Product Name"].lower() == remove_item.lower():
                            grand_total -= item["Item Total"]
                            products.remove(item)
                            print("Item removed.")
                            break

                elif choice == '3':
                    update_item = input("Enter product name to update: ")
                    for item in products:
                        if item["Product Name"].lower() == update_item.lower():
                            new_price = int(input("Enter new price: "))
                            new_quantity = int(input("Enter new quantity: "))
                            old_total = item["Item Total"]
                            item["Product Price"] = new_price
                            item["Product Quantity"] = new_quantity
                            item["Item Total"] = new_price * new_quantity
                            grand_total += item["Item Total"] - old_total
                            print("Item updated.")
                            break

                elif choice == '4':
                    display_invoice(products, grand_total, name, num, Mobilenumber)

                elif choice == '5':
                    save_to_database(products, grand_total, name, num, Mobilenumber)
                    break

            if choice == '5':
                break

        display_invoice(products, grand_total, name, num, Mobilenumber)

    elif main_choice == '2':
        display_all_customers()

    elif main_choice == '3':
        search_invoice()

    elif main_choice == '4':
        update_invoice()

    elif main_choice == '5':
        delete_invoice()

    elif main_choice == '6':
        print("Exiting...")
        break

    else:
        print("Invalid choice!")
