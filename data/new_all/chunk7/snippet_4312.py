# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59900756/attributeerror-list-object-has-no-attribute-strftime-python-3-csv-socrati
##################################      C.omma, S.eperated,V.alue       ################################################

# https:// ten years of googles stock prices to practise manipulating data.

#   Most small amounts of data are stored in a spread sheet and larger amounts of data are stored in databases.
#   However CSV's have a place. They are easy, no drivers or api's are needed.

#  Header - first entry of data in the list
#   Data - all the rest of the data
#    - Each row data(like a record in a data base) is seperated by comma's and everything is a string.
#    - Two commas in a row ',,' means there is a missing piece of data.
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import time
    _l_(654976)

except ImportError:
    pass
try:
    import csv
    _l_(654978)

except ImportError:
    pass
try:
    from datetime import datetime
    _l_(654980)

except ImportError:
    pass



path = (r"C:\Users\mexib\Socratica Learning\Google Stock Market Data - google_stock_data.csv.csv")
_l_(654981)
file = _c_(654984, _n_(654982, "open", lambda: open), _n_(654983, "path", lambda: path), newline='')
_l_(654985)
#                          ^ adding empty brackets makes this keyword arg(kwarg) universal for different pc's
reader = _c_(654989, _a_(654987, _n_(654986, "csv", lambda: csv), "reader"), _n_(654988, "file", lambda: file))   # Using the reader function here parse the data
_l_(654990)   # Using the reader function here parse the data

header = _c_(654993, _n_(654991, "next", lambda: next), _n_(654992, "reader", lambda: reader))       # The first line is the header so we use next fucntion to get to the data.
_l_(654994)       # The first line is the header so we use next fucntion to get to the data.

#   at this point the list has been parsed but each element of this list is still a string.

data = []
_l_(654995)
for row in _n_(654996, "reader", lambda: reader):
    _l_(655037)

    # row = [Date, Open, High, Low, CLose, Volume, Adj. Close]
    date = _c_(655000, _a_(654998, _n_(654997, "datetime", lambda: datetime), "strptime"), _n_(654999, "row", lambda: row)[0], '%m/%d/%Y')
    _l_(655001)
    open_price = _c_(655004, _n_(655002, "float", lambda: float), _n_(655003, "row", lambda: row)[1])  # 'open' is a builtin function
    _l_(655005)  # 'open' is a builtin function
    high = _c_(655008, _n_(655006, "float", lambda: float), _n_(655007, "row", lambda: row)[2])
    _l_(655009)
    low = _c_(655012, _n_(655010, "float", lambda: float), _n_(655011, "row", lambda: row)[3])
    _l_(655013)
    close = _c_(655016, _n_(655014, "float", lambda: float), _n_(655015, "row", lambda: row)[4])
    _l_(655017)
    volume = _c_(655020, _n_(655018, "int", lambda: int), _n_(655019, "row", lambda: row)[5])
    _l_(655021)
    adj_close = _c_(655024, _n_(655022, "float", lambda: float), _n_(655023, "row", lambda: row)[6])
    _l_(655025)

    _c_(655035, _a_(655027, _n_(655026, "data", lambda: data), "append"), [_n_(655028, "data", lambda: data), _n_(655029, "open_price", lambda: open_price), _n_(655030, "high", lambda: high), _n_(655031, "low", lambda: low), _n_(655032, "close", lambda: close), _n_(655033, "volume", lambda: volume), _n_(655034, "adj_close", lambda: adj_close)])
    _l_(655036)

# Compute the daily stock return which is percent change in price

returns_path = (r"C:\Users\mexib\Socratica Learning\google_returns.csv")  # Writes a file called google_returns.csv
_l_(655038)  # Writes a file called google_returns.csv
file = _c_(655041, _n_(655039, "open", lambda: open), _n_(655040, "returns_path", lambda: returns_path), 'w')      # The 'w' open's up this file in write mode
_l_(655042)      # The 'w' open's up this file in write mode
writer = _c_(655046, _a_(655044, _n_(655043, "csv", lambda: csv), "writer"), _n_(655045, "file", lambda: file))       # writer is a object that is storing the results from our next code     computations
_l_(655047)       # writer is a object that is storing the results from our next code     computations
_c_(655050, _a_(655049, _n_(655048, "writer", lambda: writer), "writerow"), ["Date","Return"])  # To write a write we use the writerow method and give a list of     values * this is the header
_l_(655051)  # To write a write we use the writerow method and give a list of     values * this is the header
    # Since this list is in chronological order we can loop through the data

for i in _c_(655056, _n_(655052, "range", lambda: range), _c_(655055, _n_(655053, "len", lambda: len), _n_(655054, "data", lambda: data)) - 1):
    _l_(655084)

    todays_row = _n_(655057, "data", lambda: data)[_n_(655058, "i", lambda: i)]
    _l_(655059)
    todays_date = _n_(655060, "todays_row", lambda: todays_row)[0]
    _l_(655061)
    todays_price = _n_(655062, "todays_row", lambda: todays_row)[-1]
    _l_(655063)
    yesterdays_row = _n_(655064, "data", lambda: data)[_n_(655065, "i", lambda: i)+1]
    _l_(655066)
    yesterdays_price = _n_(655067, "yesterdays_row", lambda: yesterdays_row)[-1]
    _l_(655068)

    daily_return = (_n_(655069, "todays_price", lambda: todays_price) - _n_(655070, "yesterdays_price", lambda: yesterdays_price))/ _n_(655071, "yesterdays_price", lambda: yesterdays_price)
    _l_(655072)
    formatted_date = _c_(655076, _a_(655075, _a_(655074, _n_(655073, "todays_date", lambda: todays_date), "datetime"), "strftime"), '%m/%d/%Y')
    _l_(655077)
    _c_(655082, _a_(655079, _n_(655078, "writer", lambda: writer), "writerow"), [_n_(655080, "formatted_date", lambda: formatted_date), _n_(655081, "daily_return", lambda: daily_return)])
    _l_(655083)
#for i in range(len(data) - 1):  # we stopped at the second to last row because the first row has no     previous day to compare