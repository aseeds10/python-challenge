# get file and using modules for it
import os
import csv
bankpath = os.path.join('..','Resources','Budget_data.csv')

#initialize starters
unique_months = set()
TOTAL_PROFIT_LOSSES = 0
changes_in_profit_losses = []
previous_profit_loss = None

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

        #if conditional to see changes in current vs previous row
        if previous_profit_loss is not None: #[]
            change = profit_loss - previous_profit_loss
            changes_in_profit_losses.append(change) #add each change from each comparison to list with changes
        previous_profit_loss = profit_loss #for next comparison, make current the "previous"
# Calculate total number of months
NUM_MONTHS = len(unique_months)
print("Total Months:", NUM_MONTHS)

# Calculate net total Profit/Loss
print("Total: $", TOTAL_PROFIT_LOSSES)

# Calculate the average of changes in Profit/Losses
average_change = sum(changes_in_profit_losses) / len(changes_in_profit_losses)
print("Average Change: $", round(average_change, 2))

#now that have list of the changes over the period, can just do min and max for greatest incr and decr.placing here so after loop ends
greatest_increase = max(changes_in_profit_losses)
greatest_decrease = min(changes_in_profit_losses) #hopefully works keeping into account negative values

# Find the corresponding dates for the greatest increase and decrease. using index function to get row/placement
index_greatest_increase = changes_in_profit_losses.index(greatest_increase)
index_greatest_decrease = changes_in_profit_losses.index(greatest_decrease)
#make list by converting unique months set. maybe should have made it a list from the beginning?
dates = list(unique_months)
date_greatest_increase = dates[index_greatest_increase+1]  # Add 1 to account for skipping the first row
date_greatest_decrease = dates[index_greatest_decrease+1]  # Add 1 to account for skipping the first row
print("Greatest Increase in Profits:", date_greatest_increase, "($", greatest_increase, ")")
print("Greatest Decrease in Profits:", date_greatest_decrease, "($", greatest_decrease, ")")
#dates are different when I run them? but min and mx number stays the same...
# Specify the file to write to
