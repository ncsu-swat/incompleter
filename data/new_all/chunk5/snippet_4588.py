# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54948165/working-with-json-api-data-and-getting-typeerror-list-indices-must-be-integers
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import requests
    _l_(707199)

except ImportError:
    pass
try:
    import csv
    _l_(707201)

except ImportError:
    pass
try:
    import re
    _l_(707203)

except ImportError:
    pass

outputfile = 'file.csv'
_l_(707204)
outfile = _c_(707207, _n_(707205, "open", lambda: open), _n_(707206, "outputfile", lambda: outputfile), mode='w', newline='')
_l_(707208)

master_key = ['name', 'address', 'phoneNumber']
_l_(707209)

writer = _c_(707214, _a_(707211, _n_(707210, "csv", lambda: csv), "DictWriter"), _n_(707212, "outfile", lambda: outfile), _n_(707213, "master_key", lambda: master_key), delimiter=",")
_l_(707215)
_c_(707218, _a_(707217, _n_(707216, "writer", lambda: writer), "writeheader"))
_l_(707219)

with _c_(707221, _n_(707220, "open", lambda: open), 'idfile.csv') as csv_file:
    _l_(707254)

    open_file = _c_(707225, _a_(707223, _n_(707222, "csv", lambda: csv), "reader"), _n_(707224, "csv_file", lambda: csv_file), delimiter=',')
    _l_(707226)
    for row in _n_(707227, "open_file", lambda: open_file):
        _l_(707253)

        for id in _n_(707228, "row", lambda: row):
            _l_(707252)

            url = "https://schoolsite/studentIds/"
            _l_(707229)
            response = _c_(707233, _a_(707231, _n_(707230, "requests", lambda: requests), "get"), _n_(707232, "url", lambda: url))
            _l_(707234)
            data = _c_(707237, _a_(707236, _n_(707235, "response", lambda: response), "json"))
            _l_(707238)
            _c_(707241, _n_(707239, "print", lambda: print), _n_(707240, "data", lambda: data))
            _l_(707242)
            dict = {'name': _n_(707243, "data", lambda: data)['input']['name'], 'address' : _n_(707244, "data", lambda: data)['input']['address'], 'phoneNumber' : _n_(707245, "data", lambda: data)['input']['phoneNumber']}
            _l_(707246)
            _c_(707250, _a_(707248, _n_(707247, "writer", lambda: writer), "writerow"), _n_(707249, "dict", lambda: dict))
            _l_(707251)