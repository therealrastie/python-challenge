# import Dependecies
import os
import csv
from pathlib import Path

# declaring file location
filepath = Path("C:/Users/randy/Desktop/python-challenge/" , "C:/Users/randy/Desktop/python-challenge/PyBank", "C:/Users/randy/Desktop/python-challenge/budget_data.csv")

# Create empty lists to iterate through specific rows for the following variables
total_months = []
total_profit = []
monthly_profit_change = []


# Open csv in default read mode with context manager
with open (filepath, newline="", encoding "utf-8") as budget:

  #store content of budget_data.csv in the variable csvreader
  csvreader = csv.reader(budget,delimiter=",")

# skip the header labels to iterate with the values
header = next(csvreader)

#iterate through all rows in the stored file contents
for row in csvreader: 

    # Append the total months and profits to their corresponding lists
    total_months.append(row[0])
    total_profit.append(int(row[1]))

    #iterate through the profits in order to get the monthly change in profit
    for i in range(len(total_profit)-1):
        #take the difference between two months and append to profit change
        monthly_profit_change.append(total_profit[i+1]-total_profit[i])
        #obtain maximum and minimum from the monthly profit change list
        max_increase_value = max(monthly_profit_change)
        max_decrease_value = min(monthly_profit_change)

        # Correlate max and min to the proper month using month list and index from max and min
#We use the plus 1 at the end since month associated with change is the + 1 month or next month
max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1 

# Print Statements

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")
        
