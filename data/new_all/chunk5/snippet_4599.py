# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54635859/csv-writerow-raising-an-attributeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import csv
    _l_(697473)

except ImportError:
    pass

class File:
    _l_(697500)

    def __init__(self, f):
        _l_(697477)

        _n_(697474, "self", lambda: self).f = _n_(697475, "f", lambda: f)
        _l_(697476)

    def __add__(self, other):
        _l_(697499)

        with _c_(697481, _n_(697478, "open", lambda: open), _a_(697480, _n_(697479, "self", lambda: self), "f"), mode='a') as f:
            _l_(697498)

            writer = _c_(697485, _a_(697483, _n_(697482, "csv", lambda: csv), "writer"), _n_(697484, "f", lambda: f), delimiter=',', quotechar='"')
            _l_(697486)
            _c_(697492, _a_(697488, _n_(697487, "f", lambda: f), "writerow"), _c_(697491, _n_(697489, "str", lambda: str), _n_(697490, "other", lambda: other)))
            _l_(697493)
            aux = _c_(697496, _a_(697495, _n_(697494, "self", lambda: self), "__str__"))
            _l_(697497)
            return aux

o = _c_(697502, _n_(697501, "File", lambda: File), 'file.csv')
_l_(697503)
s = _n_(697504, "o", lambda: o) + 2
_l_(697505)