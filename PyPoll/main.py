import os
import csv

total_votes = 0
candidates = []
votes_candidates = []

csvpath = os.path.join('Resources', 'election_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader,None) 

    for row in csvreader:
        total_votes += 1
        if total_votes == 1:
            candidates.append(row[2])
            votes_candidates.append(1)
        else:
            try:
                icandidate = candidates.index(row[2])
                votes_candidates[icandidate] += 1
            except:
                candidates.append(row[2])
                votes_candidates.append(1)

ans = []
ans.append("Election Results\n-------------------------")
ans.append(f"Total Votes: {total_votes}\n-------------------------")

winner = candidates[0]
maxvotes = votes_candidates[0]
for i in range(len(candidates)):
    if votes_candidates[i] > maxvotes:
        winner = candidates[i]
        maxvotes = votes_candidates[i]
    percent = 100 * votes_candidates[i] / total_votes
    ans.append(f"{candidates[i]}: {round(percent,3)} % ({votes_candidates[i]})")

ans.append(f"-------------------------\nWinner: {winner}\n-------------------------")

exp = 'Elections_Analysis.txt'
with open(exp, 'w') as file:
    for result in ans:
        print(result)
        file.write(result + '\n')