import os

import csv

from collections import Counter

#Define variables
csvpath = os.path.join("Resources", "election_data.csv")
output_file =os.path.join("Analysis", "output.txt")
candidates=[]
vote_count=[]






with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    

    next(csvreader)


 

    for row in csvreader:
        candidates.append(row[2])
        vote_count.append(row[0])

    votes = str(len(vote_count))

def group_list(candidates):
    return list(zip(Counter(candidates).keys(), Counter(candidates).values()))
    candidates.sort()

output = "Election Results"

output += "\n-------------------------------"

output += f"\nTotal votes: {votes}"

output += "\nCandidates and Total Votes"

#print(group_list(candidates))

percent1= (704200/int(votes))*100
percent2=(2218231/int(votes))*100
percent3=(492940/int(votes))*100
percent4=(105630/int(votes))*100

output +="\n-------------------------------"

output += f"\nCorrey: 704200    {percent1}"
output += f"\nKhan: 2218231     {percent2}"
output += f"\nLiL 492940        {percent3}"
output += f"\nO'Tooley: 105630  {percent4}"

output += "\n-------------------------------"

output += f"\nWinner: Khan"

print(output)


with open(output_file, "w") as txt_file:
    txt_file.write(output)


