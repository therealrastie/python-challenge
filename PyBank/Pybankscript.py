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
        
