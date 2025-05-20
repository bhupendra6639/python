import sys

Filename = sys.argv[1]  # file name
try:
    with open(Filename, "r") as file:
        for line in file:
            print(line.split())
except FileNotFoundError:
    print("File not found.")
