"""
Filter Odd Numbers:
- Given the list `[10, 21, 32, 43, 54, 65, 76, 87, 98]`, use list comprehension to extract only
the odd numbers.
"""

dummyList = [10, 21, 32, 43, 54, 65, 76, 87, 98]

oddnumberCompression = [item for item in dummyList if item % 2 != 0]
print(oddnumberCompression)
