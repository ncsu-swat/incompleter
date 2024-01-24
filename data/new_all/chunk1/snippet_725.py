# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/40535615/python-typeerror-with-for-logic-iterating-data-values
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import json
    _l_(399565)

except ImportError:
    pass
try:
    import csv
    _l_(399567)

except ImportError:
    pass

with _c_(399569, _n_(399568, "open", lambda: open), 'C:\\folder\\dev\\Tags.txt',"r") as file:
    _l_(399575)

    data = _c_(399573, _a_(399571, _n_(399570, "json", lambda: json), "load"), _n_(399572, "file", lambda: file))
    _l_(399574)

with _c_(399577, _n_(399576, "open", lambda: open), 'C:\\folder\\dev\\Tags.csv',"w",newline='') as file:
    _l_(399599)


    csv_file = _c_(399581, _a_(399579, _n_(399578, "csv", lambda: csv), "writer"), _n_(399580, "file", lambda: file))
    _l_(399582)
    for dev in _n_(399583, "data", lambda: data)["devs"]:
        _l_(399598)

        for tag in _n_(399584, "dev", lambda: dev)["tags"]:
            _l_(399597)

            _c_(399595, _a_(399586, _n_(399585, "csv_file", lambda: csv_file), "writerow"), [_n_(399587, "tag", lambda: tag)['id'], _n_(399588, "tag", lambda: tag)['name'], _n_(399589, "tag", lambda: tag)['dataType'], _n_(399590, "tag", lambda: tag)['description'], _n_(399591, "tag", lambda: tag)['alarm'], _n_(399592, "tag", lambda: tag)['value'], _n_(399593, "tag", lambda: tag)['quality'], _n_(399594, "tag", lambda: tag)['DevTagId']])
            _l_(399596)