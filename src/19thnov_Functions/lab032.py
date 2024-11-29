# write a program to print the sum of three number from the user input
#if user does not enter any value use default as 100,200,300

num1=int(input("Enter a number:"))
num2=int(input("Enter a number:"))
num3=int(input("Enter a number:"))

def sum_of_three_numbers(n1=100,n2=700,n3=800):
    return n1+n2+n3

result=sum_of_three_numbers(num1,num2,num3)
print(result)
result2=sum_of_three_numbers()
print(result2)
