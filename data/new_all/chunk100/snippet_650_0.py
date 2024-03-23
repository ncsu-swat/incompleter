# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import csv
    _l_(67275)

except ImportError:
    pass
_c_(67280, _a_(67277, _n_(67276, "csv", lambda: csv), "register_dialect"), 'csv_dialect', delimiter='|', skipinitialspace=True, quoting=_a_(67279, _n_(67278, "csv", lambda: csv), "QUOTE_ALL"))
_l_(67281)
with _c_(67283, _n_(67282, "open", lambda: open), 'temp.csv', 'r') as csvfile:
    _l_(67290)

    for row in _n_(67284, "reader", lambda: reader):
        _l_(67289)

        _c_(67287, _n_(67285, "print", lambda: print), _n_(67286, "row", lambda: row))
        _l_(67288)