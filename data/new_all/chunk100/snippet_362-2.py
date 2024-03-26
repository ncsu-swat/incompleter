# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(112256)

except ImportError:
    pass
a = _c_(112259, _a_(112258, _n_(112257, "np", lambda: np), "array"), [[4, 6], [2, 1]])
_l_(112260)
_c_(112262, _n_(112261, "print", lambda: print), 'Original array: ')
_l_(112263)
_c_(112266, _n_(112264, "print", lambda: print), _n_(112265, "a", lambda: a))
_l_(112267)
_c_(112269, _n_(112268, "print", lambda: print), 'Sort along the first axis: ')
_l_(112270)
x = _c_(112274, _a_(112272, _n_(112271, "np", lambda: np), "sort"), _n_(112273, "a", lambda: a), axis=0)
_l_(112275)
_c_(112278, _n_(112276, "print", lambda: print), _n_(112277, "x", lambda: x))
_l_(112279)
_c_(112281, _n_(112280, "print", lambda: print), 'Sort along the last axis: ')
_l_(112282)
_c_(112285, _n_(112283, "print", lambda: print), _n_(112284, "y", lambda: y))
_l_(112286)