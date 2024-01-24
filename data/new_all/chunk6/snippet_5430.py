# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/52974322/attributeerror-builtin-function-or-method-object-has-no-attribute-fieldnames
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import csv
    _l_(370276)

except ImportError:
    pass
try:
    from datetime import datetime
    _l_(370278)

except ImportError:
    pass
try:
    from pprint import pprint
    _l_(370280)

except ImportError:
    pass



def print_first_point(filename):
    _l_(370313)

    """
    This function prints and returns the first data point (second row) from
    a csv file that includes a header row.
    """
    # print city name for reference
    city = _c_(370285, _a_(370284, _c_(370283, _a_(370282, _n_(370281, "filename", lambda: filename), "split"), '-')[0], "split"), '/')[-1]
    _l_(370286)
    _c_(370291, _n_(370287, "print", lambda: print), _c_(370290, _a_(370288, '\nCity: {}', "format"), _n_(370289, "city", lambda: city)))
    _l_(370292)

    with _c_(370295, _n_(370293, "open", lambda: open), _n_(370294, "filename", lambda: filename), 'r') as f_in:
        _l_(370309)

        trip_reader = _c_(370299, _a_(370297, _n_(370296, "csv", lambda: csv), "DictReader"), _n_(370298, "f_in", lambda: f_in))
        _l_(370300)
        first_trip = _a_(370303, _a_(370302, _n_(370301, "csv", lambda: csv), "reader"), "fieldnames")
        _l_(370304)
        _c_(370307, _n_(370305, "pprint", lambda: pprint), _n_(370306, "first_trip", lambda: first_trip))
        _l_(370308)
    aux = (_n_(370310, "city", lambda: city), _n_(370311, "first_trip", lambda: first_trip))
    _l_(370312)
    # output city name and first trip for later testing
    return aux

# list of files for each city
data_files = ['./data/NYC-CitiBike-2016.csv',
              './data/Chicago-Divvy-2016.csv',
              './data/Washington-CapitalBikeshare-2016.csv',]
_l_(370314)

# print the first trip from each file, store in dictionary
example_trips = {}
_l_(370315)
for data_file in _n_(370316, "data_files", lambda: data_files):
    _l_(370325)

    city, first_trip = _c_(370319, _n_(370317, "print_first_point", lambda: print_first_point), _n_(370318, "data_file", lambda: data_file))
    _l_(370320)
    _n_(370321, "example_trips", lambda: example_trips)[_n_(370322, "city", lambda: city)] = _n_(370323, "first_trip", lambda: first_trip)
    _l_(370324)