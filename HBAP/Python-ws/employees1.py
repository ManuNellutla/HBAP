##
#  Read Employee CSV file
#  Get Frist Name, Last Name and Birthdate
#  Print as table format
##

import csv
from prettytable import PrettyTable

filename = "employees.csv"
t = PrettyTable(["Last Name","First Name", "Birth Date"])

# print employee's name
with open(filename, "r") as file:
    reader = csv.reader(file)
    next(reader)
    for col in reader:
        t.add_row([col[2] , col[1], col[4]])

print(t)