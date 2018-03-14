#dependencies
import pandas as pd

# naming files
csvpath = input("What is the path/name of the csv file containing election data?")

# create dataframes from files
poll_data = pd.read_csv(csvpath)

poll_data.head()

#find total number of votes
vote_count = poll_data.shape[0]

# get a list of vote getters, calculate the percentage of vote, and reset the index
vote_getters = pd.DataFrame(poll_data["Candidate"].value_counts())
vote_getters['%_Vote'] = vote_getters['Candidate'] / vote_getters['Candidate'].sum() 
vote_getters.reset_index(inplace = True)

#rename the columns
vote_getters.rename(columns = {"index": "Candidate", "Candidate": "Total_Votes"}, inplace = True)

#define the winner
winner = vote_getters.iloc[vote_getters['%_Vote'].argmax()]

election_summary = []
i = 0
for candidate in vote_getters:
    election_summary.append(list(vote_getters.values[i]))
    i += 1
election_summary

election_results = ["Election Results" "\n--------------------\n", 
                    "Candidate, number of votes, and % of votes:\n",
                    str(election_summary), "\n",
                    "\nTotal Votes: ", str(vote_count),
                    "\nWinner: ", str(winner['Candidate'])]

print(election_results)

with open('election_results.txt', 'w') as txtfile:
    txtfile.writelines(election_results)
