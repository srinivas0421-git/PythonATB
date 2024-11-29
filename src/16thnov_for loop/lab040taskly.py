# Leap day occurs in each year that is a multiple of 4, except for years
#     evenly divisible by 100 but not by 400.


# if year%4==0 and year%100==0:
#     print("It is a leap year")
# elif year%100==0 and year%400!=0:
#     print("it is a leap year")
# else:
#     print("it is not a leap year")


# # Check for leap year
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("It is a leap year")
# else:
#     print("It is not a leap year")

# write a program Leap day occurs in each year
# that is a multiple of 4, except for years evenly
# divisible by 100 but not by 400.

year = int(input("Enter a year: "))
if year%4==0:
    print("it is a leap year")
elif year%100==0 and year%400!=0:
    print("it is leap year")
else:
    print("it is not a leap year")


