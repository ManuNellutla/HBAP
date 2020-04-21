"""
Splits managers' names into first and last.

Demonstrates a CSV writer.
"""

import csv
import sys

infile = "employees.csv"
outfile = "employees-update2.csv"


# Read rows from source
rows = []
with open(infile, "r") as file:

    # Initialize reader
    reader = csv.reader(file)

    # Read header
    header = next(reader)

    # Delete Manager from header
    del header[0]

    # Prepend ManagerLast and ManagerFirst to header
    header.insert(0, "ManagerLast")
    header.insert(1, "ManagerFirst")

    # Remember new header
    rows.append(header)

    # Iterate over rows
    for row in reader:

        # Split manager's name into first and last
        if row[0] != "":
            first, last = row[0].split(" ")
        else:
            first = ""
            last = ""

        # Remove Manager's full name
        del row[0]

        # Prepend manager's last name and first name to row
        row.insert(0, last)
        row.insert(1, first)

        # Remember new row
        rows.append(row)

# Write rows to destination
with open(outfile, "w") as file:
    writer = csv.writer(file)
    for row in rows:
        writer.writerow(row)
