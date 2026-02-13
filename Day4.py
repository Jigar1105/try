# student = input("Enter Student Name: ")
# studentid = int(input("Enter Enrollment: "))

# # Maths
# sub1 = input("Enter Maths Mark: ")
# while not sub1.isdigit() or not (0 <= int(sub1) <= 100):
#     print("Enter Valid Number (0-100)")
#     sub1 = input("Enter Maths Mark: ")

# # Science
# sub2 = input("Enter Science Mark: ")
# while not sub2.isdigit() or not (0 <= int(sub2) <= 100):
#     print("Enter Valid Number (0-100)")
#     sub2 = input("Enter Science Mark: ")

# # English
# sub3 = input("Enter English Mark: ")
# while not sub3.isdigit() or not (0 <= int(sub3) <= 100):
#     print("Enter Valid Number (0-100)")
#     sub3 = input("Enter English Mark: ")

# # Gujarati
# sub4 = input("Enter Gujarati Mark: ")
# while not sub4.isdigit() or not (0 <= int(sub4) <= 100):
#     print("Enter Valid Number (0-100)")
#     sub4 = input("Enter Gujarati Mark: ")

# totalmarks = int(sub1) + int(sub2) + int(sub3) + int(sub4)
# percentage = totalmarks * 100 / 400

# if percentage>=90:
#     Grade="A"
# elif percentage>=80:
#     Grade="B"
# elif percentage>=70:
#     Grade="C"
# elif percentage>=60:
#     Grade="D"  
# else:
#     Grade="Ghare aaram karo ave"


# print("\nStudent Name:", student)
# print("Student ID:", studentid)
# print("Total Marks:", totalmarks)
# print(f"Percentage:{percentage:.2f}")
# print("Grade:",Grade)


# def get_valid_mark(subject):
#     mark = input(f"Enter {subject} Mark: ")
#     while not mark.isdigit() or not (0 <= int(mark) <= 100):
#         print("Enter Valid Number (0-100)")
#         mark = input(f"Enter {subject} Mark: ")
#     return int(mark)


# def student_result():
#     student = input("Enter Student Name: ")
#     studentid = int(input("Enter Enrollment: "))

#     subjects = ["Maths", "Science", "English", "Gujarati"]
#     totalmarks = 0

#     for subject in subjects:
#         totalmarks += get_valid_mark(subject)

#     percentage = totalmarks * 100 / 400

#     print("\nStudent Name:", student)
#     print("Student ID:", studentid)
#     print("Total Marks:", totalmarks)
#     print("Percentage:", percentage.2f)

# student_result()


import random
num=random.randint(0,9999)
name=input("Enter Your Name:")
Mobilenumber = input("Enter Number: ")
while not str(Mobilenumber).isdigit() or len(str((Mobilenumber))) != 10 or str(Mobilenumber)[0] not in ['7','8','9']:
    print("Enter a valid 10-digit mobile number")
    Mobilenumber = input("Enter Number: ")
productname=input("Enter Product Name:")
productprice=input("Enter Product Price:")
while not productprice.isdigit():
    print("Enter a valid number")
    productprice=input("Enter Product Price:")
productquantiti=input("Enter Product Quantiti:")
while not productquantiti.isdigit():
    print("Enter a valid number")
    productquantiti=input("Enter Product Quantity:")
totalprice=int(productprice)*int(productquantiti)

print("----Invoice Details-----")
print("Invoice Number:",num)
print("Customer Name:",name)
print("Phone Number:",Mobilenumber)
print("Product Name:",productname)
print("Product Price:",productprice)
print("Product Quantiti:",productquantiti)
print("Total Price:",totalprice)

while True:
    print("1.Add itme")
    print("2.Exit")

    choice=int(input("Enter Your choice: "))

    if choice==1:
        productname=input("Enter Product Name:")
        productprice=input("Enter Product Price:")
        while not productprice.isdigit():
            print("Enter a valid number")
            productprice=input("Enter Product Price:")
        productquantiti=input("Enter Product Quantiti:")
        while not productquantiti.isdigit():
            print("Enter a valid number")
            productquantiti=input("Enter Product Quantity:")
        totalprice=int(productprice)*int(productquantiti)

    elif choice==2:
        break

    else:
        print("Invalid Choice")


    items={
        "product name:",productname,
        "Product price:",productprice,
        "total price:",totalprice
    }

    print("Product Name:",productname)
    print("Product Price:",productprice)
    print("Product Quantiti:",productquantiti)
    print("Total Price:",totalprice)
    print(items)


