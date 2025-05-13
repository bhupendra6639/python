"""
3.	Read and print the Name column from a CSV file.
o	Task: Read a CSV file named students.csv and print only the values from the Name column.
o	Expected Output:
o	Alice
o	Bob
o	Charlie

"""

import csv

with open("students.csv", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["Age"])
