import csv
import sys

candidate_list = []
total_votes = 0
candidate_votes = []
winnerIndex = 0
currentWinningVotes = 0
sys.stdout = open('PyPoll/Analysis/analysis.txt','w')

# reads election_data.csv
with open('PyPoll/Resources/election_data.csv', mode = 'r') as pollcsv:
    # sets the delimiter and the file
    f = csv.reader(pollcsv, delimiter = ',')
    # skips the headers
    next(f, None)
    for x in f:
        total_votes += 1
        if not candidate_list.__contains__(x[2]):
            candidate_list.append(x[2])
            candidate_votes.append(0)
        for y in candidate_list:
            if(y == x[2]):
                candidate_votes[(candidate_list.index(y))] += 1

currentWinningVotes = candidate_votes[0]
print(candidate_list)
print(candidate_votes)
print(total_votes)

print("Election Results:")
print("-----------------")
print("Total Votes: " + str(total_votes))
print("-----------------")
for x in candidate_list:
    print(x + ": " + str((candidate_votes[candidate_list.index(x)]) / total_votes) + "%, "+ str(candidate_votes[candidate_list.index(x)]))
    if(candidate_votes[candidate_list.index(x)] > currentWinningVotes):
        winnerIndex = candidate_list.index(x)
        currentWinningVotes = candidate_votes[candidate_list.index(x)]
print("-----------------")
print("Winner: " + candidate_list[winnerIndex])