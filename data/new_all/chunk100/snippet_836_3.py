# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import csv
    _l_(83372)

except ImportError:
    pass
_c_(83374, _n_(83373, "print", lambda: print), 'Write dictionaries to a CSV file:')
_l_(83375)
fw = _c_(83377, _n_(83376, "open", lambda: open), 'test.csv', 'w', newline='')
_l_(83378)
_c_(83381, _a_(83380, _n_(83379, "writer", lambda: writer), "writeheader"))
_l_(83382)
_c_(83385, _a_(83384, _n_(83383, "writer", lambda: writer), "writerow"), {'Name': 'Jasmine Barrett', 'Class': 'V'})
_l_(83386)
_c_(83389, _a_(83388, _n_(83387, "writer", lambda: writer), "writerow"), {'Name': 'Garry Watson', 'Class': 'V'})
_l_(83390)
_c_(83393, _a_(83392, _n_(83391, "writer", lambda: writer), "writerow"), {'Name': 'Courtney Caldwell', 'Class': 'VI'})
_l_(83394)
_c_(83397, _a_(83396, _n_(83395, "fw", lambda: fw), "close"))
_l_(83398)
fr = _c_(83400, _n_(83399, "open", lambda: open), 'test.csv', 'r')
_l_(83401)
csv = _c_(83405, _a_(83403, _n_(83402, "csv", lambda: csv), "reader"), _n_(83404, "fr", lambda: fr), delimiter=',')
_l_(83406)
for row in _n_(83407, "csv", lambda: csv):
    _l_(83412)

    _c_(83410, _n_(83408, "print", lambda: print), _n_(83409, "row", lambda: row))
    _l_(83411)
_c_(83415, _a_(83414, _n_(83413, "fr", lambda: fr), "close"))
_l_(83416)