# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import defaultdict
    _l_(30398)

except ImportError:
    pass

def test(*dicts):
    _l_(30414)

    for el in _n_(30399, "dicts", lambda: dicts):
        _l_(30409)

        for key in _n_(30400, "el", lambda: el):
            _l_(30408)

            _c_(30406, _a_(30403, _n_(30401, "result", lambda: result)[_n_(30402, "key", lambda: key)], "append"), _n_(30404, "el", lambda: el)[_n_(30405, "key", lambda: key)])
            _l_(30407)
    aux = _c_(30412, _n_(30410, "dict", lambda: dict), _n_(30411, "result", lambda: result))
    _l_(30413)
    return aux
d1 = {'w': 50, 'x': 100, 'y': 'Green', 'z': 400}
_l_(30415)
d2 = {'x': 300, 'y': 'Red', 'z': 600}
_l_(30416)
_c_(30418, _n_(30417, "print", lambda: print), 'Original dictionaries:')
_l_(30419)
_c_(30422, _n_(30420, "print", lambda: print), _n_(30421, "d1", lambda: d1))
_l_(30423)
_c_(30426, _n_(30424, "print", lambda: print), _n_(30425, "d2", lambda: d2))
_l_(30427)
_c_(30429, _n_(30428, "print", lambda: print), '\nCombined dictionaries, creating a list of values for each key:')
_l_(30430)
_c_(30436, _n_(30431, "print", lambda: print), _c_(30435, _n_(30432, "test", lambda: test), _n_(30433, "d1", lambda: d1), _n_(30434, "d2", lambda: d2)))
_l_(30437)