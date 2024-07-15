#get file and use modules to read/use them
import os
import csv
pollpath = os.path.join('..','Resources','election_data.csv')

#initialize starters
unique_votes=set()
unique_candidates=set()
#add the rest of starters here, once do this step

# Reading using csv module. Open CSV file
with open(pollpath, encoding="utf-8") as pollfile:
    pollreader = csv.reader(pollfile)
    next(pollreader)  # Skip the header row
    for row in pollreader:
        ballot_id_column = row[0] #ballot id in 1st column
        vote = ballot_id_column.split(",")[0] #1st element after comma split
        unique_votes.add(vote) #add unique vote to set after each loop

        candidate_column=row[2] #3rd column
        candidate = candidate_column.split(",")[0] #1st elmen after comma split? 
        #note to self: I don't think split was necessary but was not sure how to add to set without this
        unique_candidates.add(candidate) #add unique candidate to set after each loop
#calculations based on above loops etc
#calc total votes
NUM_VOTES=len(unique_votes)
print("Total Votes: ",NUM_VOTES)
#calc total candidates. do not need to print
NUM_CANDIDATES=len(unique_candidates)
print(NUM_CANDIDATES)
# Specify the file to write to
#output_path = os.path.join('..','Analysis','PyPoll_Results.txt')
# Open the file using "write" mode. Specify the variable to hold the contents
#with open(output_path, 'w') as file:
    #file.write("Election Results\n")
    #file.write("-------------------------\n")
    #file.write(f"Total Votes: {NUM_VOTES}\n")
    #file.write("-------------------------\n")
    #fix so shows votes received by 1st candidate file.write(f"Total: {TOTAL_PROFIT_LOSSES}\n")
    #fix so shows votes received by 2nd candidate file.write(f"Total: {TOTAL_PROFIT_LOSSES}\n")
    #fix so shows votes received by 3rd candidate file.write(f"Total: {TOTAL_PROFIT_LOSSES}\n")
    #file.write("-------------------------\n")
    #file.write(f"Winner: {[remove these brackets, insert variable that stores winner]}\n")
    #file.write("-------------------------\n")
#print("Results exported to PyPoll_Results.txt")
# End-of-file (EOF)