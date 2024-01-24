# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54635859/csv-writerow-raising-an-attributeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import csv
    _l_(680279)

except ImportError:
    pass

class File:
    _l_(680306)

    def __init__(self, f):
        _l_(680283)

        _n_(680280, "self", lambda: self).f = _n_(680281, "f", lambda: f)
        _l_(680282)

    def __add__(self, other):
        _l_(680305)

        with _c_(680287, _n_(680284, "open", lambda: open), _a_(680286, _n_(680285, "self", lambda: self), "f"), mode='a') as f:
            _l_(680304)

            writer = _c_(680291, _a_(680289, _n_(680288, "csv", lambda: csv), "writer"), _n_(680290, "f", lambda: f), delimiter=',', quotechar='"')
            _l_(680292)
            _c_(680298, _a_(680294, _n_(680293, "f", lambda: f), "writerow"), _c_(680297, _n_(680295, "str", lambda: str), _n_(680296, "other", lambda: other)))
            _l_(680299)
            aux = _c_(680302, _a_(680301, _n_(680300, "self", lambda: self), "__str__"))
            _l_(680303)
            return aux

o = _c_(680308, _n_(680307, "File", lambda: File), 'file.csv')
_l_(680309)
s = _n_(680310, "o", lambda: o) + 2
_l_(680311)