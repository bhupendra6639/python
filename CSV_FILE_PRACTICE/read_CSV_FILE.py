import csv

with open("data.csv",newline="") as file:
      sample_Data=csv.reader(file)
      print(sample_Data)##buffer format data
      for data in sample_Data:
        print(data)