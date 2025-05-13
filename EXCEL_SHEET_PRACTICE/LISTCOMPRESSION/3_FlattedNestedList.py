"""
Flatten Nested List:
- Given a nested list `[[1, 2, 3], [4, 5, 6], [7, 8, 9]]`, use list comprehension to flatten it into
a single list.
"""

list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

nestedListCompression = [indexList for item in list for indexList in item]
print(nestedListCompression)
