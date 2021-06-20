
import os
import csv

#Set path for file
csvpath = os.path.join('Resources', 'budget_data.csv')

total_months = []
net_profit = []
profit_change = []

H=lambda L:sum([L[x+1]-L[x] for x in range(len(L)-1)])/(len(L)-1)
M=lambda L:max([L[x+1]-L[x] for x in range(len(L)-1)])
N=lambda L:min([L[x+1]-L[x] for x in range(len(L)-1)])

# Open and read csv
with open("Resources/budget_data.csv", newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

#iterate values to add to list
    for row in csvreader:
        total_months.append(row[0])
        net_profit.append(int(row[1]))
    #print(total_months)
    print()

    for row in csvreader:
        total_months.append(row[0])
        net_profit.append(int(row[1]))

    for i in range (len(net_profit)-1):
        profit_change.append(net_profit[i+1]-net_profit[i])
    
month_inc=profit_change.index(max(profit_change))+1
month_dec=profit_change.index(min(profit_change))+1

ans = []

ans.append("Financial Analysis\n-------------------------------")
ans.append(f"Total Months:{len(total_months)}")
ans.append(f"Total: ${sum(net_profit)}")
ans.append(f"Average Change:{round(H(net_profit),2)}")
ans.append(f"Greatest Increase in Profits: {total_months[month_inc]} (${(str(M(net_profit)))})")
ans.append(f"Greatest Decrease in Profits: {total_months[month_dec]} (${(str(N(net_profit)))})")

exp = 'Financial_Analysis.txt'

with open(exp, 'w') as file:
    for x in ans:
        print(x)
        file.write(x + '\n')

