import csv

header = ["name", "age", "grade"]
new_row = [
    ["John", "18", "A"],
    ["Jane", "19", "B"],
    ["Mark", "17", "A"],
]
with open("dummyPractice11.csv", "a", newline="") as file:
    write = csv.writer(file)
    write.writerow(header)
    write.writerows(new_row)


# import csv

# header = ["name", "age", "grade"]
# new_row = [
#     ["John", "18", "A"],
#     ["Jane", "19", "B"],
#     ["Mark", "17", "A"],
# ]
# with open("dummy23.csv", "w", newline="") as file:
#     write = csv.writer(file)
#     write.writerow(header)
#     write.writerow(new_row)
