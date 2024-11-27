# from unittest.mock import AsyncMock
#
# score=int(input("Enter a Marks:"))
#
# if score>=90 and score<=100:
#     print("Grade is: A")
# elif score>=80 and score<=90:
#     print("Grade is:B")
# elif score>=70 and score<=80:
#     print("Grade is:C")
# elif score>=60 and score<=70:
#     print("Grade is:D")
# elif score>=0 and score<=59:
#     print("Grade is: F")
# elif score>=100 and score<=-1:
#     print("You are superman not eligible for grades")
# else:
#     print("Invalid inputs")
#

# class program:
#     def __init__(self,age=0):
#         self._age=age
#     def set_age(self,a):
#         self._age=a
#     def get_age(self):
#         return self._age
#
# obj=program()
# obj.set_age(21)
# age1=obj.get_age()
# print(age1)
# print(obj._age)

class program:
	def __init__(self,stid=0):
		self._stid=stid
	def set_stid(self,a):
		self._stid=a
	def get_stid(self):
		return self._stid
obj=program()
obj.set_stid(21)
print(obj.get_stid())
print(obj._stid)
