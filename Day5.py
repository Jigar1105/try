import random
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
        "Product Price": productprice,
        "Product Quantity": productquantiti,
        "Item Total": item_total
    })

    while True:
        print("1. Add another item")
        print("2. Exit")
        choice = input("Enter Your choice: ")

        if choice == '1':
            break  
        elif choice == '2':
            break  
        else:
            print("Invalid choice. Please enter 1 or 2.")

    if choice == '2':
        break  

print("\n---- Invoice Details -----")
print("Invoice Number:", num)
print("Customer Name:", name)
print("Phone Number:", Mobilenumber)
print("\nProducts:")
for item in products:
    print(item)
print("Grand Total:", grand_total)
