# a=input("Enter first number: ")
# while not a.isdigit():
#     print("Enter a valid number")
#     a=input("Enter first number: ")
# b=input("Enter second number: ")
# while not b.isdigit():
#     print("Enter a valid number")
#     b=input("Enter second number: ")
# c=input("Enter third number:")
# while not c.isdigit():
#     print("Enter a valid number")
#     c=input("Enter third number: ")

# # if a.isdigit() and b.isdigit() and c.isdigit():
# a=int(a)
# b=int(b)
# c=int(c)

# if a>b and a>c:
#     print("largest number:",a)
        
# elif b>a and b>c:
#     print("largest Number:",b)
# else:
#     print("LArgest Number:",c)


# a = input("Enter first number: ")
# b = input("Enter second number: ")
# c = input("Enter third number: ")

# if a.isdigit() and b.isdigit() and c.isdigit():

#     if len(a) > len(b) and len(a) > len(c):
#         print("Largest number:", a)
#     elif len(b) > len(a) and len(b) > len(c):
#         print("Largest number:", b)
#     elif len(c) > len(a) and len(c) > len(b):
#         print("Largest number:", c)
#     else:
#         if a > b and a > c:
#             print("Largest number:", a)
#         elif b > a and b > c:
#             print("Largest number:", b)
#         else:
#             print("Largest number:", c)

# else:
#     print("Invalid input")


user = input("Enter Name: ")
Mobilenumber = input("Enter Number: ")
while not Mobilenumber.isdigit() or len(Mobilenumber) != 10:
    print("Enter a valid 10-digit mobile number")
    Mobilenumber = input("Enter Number: ")

product = input("Product Name: ")
product_price=input("Enter Price:")
while not product_price.isdigit():
    print("Enter Valid Price")
    product_price=input("Enter Price:")
Quantity=input("Enter Quantity:")
while not Quantity.isdigit():
    print("Enter Valid Quantity")
    Quantity=input("Enter Quantity:")
    
Total_price =int(product_price) *int(Quantity)

print("\n--- User Details ---")
print("User Name:", user)
print("Mobile Number:", Mobilenumber)
print("Product Name:", product)
print("Quantity:",Quantity)
print("Price:", product_price)
print("Total price:",Total_price)




