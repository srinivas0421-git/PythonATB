# input_string = "hello world"
# vowel = "aeiou"
# vowel_count = 0
#
# for char in input_string:
#     if char in vowel:
#         vowel_count=vowel_count+1
# print(vowel_count)
# # consonents in given string
#
# input_string1 = "hhyyeu"
# consonets = "hhyy"
# consonets_coount = 0
#
# for char in input_string1:
#     if char in consonets:
#         consonets_coount = consonets_coount + 1
# print(consonets_coount)
#count vowels in given string

# name="shanmukh"
# vowel="au"
# vowel_count=0
#
# for char in name:
#     if char in vowel:
#         vowel_count=vowel_count+1
# print(vowel_count)

# Count consonants in given string

# name="shanmukh"
# consonent1="shnmkh"
# consonent_c=0
#
# for char in name:
#     if char in consonent1:
#         consonent_c=consonent_c+1
# print(consonent_c)

#Right angle Triangle

# for i in range(1,6):
#     for j in range(i+1):
#         print("*",end="")
#     print()


#left angle triangle

for i in range(1,6):
    for j in range(6-i):
        print(" ",end="")
    for k in range(i):
        print("*",end="")
    print()