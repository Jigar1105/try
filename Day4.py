# # student = input("Enter Student Name: ")
# # studentid = int(input("Enter Enrollment: "))

# # # Maths
# # sub1 = input("Enter Maths Mark: ")
# # while not sub1.isdigit() or not (0 <= int(sub1) <= 100):
# #     print("Enter Valid Number (0-100)")
# #     sub1 = input("Enter Maths Mark: ")

# # # Science
# # sub2 = input("Enter Science Mark: ")
# # while not sub2.isdigit() or not (0 <= int(sub2) <= 100):
# #     print("Enter Valid Number (0-100)")
# #     sub2 = input("Enter Science Mark: ")

# # # English
# # sub3 = input("Enter English Mark: ")
# # while not sub3.isdigit() or not (0 <= int(sub3) <= 100):
# #     print("Enter Valid Number (0-100)")
# #     sub3 = input("Enter English Mark: ")

# # # Gujarati
# # sub4 = input("Enter Gujarati Mark: ")
# # while not sub4.isdigit() or not (0 <= int(sub4) <= 100):
# #     print("Enter Valid Number (0-100)")
# #     sub4 = input("Enter Gujarati Mark: ")

# # totalmarks = int(sub1) + int(sub2) + int(sub3) + int(sub4)
# # percentage = totalmarks * 100 / 400

# # if percentage>=90:
# #     Grade="A"
# # elif percentage>=80:
# #     Grade="B"
# # elif percentage>=70:
# #     Grade="C"
# # elif percentage>=60:
# #     Grade="D"  
# # else:
# #     Grade="Ghare aaram karo ave"


# # print("\nStudent Name:", student)
# # print("Student ID:", studentid)
# # print("Total Marks:", totalmarks)
# # print(f"Percentage:{percentage:.2f}")
# # print("Grade:",Grade)


# # def get_valid_mark(subject):
# #     mark = input(f"Enter {subject} Mark: ")
# #     while not mark.isdigit() or not (0 <= int(mark) <= 100):
# #         print("Enter Valid Number (0-100)")
# #         mark = input(f"Enter {subject} Mark: ")
# #     return int(mark)


# # def student_result():
# #     student = input("Enter Student Name: ")
# #     studentid = int(input("Enter Enrollment: "))

# #     subjects = ["Maths", "Science", "English", "Gujarati"]
# #     totalmarks = 0

# #     for subject in subjects:
# #         totalmarks += get_valid_mark(subject)

# #     percentage = totalmarks * 100 / 400

# #     print("\nStudent Name:", student)
# #     print("Student ID:", studentid)
# #     print("Total Marks:", totalmarks)
# #     print("Percentage:", percentage.2f)

# # student_result()




import random

def display_invoice(data, totalprice, name, num, Mobilenumber):
    print("\n----------------Invoice Items----------------")
    print("Customer Name:", name)
    print("Invoice Number:", num)
    print("Phone Number:", Mobilenumber)
    print("\nProduct Name\tProduct Price\tProduct Quantity\tItem Total")

    for productname, details in data.items():
        print(f"{productname}\t\t{details['Product Price']}\t\t{details['Product Quantiti']}\t\t\t{details['Total Price']}")

    print("\n--------------------------------------")
    print("Grand Total:", totalprice)
    print("-----------------------------------------")



num = random.randint(0, 9999)
name = input("Enter Your Name: ")

Mobilenumber = input("Enter Number: ")
while not Mobilenumber.isdigit() or len(Mobilenumber) != 10 or Mobilenumber[0] not in ['7','8','9']:
    print("Enter a valid 10-digit mobile number")
    Mobilenumber = input("Enter Number: ")


productname = input("Enter Product Name: ")

productprice = input("Enter Product Price: ")
while not productprice.isdigit():
    print("Enter a valid number")
    productprice = input("Enter Product Price: ")

productquantiti = input("Enter Product Quantity: ")
while not productquantiti.isdigit():
    print("Enter a valid number")
    productquantiti = input("Enter Product Quantity: ")

totalprice = int(productprice) * int(productquantiti)

data = {
    productname: {
        "Product Price": int(productprice),
        "Product Quantiti": int(productquantiti),
        "Total Price": totalprice
    }
}

while True:
    print("\n1.Add item")
    print("2.Remove item")
    print("3.Update item")
    print("4.Display invoice")
    print("5.Exit")

    choice = input("Enter Your choice: ")

    if choice == '1':
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
        totalprice += item_total

        data[productname] = {
            "Product Price": int(productprice),
            "Product Quantiti": int(productquantiti),
            "Total Price": item_total
        }

    elif choice == '2':
        remove_item = input("Enter item name to remove: ")

        if remove_item in data:
            totalprice -= data[remove_item]["Total Price"]
            del data[remove_item]
            print("Item removed successfully")
        else:
            print("Item not found")

    elif choice == '3':
        update_item = input("Enter item name to update: ")

        if update_item in data:
            new_price = input("Enter new price: ")
            while not new_price.isdigit():
                print("Enter valid number")
                new_price = input("Enter new price: ")

            new_quantity = input("Enter new quantity: ")
            while not new_quantity.isdigit():
                print("Enter valid number")
                new_quantity = input("Enter new quantity: ")

            old_total = data[update_item]["Total Price"]
            new_total = int(new_price) * int(new_quantity)

            data[update_item]["Product Price"] = int(new_price)
            data[update_item]["Product Quantiti"] = int(new_quantity)
            data[update_item]["Total Price"] = new_total

            totalprice += (new_total - old_total)

            print("Item updated successfully")
        else:
            print("Item not found")

    elif choice == '4':
        display_invoice(data, totalprice, name, num, Mobilenumber)

    elif choice == '5':
        break

    else:
        print("Invalid Choice")

display_invoice(data, totalprice, name, num, Mobilenumber)


