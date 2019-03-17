{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 73,
   "metadata": {},
   "outputs": [],
   "source": [
    "# import dependencies\n",
    "import os\n",
    "import csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "metadata": {},
   "outputs": [],
   "source": [
    "# path to .csv file for input and .txt file for output\n",
    "bankdata = os.path.join(\"Resources/budget_data.csv\")\n",
    "summdata = os.path.join(\"Summary/budget_summary.txt\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "metadata": {},
   "outputs": [],
   "source": [
    "# define lists for gathering data\n",
    "date = []\n",
    "porl = []"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "metadata": {},
   "outputs": [],
   "source": [
    "# read csv and append lists\n",
    "with open(bankdata, 'r') as csvfile:\n",
    "    csvread = csv.reader(csvfile)\n",
    "    next(csvread, None)\n",
    "    for row in csvread:\n",
    "        date.append(row[0])\n",
    "        porl.append(int(row[1]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "metadata": {},
   "outputs": [],
   "source": [
    "# define variables to be used for output and print statement\n",
    "# tried to put these in after creating the lists, but it caused problems for the way I wanted to code this, so I put them here.\n",
    "months = len(date)     # Total number of months\n",
    "tot_porl = 0     # Total profit or loss over entire period. Set to Zero at start, will be modified in loop.\n",
    "grinc_porl = porl[0]     # Greatest increase in profit. Starting equal to first entry.\n",
    "grdec_porl = porl[0]     # Greatest decrease in profit. Starting equal to first entry.\n",
    "# will create variable for date of greatest profit and greatest loss during loop. adding them now makes this bothersome"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Loop through list of profit and loos to find values for variables\n",
    "# I use \"q\" in this because other letters (i, j, etc.) reminded of VBA. I say \"NO\" to that! Also, the \"q\" stands out to me.\n",
    "for q in range(len(porl)):\n",
    "    if porl[q] >= grinc_porl:\n",
    "        grinc_porl = porl[q]\n",
    "        grinc_date = date[q]     # variable for date of greatest profit\n",
    "    elif porl[q] <= grdec_porl:  # I thought else would go here, but it didn't like that, something I'll have to look into.\n",
    "        grdec_porl = porl[q]\n",
    "        grdec_date = date[q]\n",
    "    tot_porl += porl[q]     # I like \"+=\" (it made this code shorter) I also like the \"\"-=, *=, /=\"\" operators, will use them in the future"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "metadata": {},
   "outputs": [],
   "source": [
    "# create and calculate the average profit or loss\n",
    "avg_porl = round(tot_porl / months, 2)     # this also didn't like being at the top with the way I tried to write this code"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "metadata": {},
   "outputs": [],
   "source": [
    "# I used this line to test my variables and debug code, just copy and pasted variables in to check before moving on\n",
    "# type(avg_porl), print(avg_porl)     # The variables I left plugged in are the last ones tested"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "------------------------------\n",
      "->   Financial Analysis     <-\n",
      "------------------------------\n",
      "\n",
      "Total Months: 86\n",
      "Total: $38,382,578\n",
      "Average Change: $446,309.05\n",
      "Greatest Increase in Profit:  Feb-2012 ($1,170,593)\n",
      "Greatest Decrease in Profit:  Sep-2013 ($-1,196,225)\n",
      "\n",
      "<End Summary>\n"
     ]
    }
   ],
   "source": [
    "#print results of loops and data to terminal, do some formatting\n",
    "print(\"------------------------------\")\n",
    "print(\"->   Financial Analysis     <-\")\n",
    "print(\"------------------------------\")\n",
    "print(\"\")\n",
    "print(\"Total Months: \" + str(months))\n",
    "print(\"Total: ${:,}\".format(tot_porl))\n",
    "print(\"Average Change: ${:,}\".format(avg_porl))\n",
    "print(\"Greatest Increase in Profit:  \" + (grinc_date) + \" (${:,})\".format(grinc_porl))\n",
    "print(\"Greatest Decrease in Profit:  \" + (grdec_date) + \" (${:,})\".format(grdec_porl))\n",
    "print(\"\")\n",
    "print(\"<End Summary>\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "metadata": {},
   "outputs": [],
   "source": [
    "# write the output text file and populate with data\n",
    "with open(summdata, 'w',) as banksum:\n",
    "    banksum.writelines(\"------------------------------\" + '\\n')\n",
    "    banksum.writelines(\"->   Financial Analysis     <-\" + '\\n')\n",
    "    banksum.writelines(\"------------------------------\" + '\\n')\n",
    "    banksum.writelines(\"\" + '\\n')\n",
    "    banksum.writelines(\"Total Months: \" + str(months) + '\\n')\n",
    "    banksum.writelines(\"Total: ${:,}\".format(tot_porl) + '\\n')\n",
    "    banksum.writelines(\"Average Change: ${:,}\".format(avg_porl) + '\\n')\n",
    "    banksum.writelines(\"Greatest Increase in Profit:  \" + (grinc_date) + \" (${:,})\".format(grinc_porl) + '\\n')\n",
    "    banksum.writelines(\"Greatest Decrease in Profit:  \" + (grdec_date) + \" (${:,})\".format(grdec_porl) + '\\n')\n",
    "    banksum.writelines(\"\" + '\\n')\n",
    "    banksum.writelines(\"<End Summary>\" + '\\n')\n",
    "    banksum.close"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
