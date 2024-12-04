# Sort a dictionary by its values in descending order
import operator
# my_dict = {"a": 3, "b": 1, "c": 2}
#
# sort_d=sorted(my_dict.items(),key=operator.itemgetter(1))
# print("Dictionary in Ascending order by value:",sort_d)
# sort_d=sorted(my_dict.items(),key=operator.itemgetter(1),reverse=True)
# print("Dictionary in Descending order by value:",sort_d)


# dit={1:20,2:100,5:60,7:90}
#
# #sort the dictionary in ascending order by value
# sort_ad=sorted(dit.items(),key=operator.itemgetter(1))
# print(sort_ad)
#
# sort_ad=sorted(dit.items(),key=operator.itemgetter(1),reverse=True)
# print(sort_ad)

#Example3
# import operator
# fruits={"apple":1,"banana":4,"carrot":8,"beetroot":2,"corn":6}
# print(fruits)
#
# fruits_ao_do=sorted(fruits.items(),key=operator.itemgetter(1),reverse=False)
# print(fruits_ao_do)
#
# fruits_ao_do=sorted(fruits.items(),key=operator.itemgetter(1),reverse=True)
# print(fruits_ao_do)


#Example 4
import operator
from operator import itemgetter
from urllib.parse import ParseResult

fruits={'apple':2,'kiwi':1,'grapes':4,'orange':6}

fruits_ao=sorted(fruits.items(),key=operator.itemgetter(1),reverse=False)
print(fruits_ao)

#without reverse keyword we can print the dictionary in ascending order

fruits_ao1=sorted(fruits.items(),key=operator.itemgetter(1))
print(fruits_ao1)

#decending order by value
fruits_do=sorted(fruits.items(),key=operator.itemgetter(1),reverse=True)
print(fruits_do)


















