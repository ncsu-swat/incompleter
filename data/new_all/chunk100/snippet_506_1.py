# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from itertools import product
    _l_(52377)

except ImportError:
    pass

def all_repeat(str1, rno):
    _l_(52394)

    chars = _c_(52380, _n_(52378, "list", lambda: list), _n_(52379, "str1", lambda: str1))
    _l_(52381)
    for c in _c_(52385, _n_(52382, "product", lambda: product), _n_(52383, "chars", lambda: chars), repeat=_n_(52384, "rno", lambda: rno)):
        _l_(52391)

        _c_(52389, _a_(52387, _n_(52386, "results", lambda: results), "append"), _n_(52388, "c", lambda: c))
        _l_(52390)
    aux = _n_(52392, "results", lambda: results)
    _l_(52393)
    return aux
_c_(52398, _n_(52395, "print", lambda: print), _c_(52397, _n_(52396, "all_repeat", lambda: all_repeat), 'xyz', 3))
_l_(52399)
_c_(52403, _n_(52400, "print", lambda: print), _c_(52402, _n_(52401, "all_repeat", lambda: all_repeat), 'xyz', 2))
_l_(52404)
_c_(52408, _n_(52405, "print", lambda: print), _c_(52407, _n_(52406, "all_repeat", lambda: all_repeat), 'abcd', 4))
_l_(52409)