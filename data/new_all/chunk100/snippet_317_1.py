# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import defaultdict
    _l_(30439)

except ImportError:
    pass

def test(*dicts):
    _l_(30459)

    result = _c_(30442, _n_(30440, "defaultdict", lambda: defaultdict), _n_(30441, "list", lambda: list))
    _l_(30443)
    for el in _n_(30444, "dicts", lambda: dicts):
        _l_(30454)

        for key in _n_(30445, "el", lambda: el):
            _l_(30453)

            _c_(30451, _a_(30448, _n_(30446, "result", lambda: result)[_n_(30447, "key", lambda: key)], "append"), _n_(30449, "el", lambda: el)[_n_(30450, "key", lambda: key)])
            _l_(30452)
    aux = _c_(30457, _n_(30455, "dict", lambda: dict), _n_(30456, "result", lambda: result))
    _l_(30458)
    return aux
d2 = {'x': 300, 'y': 'Red', 'z': 600}
_l_(30460)
_c_(30462, _n_(30461, "print", lambda: print), 'Original dictionaries:')
_l_(30463)
_c_(30466, _n_(30464, "print", lambda: print), _n_(30465, "d1", lambda: d1))
_l_(30467)
_c_(30470, _n_(30468, "print", lambda: print), _n_(30469, "d2", lambda: d2))
_l_(30471)
_c_(30473, _n_(30472, "print", lambda: print), '\nCombined dictionaries, creating a list of values for each key:')
_l_(30474)
_c_(30480, _n_(30475, "print", lambda: print), _c_(30479, _n_(30476, "test", lambda: test), _n_(30477, "d1", lambda: d1), _n_(30478, "d2", lambda: d2)))
_l_(30481)