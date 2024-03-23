# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
for i in _c_(52180, _n_(52179, "range", lambda: range), 100, 401):
    _l_(52200)

    s = _c_(52183, _n_(52181, "str", lambda: str), _n_(52182, "i", lambda: i))
    _l_(52184)
    if _c_(52187, _n_(52185, "int", lambda: int), _n_(52186, "s", lambda: s)[0]) % 2 == 0 and _c_(52190, _n_(52188, "int", lambda: int), _n_(52189, "s", lambda: s)[1]) % 2 == 0 and (_c_(52193, _n_(52191, "int", lambda: int), _n_(52192, "s", lambda: s)[2]) % 2 == 0):
        _l_(52199)

        _c_(52197, _a_(52195, _n_(52194, "items", lambda: items), "append"), _n_(52196, "s", lambda: s))
        _l_(52198)
_c_(52205, _n_(52201, "print", lambda: print), _c_(52204, _a_(52202, ',', "join"), _n_(52203, "items", lambda: items)))
_l_(52206)