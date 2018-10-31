import csv

csv_file = open("example.csv", "r")
csv_reader = csv.reader(csv_file)
for row in csv_reader:
    print(row)

csv_file.close()
