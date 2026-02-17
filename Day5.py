import random
def display_invoice(products, grand_total, name, num, Mobilenumber):
    print("\n----------------Invoice Items----------------")
    print("Customer Name:", name)
    print("Invoice Number:", num)
    print("Phone Number:", Mobilenumber)
    print("\nProduct Name\tProduct Price\tProduct Quantity\tItem Total")
    
    for item in products:
        print(f"{item['Product Name']}\t\t{item['Product Price']}\t\t{item['Product Quantity']}\t\t\t{item['Item Total']}")
    
    print("\n--------------------------------------")
    print("Grand Total:", grand_total)
    print("-----------------------------------------")

num = random.randint(1000, 9999)
name = input("Enter Your Name: ")

Mobilenumber = input("Enter Number: ")
while not Mobilenumber.isdigit() or len(Mobilenumber) != 10 or Mobilenumber[0] not in ['7','8','9']:
    print("Enter a valid 10-digit mobile number")
    Mobilenumber = input("Enter Number: ")

products = []
grand_total = 0

while True:
    productname = input("Enter Product Name: ")

    productprice = input("Enter Product Price: ")
    while not productprice.isdigit():
        print("Enter a valid number")
        productprice = input("Enter Product Price: ")

    productquantiti = input("Enter Product Quantity: ")
    while not productquantiti.isdigit():
        print("Enter a valid number")
        productquantiti = input("Enter Product Quantity: ")

    item_total = int(productprice) * int(productquantiti)
    grand_total += item_total

    products.append({
        "Product Name": productname,
        "Product Price": int(productprice),
        "Product Quantity": int(productquantiti),
        "Item Total": item_total
    })

    while True:
        print("\n1. Add another item")
        print("2. Any item remove")
        print("3. Update item")
        print("4. Display Invoice")
        print("5. Exit")
        choice = input("Enter Your choice: ")

        if choice == '1':
            break  

        elif choice == '2':
            remove_item = input("Enter the name of the item to remove: ")
            for item in products:
                if item["Product Name"].lower() == remove_item.lower():
                    grand_total -= item["Item Total"]
                    products.remove(item)
                    print(f"{remove_item} has been removed.")
                    break
            else:
                print(f"{remove_item} not found in the invoice.")

        elif choice == '3':
            update_item = input("Enter the name of the item to update: ")
            for item in products:
                if item["Product Name"].lower() == update_item.lower():
                    new_price = input("Enter new price: ")
                    while not new_price.isdigit():
                        print("Enter a valid number")
                        new_price = input("Enter new price: ")

                    new_quantity = input("Enter new quantity: ")
                    while not new_quantity.isdigit():
                        print("Enter a valid number")
                        new_quantity = input("Enter new quantity: ")

                    old_total = item["Item Total"]

                    item["Product Price"] = int(new_price)
                    item["Product Quantity"] = int(new_quantity)
                    item["Item Total"] = int(new_price) * int(new_quantity)

                    grand_total += (item["Item Total"] - old_total)

                    print(f"{update_item} has been updated.")
                    break
            else:
                print(f"{update_item} not found in the invoice.")

        elif choice == '4':
            display_invoice(products, grand_total, name, num, Mobilenumber)

        elif choice == '5':
            break

        else:
            print("Invalid choice. Please enter 1,2,3,4 or 5")

    if choice == '5':
        break  

display_invoice(products, grand_total, name, num, Mobilenumber)
