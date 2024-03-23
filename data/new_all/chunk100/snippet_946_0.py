# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import defaultdict
    _l_(95034)

except ImportError:
    pass

def frequencies(lst):
    _l_(95044)

    for val in _n_(95035, "lst", lambda: lst):
        _l_(95039)

        _n_(95036, "freq", lambda: freq)[_n_(95037, "val", lambda: val)] += 1
        _l_(95038)
    aux = _c_(95042, _n_(95040, "dict", lambda: dict), _n_(95041, "freq", lambda: freq))
    _l_(95043)
    return aux
_c_(95048, _n_(95045, "print", lambda: print), _c_(95047, _n_(95046, "frequencies", lambda: frequencies), ['a', 'b', 'f', 'a', 'c', 'e', 'a', 'a', 'b', 'e', 'f']))
_l_(95049)
_c_(95053, _n_(95050, "print", lambda: print), _c_(95052, _n_(95051, "frequencies", lambda: frequencies), [3, 4, 7, 5, 9, 3, 4, 5, 0, 3, 2, 3]))
_l_(95054)