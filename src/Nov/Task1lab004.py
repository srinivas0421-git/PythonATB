# num1=float(input("Enter a number1:"))
# num2=float(input("Enter a number2:"))
# num3=float(input("Enter a number3:"))
# num4=float(input("Enter a number4:"))
#
# sub_result=num1-num2-num3
# sum_result=num1+num2+num3
# mul_result=num1*num2
# div_result=num1/num2
# print(sum_result)
# print(sub_result)
# print(mul_result)
# print(div_result)
from math import remainder

num1=int(input("Enter the first number (dividend): "))
num2=int(input("Enter the second number(division): "))

quotient=num1//num2
remaind=num1 % num2
print(quotient)
print(remaind)