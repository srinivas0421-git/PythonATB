# Write a program that classifies a triangle based on
# its side lengths. Given three input values representing the lengths of the sides,
# determine if the triangle is equilateral (all sides are equal), isosceles
# (exactly two sides are equal), or scalene (no sides are equal). Use an
# if-else statement to classify the triangle.

s1=int(input("Enter a side1: "))
s2=int(input("Enter a side2: "))
s3=int(input("Enter a side3: "))

if s1==s2==s3:
    print("Equilateral")
elif s1==s2!=s3:
    print("isosceles")
else:
    print("scalene triangle")
