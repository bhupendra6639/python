"""7. Filter and Square:
- From the list `[10, 15, 20, 25, 30]`, use list comprehension to create a new list containing
the squares of numbers that are greater than `20`.
"""

list1 = [10, 15, 20, 25, 30]
filterAndSquarCompression = [item**2 for item in list1 if item > 20]
print(filterAndSquarCompression)
