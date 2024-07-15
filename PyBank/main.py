#importing file using modules for it
import os
import csv
bankpath = os.path.join('..','Resources','Budget_data.csv')
# Reading using csv module. Open CSV file
with open(bankpath, encoding="utf-8") as bankfile:
    bankreader = csv.reader(bankfile)
    unique_months = set()

    # Skip the header row
    next(bankreader)  # Skip the header row
    
    # Loop through the rows in the CSV file
    for row in bankreader:
        date = row[0]  # Assuming the date is in the first column
        month = date.split(",")[0]  # Extract the month from the date. 1st element after split
        unique_months.add(month)

# Count the number of unique months
NUM_MONTHS = len(unique_months)
print("Total Months:",NUM_MONTHS)
