
#Modules
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
    print(total_months)
    print()
    
#print(len(total_months))
print(sum(net_profit))
print(H(net_profit))
print(M(net_profit))
print(N(net_profit))

# print()
# print("Financial Analysis")
# print("-------------------")
# print(f"Total Months:{len(total_months)}")
# print(f"Total: ${sum(net_profit)}")
# print(f"Average Change:{round(H(net_profit),2)}")
# print(f"Greatest Increase in Profits: {total_months[monthly_increase]} (${(str(increase))})")
# print(f"Greatest Decrease in Profits: {total_months[monthly_decrease]} (${(str(decrease))})")

# # export text file of results
# output = "output.txt"
# with open("output","w") as new:
#     new.write("Financial Analysis")
#     new.write("\n")
#     new.write("--------------------")
#     new.write("\n")
#     new.write(f"Total Months:{len(total_months)}")
#     new.write("\n")
#     new.write(f"Total: ${sum(net_profit)}")
#     new.write("\n")
#     new.write(f"Average Change: {round(sum(profit_change)/len(profit_change),2)}")
#     new.write("\n")
#     new.write(f"Greatest Increase in Profits: {total_months[monthly_increase]} (${(str(increase))})")
#     new.write("\n")
#     new.write(f"Greatest Decrease in Profits: {total_months[monthly_decrease]} (${(str(increase))})")




