# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53282885/python-adding-values-to-a-dictionary-typeerror-string-indices-must-be-integers
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from kafka import KafkaConsumer
    _l_(661641)

except ImportError:
    pass
try:
    import json
    _l_(661643)

except ImportError:
    pass
try:
    import csv
    _l_(661645)

except ImportError:
    pass
try:
    import sys
    _l_(661647)

except ImportError:
    pass
try:
    from datetime import datetime
    _l_(661649)

except ImportError:
    pass
try:
    import os
    _l_(661651)

except ImportError:
    pass

# connect to kafka topic
kaf = _c_(661653, _n_(661652, "KafkaConsumer", lambda: KafkaConsumer), 'students.all.events')
_l_(661654)


outputfile = 'C:\\Users\\Documents\\students_output.csv'
_l_(661655)

outfile = _c_(661658, _n_(661656, "open", lambda: open), _n_(661657, "outputfile", lambda: outputfile), mode='w', newline='')
_l_(661659)
master_key = ['id', 'name', 'lastName', 'science', 'math', 'english']
_l_(661660)

writer = _c_(661665, _a_(661662, _n_(661661, "csv", lambda: csv), "DictWriter"), _n_(661663, "outfile", lambda: outfile), _n_(661664, "master_key", lambda: master_key), delimiter="|")
_l_(661666)
_c_(661669, _a_(661668, _n_(661667, "writer", lambda: writer), "writeheader"))
_l_(661670)
'''
writer = csv.writer(outfile)
writer.writerow(['JSON_Data'])
'''
_l_(661671)

i = 1
_l_(661672)
for row in _n_(661673, "kaf", lambda: kaf):
    _l_(661716)

    if _n_(661674, "i", lambda: i) < 5000:
        _l_(661715)

        json_row = _c_(661679, _a_(661676, _n_(661675, "json", lambda: json), "loads"), _a_(661678, _n_(661677, "row", lambda: row), "value"))
        _l_(661680)
        _c_(661683, _n_(661681, "print", lambda: print), 'Row: ', _n_(661682, "i", lambda: i))
        _l_(661684)
        _c_(661687, _n_(661685, "print", lambda: print), _n_(661686, "json_row", lambda: json_row))
        _l_(661688)

        dict = {'id': _n_(661689, "json_row", lambda: json_row)['id'], 'name': _n_(661690, "json_row", lambda: json_row)['name'], 'lastName': _n_(661691, "json_row", lambda: json_row)['lastName']}
        _l_(661692)

        for value in _n_(661693, "json_row", lambda: json_row)['grades']:
            _l_(661707)

            if _n_(661694, "value", lambda: value)['science'] is not None:
                _l_(661706)

                _n_(661695, "dict", lambda: dict)['science'] = _n_(661696, "value", lambda: value)['science']
                _l_(661697)
                _n_(661698, "dict", lambda: dict)['math'] = _n_(661699, "value", lambda: value)['math']
                _l_(661700)

            elif _n_(661701, "value", lambda: value)['english'] is not None:
                _l_(661705)

                _n_(661702, "dict", lambda: dict)['english'] = _n_(661703, "value", lambda: value)['english']
                _l_(661704)

        _c_(661711, _a_(661709, _n_(661708, "writer", lambda: writer), "writerow"), _n_(661710, "dict", lambda: dict))
        _l_(661712)
        i += 1
        _l_(661713)
    else:
        break
        _l_(661714)

_c_(661719, _a_(661718, _n_(661717, "outfile", lambda: outfile), "close"))
_l_(661720)