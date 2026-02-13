# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist.insert(2,"chikoo")

# # thislist[1:3] = ["blackcurrant", "watermelon"]

# print(thislist)

# def sum1(a,b):
#     c=a+b
#     return c

# result=sum1(10,10)
# print(result)

# def square(a):
#     b=a*a
#     return b
# result=square(10)
# print(result)

# tuple=(1,2,3,4,5,6,7)
# y=(55,6,7)
# tuple += y
# print(tuple)

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


buyerstate=input("Buyer State: ")
sellerstate=input("Seller State: ")
if sellerstate == buyerstate :
    cgst=0.09*Total_price
    sgst=0.09*Total_price
    print("cGST:",cgst)
    print("sGST:",sgst)
    Total_price=Total_price+cgst+sgst
    print(Total_price)

else:
    igst=0.18*Total_price
    print("IGST:",igst)
    Total_price=Total_price+igst
    print(Total_price)

order_data = [
    user,
    Mobilenumber,
    product,
    int(product_price),
    int(Quantity),
    buyerstate,
    sellerstate,
    Total_price
]


print("\n--- User Details ---")
print("User Name:", user)
print("Mobile Number:", Mobilenumber)
print("Product Name:", product)
print("Quantity:",Quantity)
print("Price:", product_price)
print("Total price:",Total_price)
print(order_data)


