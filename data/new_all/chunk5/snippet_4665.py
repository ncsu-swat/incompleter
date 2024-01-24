# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53282885/python-adding-values-to-a-dictionary-typeerror-string-indices-must-be-integers
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from kafka import KafkaConsumer
    _l_(665301)

except ImportError:
    pass
try:
    import json
    _l_(665303)

except ImportError:
    pass
try:
    import csv
    _l_(665305)

except ImportError:
    pass
try:
    import sys
    _l_(665307)

except ImportError:
    pass
try:
    from datetime import datetime
    _l_(665309)

except ImportError:
    pass
try:
    import os
    _l_(665311)

except ImportError:
    pass

# connect to kafka topic
kaf = _c_(665313, _n_(665312, "KafkaConsumer", lambda: KafkaConsumer), 'students.all.events')
_l_(665314)


outputfile = 'C:\\Users\\Documents\\students_output.csv'
_l_(665315)

outfile = _c_(665318, _n_(665316, "open", lambda: open), _n_(665317, "outputfile", lambda: outputfile), mode='w', newline='')
_l_(665319)
master_key = ['id', 'name', 'lastName', 'science', 'math', 'english']
_l_(665320)

writer = _c_(665325, _a_(665322, _n_(665321, "csv", lambda: csv), "DictWriter"), _n_(665323, "outfile", lambda: outfile), _n_(665324, "master_key", lambda: master_key), delimiter="|")
_l_(665326)
_c_(665329, _a_(665328, _n_(665327, "writer", lambda: writer), "writeheader"))
_l_(665330)
'''
writer = csv.writer(outfile)
writer.writerow(['JSON_Data'])
'''
_l_(665331)

i = 1
_l_(665332)
for row in _n_(665333, "kaf", lambda: kaf):
    _l_(665376)

    if _n_(665334, "i", lambda: i) < 5000:
        _l_(665375)

        json_row = _c_(665339, _a_(665336, _n_(665335, "json", lambda: json), "loads"), _a_(665338, _n_(665337, "row", lambda: row), "value"))
        _l_(665340)
        _c_(665343, _n_(665341, "print", lambda: print), 'Row: ', _n_(665342, "i", lambda: i))
        _l_(665344)
        _c_(665347, _n_(665345, "print", lambda: print), _n_(665346, "json_row", lambda: json_row))
        _l_(665348)

        dict = {'id': _n_(665349, "json_row", lambda: json_row)['id'], 'name': _n_(665350, "json_row", lambda: json_row)['name'], 'lastName': _n_(665351, "json_row", lambda: json_row)['lastName']}
        _l_(665352)

        for value in _n_(665353, "json_row", lambda: json_row)['grades']:
            _l_(665367)

            if _n_(665354, "value", lambda: value)['science'] is not None:
                _l_(665366)

                _n_(665355, "dict", lambda: dict)['science'] = _n_(665356, "value", lambda: value)['science']
                _l_(665357)
                _n_(665358, "dict", lambda: dict)['math'] = _n_(665359, "value", lambda: value)['math']
                _l_(665360)

            elif _n_(665361, "value", lambda: value)['english'] is not None:
                _l_(665365)

                _n_(665362, "dict", lambda: dict)['english'] = _n_(665363, "value", lambda: value)['english']
                _l_(665364)

        _c_(665371, _a_(665369, _n_(665368, "writer", lambda: writer), "writerow"), _n_(665370, "dict", lambda: dict))
        _l_(665372)
        i += 1
        _l_(665373)
    else:
        break
        _l_(665374)

_c_(665379, _a_(665378, _n_(665377, "outfile", lambda: outfile), "close"))
_l_(665380)