#dependencies
import pandas as pd

# naming files
csvpath = input("What is the path/name of the csv file containing budget data?")

# create dataframes from files
budget = pd.read_csv(csvpath)


# finding how many months there are
months = budget['Date'].nunique()

#total amount of revenue
revenue = budget['Revenue'].sum()

budget['Monthly Delta'] = 0

# looping trhough to find the monthly delta.
# Monthly delta defined as current month minus the previous month
for i in range(len(budget)-1):
    budget.iloc[i + 1, 2] = budget.iloc[(i + 1), 1] - budget.iloc[i, 1]
    i += 1

# Finding the average monthly chage
avg_delta = budget['Monthly Delta'].mean()

# Finding the maximimum monthly change
max_delta = budget.iloc[budget['Monthly Delta'].argmax()]

# Finding the minimum monthly change
min_delta = budget.iloc[budget['Monthly Delta'].argmin()]

#creating a list that can be written to a file
financial_analysis = ["Financial Analysis" "\n--------------------",
                      "\nTotal Months:", str(months), "\nRevenue:", str(revenue),
                      "\nAverage Revenue Change:", str(avg_delta), 
                      "\nGreatest Increase in Revenue:", str(max_delta.iloc[0]), 
                      "($", str(max_delta.iloc[2]), ")",
                      "\nGreatest Decrease in Revenue:", str(min_delta.iloc[0]), 
                      "($", str(min_delta.iloc[2]), ")"]

print(financial_analysis)

#writing to file
with open('financial_analysis.txt', 'w') as txtfile:
    txtfile.writelines(financial_analysis)
