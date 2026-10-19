import csv

new_name = input("what`s your name?")
new_age = int(input("what`s your age?"))
new_data = [new_name, new_age]

with open("sample.csv", "a", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(new_data)