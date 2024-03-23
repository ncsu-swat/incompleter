# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import csv
    _l_(38703)

except ImportError:
    pass
data = [[10, 'a1', 1], [12, 'a2', 3], [14, 'a3', 5], [16, 'a4', 7], [18, 'a5', 9]]
_l_(38704)
with _c_(38706, _n_(38705, "open", lambda: open), 'temp.csv', 'w', newline='') as f:
    _l_(38717)

    writer = _c_(38710, _a_(38708, _n_(38707, "csv", lambda: csv), "writer"), _n_(38709, "f", lambda: f))
    _l_(38711)
    _c_(38715, _a_(38713, _n_(38712, "writer", lambda: writer), "writerows"), _n_(38714, "data", lambda: data))
    _l_(38716)
with _c_(38719, _n_(38718, "open", lambda: open), 'temp.csv', newline='') as csvfile:
    _l_(38728)

    for row in _n_(38720, "data", lambda: data):
        _l_(38727)

        _c_(38725, _n_(38721, "print", lambda: print), _c_(38724, _a_(38722, ', ', "join"), _n_(38723, "row", lambda: row)))
        _l_(38726)