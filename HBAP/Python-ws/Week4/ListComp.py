"""
understanding List comprhensions
"""
import csv
from prettytable import PrettyTable

filename = "../Week3/employees.csv"

def birthdate(e):
    return e["BirthDate"]

with open(filename, "r") as file:
    # using Dict reader to get access to header column names
    reader = csv.DictReader(file)
    # put all of them into employees list
    employees = [row for row in reader]

# how about printing into table
t = PrettyTable(["Last Name","First Name", "Birth Date"])
# Iterate over employees list
for employee in sorted(employees, key=birthdate):
    t.add_row([employee["LastName"], employee["FirstName"], employee["BirthDate"]])

# Finally print table
print(t)
