# Find the max between 3 numbers

# user input --num1,num2,num3-->int
# o/p->int or string with max number

num1 = int(input("Enter a number:"))
num2 = int(input("Enter a number:"))
num3 = int(input("Enter a number:"))

# Logic
# if condition 1
# print(do 1)
#
if num1 > num2 and num1 > num3:
    print("Max is", num1)
elif num2>num1 and num2>num3:
    print("max is", num2)
else:
    print("max is",num3)
