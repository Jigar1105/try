import random
import pymysql

# -------- DATABASE CONNECTION --------
def get_connection():
    return pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database='invoice_db',
        port=3306,
        cursorclass=pymysql.cursors.DictCursor
    )

# -------- DISPLAY SINGLE INVOICE --------
def display_invoice(customer_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customers WHERE id=%s", (customer_id,))
    customer = cursor.fetchone()
    if not customer:
        print("Invoice not found!")
        conn.close()
        return

    print("\n======= INVOICE =======")
    print("Invoice Number:", customer["invoice_number"])
    print("Customer Name:", customer["customer_name"])
    print("Mobile:", customer["mobile"])
    print("Grand Total:", customer["grand_total"])
    print("-----------------------")
    print("Items:")
    cursor.execute("SELECT * FROM invoice_items WHERE customer_id=%s", (customer_id,))
    items = cursor.fetchall()
    for item in items:
        print(f"{item['product_name']} | {item['product_price']} | {item['product_quantity']} | {item['item_total']}")
    print("========================\n")
    conn.close()

# -------- RECALCULATE GRAND TOTAL --------
def recalculate_total(customer_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(item_total) as total FROM invoice_items WHERE customer_id=%s", (customer_id,))
    total = cursor.fetchone()["total"] or 0
    cursor.execute("UPDATE customers SET grand_total=%s WHERE id=%s", (total, customer_id))
    conn.commit()
    conn.close()

# -------- CREATE INVOICE (DB ONLY) --------
def create_invoice():
    invoice_number = random.randint(1000, 9999)
    name = input("Enter Customer Name: ")
    mobile = input("Enter Mobile Number: ")
    while not mobile.isdigit() or len(mobile) != 10:
        print("Enter a valid 10-digit mobile number")
        mobile = input("Enter Mobile Number: ")

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO customers (invoice_number, customer_name, mobile, grand_total) VALUES (%s,%s,%s,%s)",
        (invoice_number, name, mobile, 0)
    )
    customer_id = cursor.lastrowid
    conn.commit()

    while True:
        product_name = input("Enter Product Name: ")
        price = float(input("Enter Product Price: "))
        quantity = int(input("Enter Product Quantity: "))
        total = price * quantity

        cursor.execute(
            "INSERT INTO invoice_items (customer_id, product_name, product_price, product_quantity, item_total) VALUES (%s,%s,%s,%s,%s)",
            (customer_id, product_name, price, quantity, total)
        )
        conn.commit()
        recalculate_total(customer_id)

        print("\n1. Add another item")
        print("2. Finish Invoice")
        choice = input("Enter choice: ")
        if choice == '2':
            break

    conn.close()
    display_invoice(customer_id)
    print("Invoice created successfully!")

# -------- SEARCH INVOICE --------
def search_invoice():
    invoice_no = input("Enter Invoice Number: ")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM customers WHERE invoice_number=%s", (invoice_no,))
    customer = cursor.fetchone()
    conn.close()
    if customer:
        display_invoice(customer["id"])
    else:
        print("Invoice not found!")

# -------- DELETE INVOICE --------
def delete_invoice():
    invoice_no = input("Enter Invoice Number to Delete: ")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM customers WHERE invoice_number=%s", (invoice_no,))
    customer = cursor.fetchone()
    if not customer:
        print("Invoice not found!")
        conn.close()
        return
    confirm = input("Are you sure? (yes/no): ")
    if confirm.lower() == "yes":
        cursor.execute("DELETE FROM customers WHERE invoice_number=%s", (invoice_no,))
        conn.commit()
        print("Invoice deleted.")
    else:
        print("Cancelled.")
    conn.close()


def update_invoice_items():
    invoice_no = input("Enter Invoice Number to Update Items: ")
    conn = get_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    cursor.execute("SELECT * FROM customers WHERE invoice_number=%s", (invoice_no,))
    customer = cursor.fetchone()

    if not customer:
        print("Invoice not found!")
        conn.close()
        return

    customer_id = customer["id"]

    while True:
        pname = input("Enter product name to update: ")

        # 🔹 Pehle check karo item exist karta hai ya nahi
        cursor.execute(
            "SELECT * FROM invoice_items WHERE customer_id=%s AND product_name=%s",
            (customer_id, pname)
        )
        item = cursor.fetchone()

        if item:
            break   # Agar item mil gaya to loop se bahar
        else:
            print("Invalid item name! Please enter correct product name.")

    # 🔹 Update values lo
    new_price = float(input("New price: "))
    new_qty = int(input("New quantity: "))
    new_total = new_price * new_qty

    # 🔹 Update query
    cursor.execute(
        """UPDATE invoice_items 
           SET product_price=%s, product_quantity=%s, item_total=%s 
           WHERE customer_id=%s AND product_name=%s""",
        (new_price, new_qty, new_total, customer_id, pname)
    )

    conn.commit()

    recalculate_total(customer_id)

    print("Item updated successfully.")
    conn.close()

# -------- MAIN MENU --------
while True:
    print("\n====== INVOICE SYSTEM ======")
    print("1. Create Invoice")
    print("2. Search Invoice by Number")
    print("3. Update Invoice Items")
    print("4. Delete Invoice")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        create_invoice()
    elif choice == '2':
        search_invoice()
    elif choice == '3':
        update_invoice_items()
    elif choice == '4':
        delete_invoice()
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice!")
