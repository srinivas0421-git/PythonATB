# my_list = [1, 2, 2, 3, 4, 4, 5]
# # Remove duplicates from a list using a set.
# # Output: [1, 2, 3, 4, 5]
# my_list1=set(my_list)
# print(my_list1)

# count the consonents in given string

in_string = "srinivas"
consonent = "srnv"
consonent_count = 0

for char in in_string:
    if char in consonent:
        consonent_count = consonent_count + 1
print(consonent_count)
