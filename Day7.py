import random
# from openpyxl import Workbook  # Excel save temporarily commented
import pymysql


# -------- Display Single Invoice --------
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


# -------- Save to Database --------
def save_to_database(products, grand_total, name, num, Mobilenumber):
    try:
        conn = pymysql.connect(
            host='127.0.0.1',
            user='root',
            password='',
            database='invoice_db',
            port=3306
        )
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
        cursor.close()
        conn.close()

        print("Data saved to MySQL successfully!")

    except Exception as e:
        print("Database Error:", e)


# -------- Display All Database Records --------
def display_all_customers():
    try:
        conn = pymysql.connect(
            host='127.0.0.1',
            user='root',
            password='',
            database='invoice_db',
            port=3306
        )
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

        cursor.close()
        conn.close()

    except Exception as e:
        print("Database Error:", e)


# ================= MAIN MENU =================

while True:
    print("\n========= INVOICE SYSTEM =========")
    print("1. Create Invoice")
    print("2. View All Database Records")
    print("3. Exit")

    main_choice = input("Enter choice: ")

    if main_choice == '1':
        # -------- Create Invoice --------
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
                print("Enter valid number")
                productprice = input("Enter Product Price: ")

            productquantity = input("Enter Product Quantity: ")
            while not productquantity.isdigit():
                print("Enter valid number")
                productquantity = input("Enter Product Quantity: ")

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
                    break  # back to add new product

                elif choice == '2':
                    remove_item = input("Enter product name to remove: ")
                    for item in products:
                        if item["Product Name"].lower() == remove_item.lower():
                            grand_total -= item["Item Total"]
                            products.remove(item)
                            print(f"{remove_item} removed.")
                            break
                    else:
                        print("Item not found.")

                elif choice == '3':
                    update_item = input("Enter product name to update: ")
                    for item in products:
                        if item["Product Name"].lower() == update_item.lower():
                            new_price = input("Enter new price: ")
                            while not new_price.isdigit():
                                new_price = input("Enter valid price: ")

                            new_quantity = input("Enter new quantity: ")
                            while not new_quantity.isdigit():
                                new_quantity = input("Enter valid quantity: ")

                            old_total = item["Item Total"]
                            item["Product Price"] = int(new_price)
                            item["Product Quantity"] = int(new_quantity)
                            item["Item Total"] = int(new_price) * int(new_quantity)
                            grand_total += item["Item Total"] - old_total
                            print(f"{update_item} updated.")
                            break
                    else:
                        print("Item not found.")

                elif choice == '4':
                    display_invoice(products, grand_total, name, num, Mobilenumber)

                elif choice == '5':
                    # save_to_excel(products, grand_total, name, num, Mobilenumber)  # optional
                    save_to_database(products, grand_total, name, num, Mobilenumber)
                    break

                else:
                    print("Invalid choice!")

            if choice == '5':
                break

        display_invoice(products, grand_total, name, num, Mobilenumber)

    elif main_choice == '2':
        display_all_customers()

    elif main_choice == '3':
        print("Exiting...")
        break

    else:
        print("Invalid choice!")
