import re

def is_find_only_digits(input):
    return bool(re.fullmatch(r'\d+', input))

print(is_find_only_digits("12345")) 
print(is_find_only_digits("123a5"))