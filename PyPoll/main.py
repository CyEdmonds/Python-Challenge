#  import dependencies
import os
import csv

#  create path to input data
polldata = os.path.join("Resources/election_data.csv")
summpoll = os.path.join("Summary/election_results.txt")

#  create a dictionary for storing election data
election = {}

#  define lists for gathering data
candidate = []
cand_vote = []
percent = []
winnerlst = []

#  set initial total votes to zero
total_votes = 0

#  Read the csvfile, skipping header and parse data to the dictionary
with open(polldata, 'r') as csvfile:
    csvread = csv.reader(csvfile)
    next(csvread, None)
    for row in csvread:
        if row[2] in election.keys():
            election[row[2]] = election[row[2]]+1
        else:
            election[row[2]] = 1
        total_votes += 1

#  fill lists with data from dictionary keys
for key, value in election.items():
    candidate.append(key)
    cand_vote.append(value)
# print(election)     #  for checking and debugging, note: had to reset kernel when running from jupyter notebook

#  calculates percent of total votes each candidate received
for q in cand_vote:
    percent.append(round(q/total_votes*100, 1))
# percent     #  checking and debugging

#  create tuple from lists
cand_tpl = list(zip(candidate, cand_vote, percent))
# cand_tpl     #  checking and debugging

#  determine winner  (accounts for a tie)
for name in cand_tpl:
    if max(cand_vote) == name[1]:
        winnerlst.append(name[0])
        winner = winnerlst[0]     #  originally created this variable with others at top, moved here when code caused problems
        if len(winnerlst) > 1:
            for r in range(1, len(winnerlst)):
                winner = winner + "," + winnerlst[r]
# winner     #  checking and debugging, note: can check to see if above loop works by running multiple times in jupyter nb

#  write data to output file 'election_results.txt'
with open(summpoll, 'w') as tally:
    tally.write("------------------------------" + '\n')
    tally.write("->     Election Results     <-" + '\n')
    tally.write("------------------------------" + '\n')
    tally.write("Total Votes: " + str(total_votes) + '\n')
    tally.write("------------------------------" + '\n')
    for entry in cand_tpl:
        tally.write(entry[0] + ": " + str(entry[2]) + "% (" + str(entry[1]) + ")" + '\n')
    tally.write("------------------------------" + '\n')
    tally.write("Winner: " + winner + '\n')
    tally.write("------------------------------" + '\n')
    tally.close

    #  print 'election_results.txt' to terminal
with open(summpoll, 'r') as terminaltally:
    print(terminaltally.read())
    