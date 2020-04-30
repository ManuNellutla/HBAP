import sys
import csv
import pandas as pd

employeefile = "../Week3/employees.csv"

with open(employeefile, newline='') as f:
    try:
        # Process CSV file
        # printing, verbatim, Manager,LastName,FirstName, on a line of its own, and
        # printing, for each employee in employees.csv, on a line of its own, the employee’s manager, followed by a          #comma, the employee’s last name, followed by a comma, and the employee’s first name.
        eedf = pd.read_csv(f, header=0, na_filter=False)
        eedf.fillna('')
        sLength = len(eedf['FirstName'])
        eedf = eedf.assign(ID=list(range(1, sLength + 1)))
        eedf = eedf.assign(FirstLastName=eedf['FirstName'] + " " + eedf['LastName'])

        print(eedf)

        print(f"ID,Manager,LastName,FirstName")
        for row in eedf.itertuples():
            if len(eedf[eedf['FirstLastName'] == row.Manager]) > 0:
                managerID = eedf[eedf['FirstLastName'] == row.Manager].iloc[0].ID
            else:
                managerID = ''
            print(f"{row.ID},{managerID},{row.LastName},{row.FirstName}")

    # Exception handling for any errors reading file
    except csv.Error as e:
        sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))
