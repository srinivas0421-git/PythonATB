def repeating_character(name):
    for char in name:
        if name.count(char)==1:
            return char
    return None

print(repeating_character("srinivas"))
print(repeating_character("dada"))
print(repeating_character("shanmukh"))