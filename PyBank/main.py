#import csv using module for it
import os
import csv
bankpath = os.path.join ('..','python-challenge','PyBank', 'Resources', 'budget_data.csv')
#reading using csv moduule. open csv file
with open(bankpath, encoding='UTF-8') as bankfile:
    bankreader = csv.reader(bankfile)
    # Create a set to store unique months
    unique_months = set()

    # Loop through the rows in the CSV file
    for row in bankreader:
        date = row['Date']
        month = date.split("-")[1]
        unique_months.add(month)

# Count the number of unique months
Num_Months = len(unique_months)
print("Total Months:",Num_Months)
