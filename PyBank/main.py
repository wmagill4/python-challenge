#import dependencies
import os
import csv

# Files to load in and output
Budget_Data = os.path.join("budget_data.csv")
Output_File = os.path.join("budget_analysis.txt")

#declare variables
total_months = 0
total_net = 0
total_change_list = []
month_of_change = []
greatest_increase = ["", 0]
greatest_decrease = ["", 0]

#open csv
with open(Budget_Data) as data:
    reader = csv.reader(data)
    header = next(reader)

    #skip the header row
    first_row = next (reader)
    total_months = total_months + 1
    total_net = total_net + int(first_row[1])
    prev_net = int(first_row[1])
    
    #loop through all rows
    for row in reader:
        
        #track total months and end total budget
        total_months = total_months + 1
        total_net = total_net + int(row[1])
        #print (total_months)
        #print (total_net)

        #track total change
        total_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        total_change_list = total_change_list + [total_change]
        month_of_change = month_of_change + [row[0]]
        
        # Calculate the greatest increase
        if total_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = total_change
        

        #calculate greatest decrease
        if total_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = total_change

# Calculate the Average Net Change
net_monthly_avg = sum(total_change_list) / len(total_change_list)

# Generate Output Summary
output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average  Change: ${net_monthly_avg:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

print (output)

# Export the results to text file
with open(Output_File, "w") as txt_file:
    txt_file.write(output)
