from unittest.mock import AsyncMock

score=int(input("Enter a Marks:"))

if score>=90 and score<=100:
    print("Grade is: A")
elif score>=80 and score<=90:
    print("Grade is:B")
elif score>=70 and score<=80:
    print("Grade is:C")
elif score>=60 and score<=70:
    print("Grade is:D")
elif score>=0 and score<=59:
    print("Grade is: F")
elif score>=100 and score<=-1:
    print("You are superman not eligible for grades")
else:
    print("Invalid inputs")


