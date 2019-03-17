#  import dependencies
import os
import csv

#  path to .csv file for input and .txt file for output
bankdata = os.path.join("Resources/budget_data.csv")
summdata = os.path.join("Summary/budget_summary.txt")

#  define lists for gathering data
date = []
porl = []

#  read csv and append lists
with open(bankdata, 'r') as csvfile:
    csvread = csv.reader(csvfile)
    next(csvread, None)
    for row in csvread:
        date.append(row[0])
        porl.append(int(row[1]))

#  define variables to be used for output and print statement
#  tried to put these in after creating the lists, but it caused problems for the way I wanted to code this, so I put them here.
months = len(date)     #  Total number of months
tot_porl = 0     #  Total profit or loss over entire period. Set to Zero at start, will be modified in loop.
grinc_porl = porl[0]     #  Greatest increase in profit. Starting equal to first entry.
grdec_porl = porl[0]     #  Greatest decrease in profit. Starting equal to first entry.
#  will create variable for date of greatest profit and greatest loss during loop. adding them now makes this bothersome

#  Loop through list of profit and loos to find values for variables
#  I use "q" in this because other letters (i, j, etc.) reminded of VBA. I say "NO" to that! Also, the "q" stands out to me.
for q in range(len(porl)):
    if porl[q] >= grinc_porl:
        grinc_porl = porl[q]
        grinc_date = date[q]     #  variable for date of greatest profit
    elif porl[q] <= grdec_porl:  #  I thought else would go here, but it didn't like that, something I'll have to look into.
        grdec_porl = porl[q]
        grdec_date = date[q]
    tot_porl += porl[q]     #  I like "+=" (it made this code shorter) I also like the ""-=, *=, /="" operators, will use them in the future

#  create and calculate the average profit or loss
avg_porl = round(tot_porl / months, 2)     #  this also didn't like being at the top with the way I tried to write this code

#  I used this line to test my variables and debug code, just copy and pasted variables in to check before moving on
#  type(avg_porl), print(avg_porl)     # The variables I left plugged in are the last ones tested

#  print results of loops and data to terminal, do some formatting
print("------------------------------")
print("->   Financial Analysis     <-")
print("------------------------------")
print("")
print("Total Months: " + str(months))
print("Total: ${:,}".format(tot_porl))
print("Average Change: ${:,}".format(avg_porl))
print("Greatest Increase in Profit:  " + (grinc_date) + " (${:,})".format(grinc_porl))
print("Greatest Decrease in Profit:  " + (grdec_date) + " (${:,})".format(grdec_porl))
print("")
print("<End Summary>")

#  write the output text file and populate with data
with open(summdata, 'w',) as banksum:
    banksum.writelines("------------------------------" + '\n')
    banksum.writelines("->   Financial Analysis     <-" + '\n')
    banksum.writelines("------------------------------" + '\n')
    banksum.writelines("" + '\n')
    banksum.writelines("Total Months: " + str(months) + '\n')
    banksum.writelines("Total: ${:,}".format(tot_porl) + '\n')
    banksum.writelines("Average Change: ${:,}".format(avg_porl) + '\n')
    banksum.writelines("Greatest Increase in Profit:  " + (grinc_date) + " (${:,})".format(grinc_porl) + '\n')
    banksum.writelines("Greatest Decrease in Profit:  " + (grdec_date) + " (${:,})".format(grdec_porl) + '\n')
    banksum.writelines("" + '\n')
    banksum.writelines("<End Summary>" + '\n')
    banksum.close
    