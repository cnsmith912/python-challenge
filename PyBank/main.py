import os

import csv

#Define variables
csvpath = os.path.join("Resources", "budget_data.csv")
output_path = os.path.join("Analysis", "output.txt")
months = 0
profit = 0
average = 0
change_list = []
previous = 0



# Read in file
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)



# Loop to find net change

    for row in csvreader:
        months = months+1
        change = int(row[1])-previous
        previous = int(row[1])
        change_list = change_list + [change]
        profit = profit + float(row[1])

# Remove first value
    change_list.remove(867884)

# Sort and perform calculations
    change_total = sum(change_list)

    average = change_total/(months-1)

    change_list.sort()

# Print results



    output = "Financial Analysis"

    output += "\n--------------------------"

    output += f"\nTotal Months: {months}"

    output += f"\nTotal: {profit}"

    output += f"\nAverage change: {average}"

    output += f"\nGreatest Increase in Profit: {change_list[-1]}"

    output += f"\nGreatest Decrease in Profit: {change_list[0]}"


print(output)

# Specify the file to write to
with open(output_path, "w") as txt_file:
    
    txt_file.write(output)

# Open the file using "write" mode. Specify the variable to hold the contents

