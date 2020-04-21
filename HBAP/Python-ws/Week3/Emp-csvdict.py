import csv
import sys

if len(sys.argv) != 2:
    sys.exit("Bad arguments")

file = sys.argv[1]

with open(file, "r") as ifile:
    reader = csv.DictReader(ifile)
    for row in reader:
        print(row["FirstName"],":", row["BirthDate"])
