#Source: https://stackoverflow.com/questions/53809815/typeerror-unsupported-operand-types-for-sub-str-and-int-on-line-8
#Define payment, knowing that up to 40 hours it is normal rate, and above that every hour is paid at 150%.
totalHours = input("Enter the total amount of worked hours:\n")
hourlyWage = input("Enter the payrate per hour:\n")
if totalHours <= 40:
    regularHours = totalHours
    overtime = 0
else:
    overtime = float(input(totalHours - 40))
    regularHours = float(input(40))
payment = hourlyWage*regularHours + (1.5*hourlyWage)*overtime
print (payment)