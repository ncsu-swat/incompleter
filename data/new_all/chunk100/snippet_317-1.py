# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import defaultdict
    _l_(110374)

except ImportError:
    pass

def test(*dicts):
    _l_(110394)

    result = _c_(110377, _n_(110375, "defaultdict", lambda: defaultdict), _n_(110376, "list", lambda: list))
    _l_(110378)
    for el in _n_(110379, "dicts", lambda: dicts):
        _l_(110389)

        for key in _n_(110380, "el", lambda: el):
            _l_(110388)

            _c_(110386, _a_(110383, _n_(110381, "result", lambda: result)[_n_(110382, "key", lambda: key)], "append"), _n_(110384, "el", lambda: el)[_n_(110385, "key", lambda: key)])
            _l_(110387)
    aux = _c_(110392, _n_(110390, "dict", lambda: dict), _n_(110391, "result", lambda: result))
    _l_(110393)
    return aux
d1 = {'w': 50, 'x': 100, 'y': 'Green', 'z': 400}
_l_(110395)
_c_(110397, _n_(110396, "print", lambda: print), 'Original dictionaries:')
_l_(110398)
_c_(110401, _n_(110399, "print", lambda: print), _n_(110400, "d1", lambda: d1))
_l_(110402)
_c_(110405, _n_(110403, "print", lambda: print), _n_(110404, "d2", lambda: d2))
_l_(110406)
_c_(110408, _n_(110407, "print", lambda: print), '\nCombined dictionaries, creating a list of values for each key:')
_l_(110409)
_c_(110415, _n_(110410, "print", lambda: print), _c_(110414, _n_(110411, "test", lambda: test), _n_(110412, "d1", lambda: d1), _n_(110413, "d2", lambda: d2)))
_l_(110416)