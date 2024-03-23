# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import csv
    _l_(38757)

except ImportError:
    pass
with _c_(38759, _n_(38758, "open", lambda: open), 'temp.csv', 'w', newline='') as f:
    _l_(38770)

    writer = _c_(38763, _a_(38761, _n_(38760, "csv", lambda: csv), "writer"), _n_(38762, "f", lambda: f))
    _l_(38764)
    _c_(38768, _a_(38766, _n_(38765, "writer", lambda: writer), "writerows"), _n_(38767, "data", lambda: data))
    _l_(38769)
with _c_(38772, _n_(38771, "open", lambda: open), 'temp.csv', newline='') as csvfile:
    _l_(38786)

    data = _c_(38776, _a_(38774, _n_(38773, "csv", lambda: csv), "reader"), _n_(38775, "csvfile", lambda: csvfile), delimiter=' ')
    _l_(38777)
    for row in _n_(38778, "data", lambda: data):
        _l_(38785)

        _c_(38783, _n_(38779, "print", lambda: print), _c_(38782, _a_(38780, ', ', "join"), _n_(38781, "row", lambda: row)))
        _l_(38784)