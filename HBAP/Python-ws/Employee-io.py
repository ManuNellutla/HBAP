# Read employee cSV file and
# Split manager name into first and last name
# Write OUt the file again

import csv

infile = "employees.csv"
outfile = "employees-update.csv"

newRow = "Mgr Last Name, Mgr First Name "
row =""
rows =[]
x = ""

with open(infile, "r") as file:
    reader = csv.reader(file)
    header = next(reader)

    # sleepy now but try reading col1 ... n and attach column 0 to new row
    row = newRow + "," + ",".join(header[1:])
    print(row)
    rows.append(row)
    print(rows)
    for col in reader:
        if col[0] != "":
            x = col[0].split(" ")
            rows.append(x[1], ",", x[0], ",", ",".join(col[1:]))
        else:
            x = ","
            rows.append(x + ",".join(col[1:]))

with open(outfile, "w") as file1:
        writer = csv.writer(file1)
        for y in rows:
            print(y)
            writer.writerow([y])
            #writer.writerow([y])
