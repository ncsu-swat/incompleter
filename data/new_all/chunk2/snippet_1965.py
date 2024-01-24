# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74849766/typeerror-cannot-unpack-non-iterable-int-object-with-filter-function
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
liste = [(3,4,5),(6,8,10),(3,10,7)]
_l_(467295)

def ucgen_mi(s):
    _l_(467312)

    for g in _n_(467296, "s", lambda: s):
        _l_(467311)

        a, b, c = _n_(467297, "g", lambda: g)
        _l_(467298)
        if (_n_(467299, "a", lambda: a) + _n_(467300, "b", lambda: b) > _n_(467301, "c", lambda: c) and _n_(467302, "a", lambda: a) + _n_(467303, "c", lambda: c) > _n_(467304, "b", lambda: b) and _n_(467305, "c", lambda: c) + _n_(467306, "b", lambda: b) > _n_(467307, "a", lambda: a)):
            _l_(467310)

            aux = True
            _l_(467308)
            return aux
        else:
            aux = False
            _l_(467309)
            return aux


_c_(467320, _n_(467313, "print", lambda: print), _c_(467319, _n_(467314, "list", lambda: list), _c_(467318, _n_(467315, "filter", lambda: filter), _n_(467316, "ucgen_mi", lambda: ucgen_mi), _n_(467317, "liste", lambda: liste))))
_l_(467321)