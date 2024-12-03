input_string = "hello world"
vowel = "aeiou"
vowel_count = 0

for char in input_string:
    if char in vowel:
        vowel_count=vowel_count+1
print(vowel_count)
# consonents in given string

input_string1 = "hhyyeu"
consonets = "hhyy"
consonets_coount = 0

for char in input_string1:
    if char in consonets:
        consonets_coount = consonets_coount + 1
print(consonets_coount)
