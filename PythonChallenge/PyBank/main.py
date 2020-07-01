import csv
import sys

sys.stdout = open('PyBank/Analysis/analysis.txt','w')
months = 0
total = 0
average_change = 0
lastvalue = 0
currentvalue = 0
greatestinc = 0
greatestdec = 0
standard_deviation = 0
sum_of_sq_dev = 0
mean_to_date = 0
devls = []
greatincmonth = ""
greatestdecmonth = ""

# opens the csv file in the resources folder
with open('PyBank/Resources/budget_data.csv', mode = 'r') as budgetcsv:
    # sets the delimiter and the file
    f = csv.reader(budgetcsv, delimiter =',')
    # skips the headers
    next(f, None)
    # iterates through all values
    for x in f:
        # finds total months
        months = months + 1
        # finds total value of lines
        total = total + int(x[1])
        # finds value of greatest inc/dec
        currentvalue = int(x[1])
        if(lastvalue == 0):
            lastvalue = currentvalue
        if(currentvalue-lastvalue > 0):
            if((currentvalue-lastvalue) > greatestinc):
                greatestinc = currentvalue
                greatestincmonth = x[0]
        if(currentvalue-lastvalue < 0):
            if((currentvalue-lastvalue) < greatestdec):
                greatestdec = currentvalue
                greatestdecmonth = x[0]
        lastvalue = currentvalue
        # sets up list for standard deviation
        devls.append(int(x[1]))

mean_to_date = total / months
for x in devls:
    sum_of_sq_dev = (x - mean_to_date)
standard_deviation = (sum_of_sq_dev / months)
print("Financial Analysis")
print("------------------")
print("Total months: " + str(months))
print("Total: $" + str(total))
print("Average Change: " + str(standard_deviation))
print("Greatest Increase: $" + str(greatestinc) + " on " + greatestincmonth)
print("Greatest Decrease: $" + str(greatestdec) + " on " + greatestdecmonth)