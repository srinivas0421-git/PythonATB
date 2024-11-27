marks = int(input("Enter marks: "))
if marks>=90 and marks <= 100:
    print("Student Grade is: A")
elif marks >= 80 and marks <= 89:
    print("Student Grade is: B")
elif marks >= 70 and marks <= 79:
    print("Student Grade is: C")
elif marks >= 60 and marks <= 69:
    print("student Grade is: D")
elif marks >= 0 and marks <= 59:
    print("Student Grade is: F")
else:
    print("Invalid input")
