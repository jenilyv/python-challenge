# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
# file_to_load = os.path.join("C:\\Users\\jilyayeva\\Downloads\\Starter_Code(1).zip\\Starter_Code\\PyBank\\Resources\\budge_data.csv")  # Input file path
# file_to_output = os.path.join("C:\\Users\\jilyayeva\\Downloads\\Starter_Code(1).zip\\Starter_Code\\PyBank\\analysis")  # Output file path

file_to_load = "C:\\9_23_24HW\\PyBank\\Resources\\budget_data.csv"
file_to_output = "C:\\9_23_24HW\\PyBank\\analysis\\analysis"
# Define variables to track the financial data

# Add more variables to track other necessary financial data

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    # Track the total and net change
    total_months = 1
    total_net = int(first_row[1])
    total_avg = 0
    prev_net = int(first_row[1])
    maxChange = -999999999999
    maxMonth = ""
    minChange = 999999999999
    minMonth = ""
    # Process each row of data
    for row in reader:
        # Track the total
        total_months = total_months + 1
        total_net = total_net + int(row[1]) 
        currentChange = int(row[1]) - prev_net
        total_avg += currentChange
        if maxChange < currentChange:
            maxChange = currentChange
            maxMonth = row[0]
        if minChange > currentChange:
            minChange= currentChange
            minMonth = row[0]
        prev_net = int(row[1])
        # Track the net change

    total_avg = round(total_avg / (total_months - 1), 2)

        # Calculate the greatest increase in profits (month and amount)

        # Calculate the greatest decrease in losses (month and amount)

financial_data.close()

# Generate the output summary
output = "Total Months: " + str(total_months) + "\nTotal: " + str(total_net) + "\nAverage Change: " + str(total_avg) + "\nGreatest Increase in Profits: " + maxMonth + " (" + str(maxChange) + ")" + "\nGreatest Decrease in Profits: " + minMonth + " (" + str(minChange) + ")"

with open(file_to_output, "w") as txt_file:
    txt_file.write(output)

print(output)


