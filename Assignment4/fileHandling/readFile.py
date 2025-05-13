filePath = ("fileHandling\text.txt", "r")
with open(filePath) as file:
    service = file.readline()
    print(service)
