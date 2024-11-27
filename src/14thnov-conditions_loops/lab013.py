# Write a program that classifies a triangle based on its side lengths. Given three input
# values representing the lengths of the sides, determine if the triangle is
# equilateral (all sides are equal), isosceles (exactly two sides are equal),
# or scalene (no sides are equal). Use an if-else statement to classify the triangle.

t1=int(input("Enter side1:  "))
t2=int(input("Enter side2: "))
t3=int(input("Enter side3: "))

if t1==t2==t3:
    print("triangle")
elif t1==t2:
    print("equilateral")
else:
    print("scalene")


