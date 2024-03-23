import csv
csv.register_dialect('csv_dialect', delimiter='|', skipinitialspace=True, quoting=csv.QUOTE_ALL)
with open('temp.csv', 'r') as csvfile:
    for row in reader:
        print(row)