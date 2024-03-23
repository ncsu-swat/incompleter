# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from itertools import product
    _l_(52346)

except ImportError:
    pass

def all_repeat(str1, rno):
    _l_(52360)

    results = []
    _l_(52347)
    for c in _c_(52351, _n_(52348, "product", lambda: product), _n_(52349, "chars", lambda: chars), repeat=_n_(52350, "rno", lambda: rno)):
        _l_(52357)

        _c_(52355, _a_(52353, _n_(52352, "results", lambda: results), "append"), _n_(52354, "c", lambda: c))
        _l_(52356)
    aux = _n_(52358, "results", lambda: results)
    _l_(52359)
    return aux
_c_(52364, _n_(52361, "print", lambda: print), _c_(52363, _n_(52362, "all_repeat", lambda: all_repeat), 'xyz', 3))
_l_(52365)
_c_(52369, _n_(52366, "print", lambda: print), _c_(52368, _n_(52367, "all_repeat", lambda: all_repeat), 'xyz', 2))
_l_(52370)
_c_(52374, _n_(52371, "print", lambda: print), _c_(52373, _n_(52372, "all_repeat", lambda: all_repeat), 'abcd', 4))
_l_(52375)