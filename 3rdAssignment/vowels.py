string = "ProgrammingAA"
vowels = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

for character in string:
    if character.lower() not in vowels:
        continue
    else:
        vowels[character] = vowels[character] + 1

print(vowels)
