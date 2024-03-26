# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import csv
    _l_(114065)

except ImportError:
    pass
with _c_(114067, _n_(114066, "open", lambda: open), 'temp.csv', 'w', newline='') as f:
    _l_(114078)

    writer = _c_(114071, _a_(114069, _n_(114068, "csv", lambda: csv), "writer"), _n_(114070, "f", lambda: f))
    _l_(114072)
    _c_(114076, _a_(114074, _n_(114073, "writer", lambda: writer), "writerows"), _n_(114075, "data", lambda: data))
    _l_(114077)
with _c_(114080, _n_(114079, "open", lambda: open), 'temp.csv', newline='') as csvfile:
    _l_(114094)

    data = _c_(114084, _a_(114082, _n_(114081, "csv", lambda: csv), "reader"), _n_(114083, "csvfile", lambda: csvfile), delimiter=' ')
    _l_(114085)
    for row in _n_(114086, "data", lambda: data):
        _l_(114093)

        _c_(114091, _n_(114087, "print", lambda: print), _c_(114090, _a_(114088, ', ', "join"), _n_(114089, "row", lambda: row)))
        _l_(114092)