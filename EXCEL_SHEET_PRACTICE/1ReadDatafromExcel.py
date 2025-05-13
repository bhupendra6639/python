"""1. Read Data from Excel:
- Write a Python program using `pandas` to read data from an Excel file named `
data.xlsx` and print the first 5 rows of the first sheet.
"""

"""1. Read Data from Excel:
- Write a Python program using `pandas` to read data from an Excel file named `
data.xlsx` and print the first 5 rows of the first sheet.
"""

import pandas as pd

dataFrame = pd.read_excel("SampleData.xlsx")
print(dataFrame.head())
