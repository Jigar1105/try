#Electricity bill
# Customer = input("Enter Name: ")
# count=0
# while count<1:
#     Mobilenumber=input("Enter Number : ")
#     if Mobilenumber.isdigit() and len(Mobilenumber)==10 and Mobilenumber[0] in ['7','8','9']:
#         count+=1
#     else:
#         print("Invalid Number ")
# unit=input("Enter Consumed unit: ")
# while not unit.isdigit():
#     print("Invalid input")
#     unit=input("Enter Consumed unit: ")
     
# if int(unit)<=100:
#     Unitprice=1.5
# elif int(unit)>100 and int(unit)<=200:
#     Unitprice=2.5
# elif int(unit)>200 and int(unit)<=300:
#     Unitprice=4.0
# else:
#     Unitprice=6

# Fixcharge=50
# Totalprice=int(unit)*Unitprice+Fixcharge

# order_data = {
#     "Customer":Customer,
#     "MobileNumber":Mobilenumber,
#     "Unit":unit,
#     "Unitprice":Unitprice,
#     "FixCharge":Fixcharge,
#     "TotalPrice":Totalprice
# }


# print("\n--- User Details ---")
# print("User Name:",Customer)
# print("Mobile Number:", Mobilenumber)
# print("Consumed Unit:", unit)
# print("UnitPrice:",Unitprice)
# print("FixCharge: ", Fixcharge)
# print("Total price:",Totalprice)
# print(order_data)



# def bill(Customer,Mobilenumber,unit):
#     #Customer = input("Enter Name: ")
#     # Mobilenumber = input("Enter Number: ")
  
#     while not str(Mobilenumber).isdigit() or len(str((Mobilenumber))) != 10 or str(Mobilenumber)[0] not in ['7','8','9']:
#         print("Enter a valid 10-digit mobile number")
#         Mobilenumber = input("Enter Number: ")
    
#     # unit=input("Enter Consumed unit: ")
#     while not str(unit).isdigit():
#         print("Invalid input")
#         unit=int(input("Enter Consumed unit: "))
     
#     if int(unit)<=100:
#         Unitprice=1.5 
#     elif int(unit)>100 and int(unit)<=200:
#         Unitprice=2.5
#     elif int(unit)>200 and int(unit)<=300:
#         Unitprice=4.0
#     else:
#         Unitprice=6

#     Fixcharge=50
#     Totalprice=int(unit)*Unitprice+Fixcharge

#     order_data = {
#         "Customer":Customer,
#         "MobileNumber":Mobilenumber,
#         "Unit":unit,
#         "Unitprice":Unitprice,
#         "FixCharge":Fixcharge,
#         "TotalPrice":Totalprice
#         }


#     print("\n--- User Details ---")
#     print("User Name:",Customer)
#     print("Mobile Number:", Mobilenumber)
#     print("Consumed Unit:", unit)
#     print("UnitPrice:",Unitprice)
#     print("FixCharge: ", Fixcharge)
#     print("Total price:",Totalprice)

#     return order_data

# bill1 = bill("Jigar",9999999999,500)
# print(bill1)

def calculator(a,b):
    # a=int(input("Enter Number:"))
    # b=int(input("Enter Number:"))

    while True:
        print("1.Addition")
        print("2.divide")
        print("3.substraction")
        print("4.multiplication")
        print("5.Exit")


        choice=int(input("Enter your choice:"))

        if choice==1:
            print("Addition is : ",a+b)
        
        elif choice==2:
            if b!=0:
                print("Division is : ",a/b)
            else:
                print("not divided by zero")
        
        elif choice==3:
            print("Substraction is :",a-b)

        elif choice==4:
            print("Multiplicaton is ",a*b)

        elif choice==5:
            break 

        else:
            print("invalid")

calculator(20,30)

