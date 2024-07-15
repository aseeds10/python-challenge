# get file and using modules for it
import os
import csv
bankpath = os.path.join('..','Resources','Budget_data.csv')

#initialize starters
unique_months = set()
TOTAL_PROFIT_LOSSES = 0

# Reading using csv module. Open CSV file
with open(bankpath, encoding="utf-8") as bankfile:
    bankreader = csv.reader(bankfile)
    next(bankreader)  # Skip the header row
    
    for row in bankreader:
        date = row[0]  # the date is in the first column
        month = date.split(",")[0]
        unique_months.add(month)

        profit_loss = int(row[1])  # Assuming profit/loss is in the second column
        TOTAL_PROFIT_LOSSES += profit_loss
# Calculate total number of months
NUM_MONTHS = len(unique_months)
print("Total Months:", NUM_MONTHS)

# Calculate net total Profit/Loss
print("Total: $", TOTAL_PROFIT_LOSSES)