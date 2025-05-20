"""Task: Write a Python program to create a CSV file named students.csv with the following data:
Name, Age, Grade
Alice, 20, B
Bob, 22, A
Charlie, 21, C
"""

import csv

header = ["Name", "Age", "Grade"]
rows = [["Alice", 20, "B"], ["Bob", 22, "A"], ["Charlie", 21, "C"]]
rows1 = [["Alice", 20, "B"], ["Bob", 22, "A"], ["Charlie", 21, "C"]]

with open("students.csv", "a+", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(rows)
    writer.writerows(rows1)

print("students.csv created successfully.")
