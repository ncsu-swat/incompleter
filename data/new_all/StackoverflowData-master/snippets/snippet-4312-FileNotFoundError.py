#Source: https://stackoverflow.com/questions/59900756/attributeerror-list-object-has-no-attribute-strftime-python-3-csv-socrati
##################################      C.omma, S.eperated,V.alue       ################################################

# https:// ten years of googles stock prices to practise manipulating data.

#   Most small amounts of data are stored in a spread sheet and larger amounts of data are stored in databases.
#   However CSV's have a place. They are easy, no drivers or api's are needed.

#  Header - first entry of data in the list
#   Data - all the rest of the data
#    - Each row data(like a record in a data base) is seperated by comma's and everything is a string.
#    - Two commas in a row ',,' means there is a missing piece of data.
import time
import csv
from datetime import datetime



path = (r"C:\Users\mexib\Socratica Learning\Google Stock Market Data - google_stock_data.csv.csv")
file = open(path, newline='')
#                          ^ adding empty brackets makes this keyword arg(kwarg) universal for different pc's
reader = csv.reader(file)   # Using the reader function here parse the data

header = next(reader)       # The first line is the header so we use next fucntion to get to the data.

#   at this point the list has been parsed but each element of this list is still a string.

data = []
for row in reader:
    # row = [Date, Open, High, Low, CLose, Volume, Adj. Close]
    date = datetime.strptime(row[0], '%m/%d/%Y')
    open_price = float(row[1])  # 'open' is a builtin function
    high = float(row[2])
    low = float(row[3])
    close = float(row[4])
    volume = int(row[5])
    adj_close = float(row[6])

    data.append([data, open_price, high, low, close, volume, adj_close])

# Compute the daily stock return which is percent change in price

returns_path = (r"C:\Users\mexib\Socratica Learning\google_returns.csv")  # Writes a file called google_returns.csv
file = open(returns_path, 'w')      # The 'w' open's up this file in write mode
writer = csv.writer(file)       # writer is a object that is storing the results from our next code     computations
writer.writerow(["Date","Return"])  # To write a write we use the writerow method and give a list of     values * this is the header
    # Since this list is in chronological order we can loop through the data

for i in range(len(data) - 1):
    todays_row = data[i]
    todays_date = todays_row[0]
    todays_price = todays_row[-1]
    yesterdays_row = data[i+1]
    yesterdays_price = yesterdays_row[-1]

    daily_return = (todays_price - yesterdays_price)/ yesterdays_price
    formatted_date = todays_date.datetime.strftime('%m/%d/%Y')
    writer.writerow([formatted_date, daily_return])
#for i in range(len(data) - 1):  # we stopped at the second to last row because the first row has no     previous day to compare