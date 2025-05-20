"""
3.	Read and print the Name column from a CSV file.
o	Task: Read a CSV file named students.csv and print only the values from the Name column.
o	Expected Output:
o	Alice
o	Bob
o	Charlie

"""

# import csv

# with open("students.csv", newline="") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(row["Age"])


import csv

filename = "data112.csv"
new_row = ["indrayani", "23", "A+"]
with open(filename, "a") as file:
    writer_csv = csv.writer(file)
    writer_csv.writerow(new_row)

print(f"new row appended to {filename}")
