#-*- coding: utf-8 -*-

# Let's start with files

#Create a new file
file = open("new_testfile.txt", "w")
file.write('Hello!\n')
file.write('This is our new text file\n')
file.write('and this is another line.\n')
file.write('Why? Because we can.\n')

file.close()


#Append new information in an existant file
append_file = open("new_testfile.txt", "a")
append_file.write("Second contribuition, now it's an append!!!!\n")
append_file.close()

#Read all the file
read_file = open("new_testfile.txt", "r")
print((read_file.read()))
read_file.close()

#Read only the first characters
read_file = open("new_testfile.txt", "r")
print((read_file.read(5)))
read_file.close()


#Read one line
line_file = open("new_testfile.txt", "r")
print((line_file.readline()))
line_file.close()


#Read all lines
lines_file = open("new_testfile.txt", "r")
print((lines_file.readlines()))
lines_file.close()


#iterate all lines in file

file = open("new_testfile.txt", "r")
for line in file:
    print(line)


#With Statement

with open("new_testfile.txt", "r") as file:
    for line in file:
        print(line)


#Now we can try to read csv files

import csv

csv_file = open("example.csv", "r")
csv_reader = csv.reader(csv_file)
for row in csv_reader:
    print (row)

csv_file.close()


csv_file = open("csv_example_other_delimiter.csv", "r")
csv_reader = csv.reader(csv_file, delimiter=';')
for row in csv_reader:
    print("ROW DATA START")
    for data in row:
        print(data)
    print("ROW DATA FINISH\n")

csv_file.close()


with open("example.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        print(row)

#And we can also write csv files


with open("example_writter.csv", "w") as csv_file:
    csv_writter = csv.writer(csv_file, delimiter='|')
    csv_writter.writerow(['Name', 'Month', 'Cost'])
    csv_writter.writerow(['ExpoQA', 'June', '800'])
    csv_writter.writerow(['EuroStar', 'November', '1900'])
    csv_writter.writerow(['Agile Testing Days', 'October', '1200'])


with open("example_writterDict.csv", "w") as csv_file:
    fieldnames = ['Name', 'Month', 'Cost']
    csv_writter = csv.DictWriter(csv_file, delimiter='|', fieldnames=fieldnames)

    csv_writter.writeheader()
    csv_writter.writerow({'Month': 'June', 'Cost': '800', 'Name': 'ExpoQA'})
    csv_writter.writerow({'Name': 'EuroStar', 'Month': 'November', 'Cost': '1900', })
    csv_writter.writerow({'Cost': '1200', 'Name': 'Agile Testing Days', 'Month': 'October'})


# ===============================================================================
# SOURCES:
#  - https://docs.python.org/2/tutorial/inputoutput.html
#  - https://docs.python.org/2/library/csv.html
# ===============================================================================
