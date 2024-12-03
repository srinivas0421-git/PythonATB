# my_dict={'a':1,'b':2,'c':3,'d':2}
# print(my_dict)#Aeccess the dictionaries
# d1={}
# for key,value in my_dict.items():
#     if value not in d1.values():
#         d1[key]=value
#     print(d1)


my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 2}
print(my_dict)
d1 = {}
for key, value in my_dict.items():
    if value not in d1.values():
        d1[key] = value
print(d1)
