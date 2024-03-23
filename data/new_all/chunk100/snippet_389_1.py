# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import csv
    _l_(38730)

except ImportError:
    pass
data = [[10, 'a1', 1], [12, 'a2', 3], [14, 'a3', 5], [16, 'a4', 7], [18, 'a5', 9]]
_l_(38731)
with _c_(38733, _n_(38732, "open", lambda: open), 'temp.csv', 'w', newline='') as f:
    _l_(38739)

    _c_(38737, _a_(38735, _n_(38734, "writer", lambda: writer), "writerows"), _n_(38736, "data", lambda: data))
    _l_(38738)
with _c_(38741, _n_(38740, "open", lambda: open), 'temp.csv', newline='') as csvfile:
    _l_(38755)

    data = _c_(38745, _a_(38743, _n_(38742, "csv", lambda: csv), "reader"), _n_(38744, "csvfile", lambda: csvfile), delimiter=' ')
    _l_(38746)
    for row in _n_(38747, "data", lambda: data):
        _l_(38754)

        _c_(38752, _n_(38748, "print", lambda: print), _c_(38751, _a_(38749, ', ', "join"), _n_(38750, "row", lambda: row)))
        _l_(38753)