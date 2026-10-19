import csv

with open("sample.csv" , "r" , encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row['Name'],row['Age'])