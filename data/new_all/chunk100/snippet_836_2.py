# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import csv
    _l_(83324)

except ImportError:
    pass
_c_(83326, _n_(83325, "print", lambda: print), 'Write dictionaries to a CSV file:')
_l_(83327)
writer = _c_(83331, _a_(83329, _n_(83328, "csv", lambda: csv), "DictWriter"), _n_(83330, "fw", lambda: fw), fieldnames=['Name', 'Class'])
_l_(83332)
_c_(83335, _a_(83334, _n_(83333, "writer", lambda: writer), "writeheader"))
_l_(83336)
_c_(83339, _a_(83338, _n_(83337, "writer", lambda: writer), "writerow"), {'Name': 'Jasmine Barrett', 'Class': 'V'})
_l_(83340)
_c_(83343, _a_(83342, _n_(83341, "writer", lambda: writer), "writerow"), {'Name': 'Garry Watson', 'Class': 'V'})
_l_(83344)
_c_(83347, _a_(83346, _n_(83345, "writer", lambda: writer), "writerow"), {'Name': 'Courtney Caldwell', 'Class': 'VI'})
_l_(83348)
_c_(83351, _a_(83350, _n_(83349, "fw", lambda: fw), "close"))
_l_(83352)
fr = _c_(83354, _n_(83353, "open", lambda: open), 'test.csv', 'r')
_l_(83355)
csv = _c_(83359, _a_(83357, _n_(83356, "csv", lambda: csv), "reader"), _n_(83358, "fr", lambda: fr), delimiter=',')
_l_(83360)
for row in _n_(83361, "csv", lambda: csv):
    _l_(83366)

    _c_(83364, _n_(83362, "print", lambda: print), _n_(83363, "row", lambda: row))
    _l_(83365)
_c_(83369, _a_(83368, _n_(83367, "fr", lambda: fr), "close"))
_l_(83370)