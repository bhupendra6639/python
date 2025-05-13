"""
Uppercase Conversion:
- Given a list of strings `[apple, banana, cherry]'
 use list comprehension to create a new
list with all strings in uppercase.
"""

FruitsList = ["apple", "banana", "cherry"]      
FruitsListCompression = [fruit.upper() for fruit in FruitsList]
print(FruitsListCompression)
