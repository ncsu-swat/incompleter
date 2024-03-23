# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import defaultdict
    _l_(30483)

except ImportError:
    pass

def test(*dicts):
    _l_(30503)

    result = _c_(30486, _n_(30484, "defaultdict", lambda: defaultdict), _n_(30485, "list", lambda: list))
    _l_(30487)
    for el in _n_(30488, "dicts", lambda: dicts):
        _l_(30498)

        for key in _n_(30489, "el", lambda: el):
            _l_(30497)

            _c_(30495, _a_(30492, _n_(30490, "result", lambda: result)[_n_(30491, "key", lambda: key)], "append"), _n_(30493, "el", lambda: el)[_n_(30494, "key", lambda: key)])
            _l_(30496)
    aux = _c_(30501, _n_(30499, "dict", lambda: dict), _n_(30500, "result", lambda: result))
    _l_(30502)
    return aux
d1 = {'w': 50, 'x': 100, 'y': 'Green', 'z': 400}
_l_(30504)
_c_(30506, _n_(30505, "print", lambda: print), 'Original dictionaries:')
_l_(30507)
_c_(30510, _n_(30508, "print", lambda: print), _n_(30509, "d1", lambda: d1))
_l_(30511)
_c_(30514, _n_(30512, "print", lambda: print), _n_(30513, "d2", lambda: d2))
_l_(30515)
_c_(30517, _n_(30516, "print", lambda: print), '\nCombined dictionaries, creating a list of values for each key:')
_l_(30518)
_c_(30524, _n_(30519, "print", lambda: print), _c_(30523, _n_(30520, "test", lambda: test), _n_(30521, "d1", lambda: d1), _n_(30522, "d2", lambda: d2)))
_l_(30525)