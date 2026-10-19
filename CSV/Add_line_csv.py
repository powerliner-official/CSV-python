import csv

new_name = input("what`s your name?")
new_age = int(input("how old you are?"))
new_data = [new_name, new_age]

with open("sample.csv", "a", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(new_data)