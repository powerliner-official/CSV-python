import csv

delete = []

with open("sample.csv" , mode = "w" , encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(delete)