import csv
import sys

if len(sys.argv) != 2:
    sys.exit("Bad arguments")

file = sys.argv[1]

""" using csv reader """
with open(file, "r") as ifile:
    reader = csv.reader(ifile)
    for row in reader:
        print(row[0],",", row[1], ",", row[2])

