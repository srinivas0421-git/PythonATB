year=int(input("Enter a year:"))

if year%100==0 and year%400==0:
    print("it is a leap year".format(year))
elif year%4==0 and year%100!=0:
    print("it is a leap year".format(year))
else:
    print("not a leap year")
