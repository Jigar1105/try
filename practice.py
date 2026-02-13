# text=input("Enter input: ")
# text=text.lower()
# if text==text[::-1]:
#     print("Text is a paindrome")
# else:
#     print("Text is not a paindrome")



# l=[10,20,30,40,50]
# total=0
# for num in l:
#     total+=num
# avg=total / len(l)
# print(avg)


# l=[1,2,3,4,5]
# l1=[2,3,6,8,9,10]

# l2=l+l1
# l2.sort()
# print(l2)


tuple=(1,2,3,4,5,6,7,8)
even=()
odd=()
for num in tuple:
    if num%2==0:
        even +=(num,)
    else:
        odd +=(num,)

print("Even:",even)
print("Odd:",odd)