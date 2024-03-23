# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import csv
    _l_(83230)

except ImportError:
    pass
_c_(83232, _n_(83231, "print", lambda: print), 'Write dictionaries to a CSV file:')
_l_(83233)
fw = _c_(83235, _n_(83234, "open", lambda: open), 'test.csv', 'w', newline='')
_l_(83236)
writer = _c_(83240, _a_(83238, _n_(83237, "csv", lambda: csv), "DictWriter"), _n_(83239, "fw", lambda: fw), fieldnames=['Name', 'Class'])
_l_(83241)
_c_(83244, _a_(83243, _n_(83242, "writer", lambda: writer), "writeheader"))
_l_(83245)
_c_(83248, _a_(83247, _n_(83246, "writer", lambda: writer), "writerow"), {'Name': 'Jasmine Barrett', 'Class': 'V'})
_l_(83249)
_c_(83252, _a_(83251, _n_(83250, "writer", lambda: writer), "writerow"), {'Name': 'Garry Watson', 'Class': 'V'})
_l_(83253)
_c_(83256, _a_(83255, _n_(83254, "writer", lambda: writer), "writerow"), {'Name': 'Courtney Caldwell', 'Class': 'VI'})
_l_(83257)
_c_(83260, _a_(83259, _n_(83258, "fw", lambda: fw), "close"))
_l_(83261)
csv = _c_(83265, _a_(83263, _n_(83262, "csv", lambda: csv), "reader"), _n_(83264, "fr", lambda: fr), delimiter=',')
_l_(83266)
for row in _n_(83267, "csv", lambda: csv):
    _l_(83272)

    _c_(83270, _n_(83268, "print", lambda: print), _n_(83269, "row", lambda: row))
    _l_(83271)
_c_(83275, _a_(83274, _n_(83273, "fr", lambda: fr), "close"))
_l_(83276)