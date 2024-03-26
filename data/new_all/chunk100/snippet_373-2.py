# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(113036)

except ImportError:
    pass
_c_(113038, _n_(113037, "print", lambda: print), 'Original array: ')
_l_(113039)
_c_(113042, _n_(113040, "print", lambda: print), _n_(113041, "x", lambda: x))
_l_(113043)
_c_(113045, _n_(113044, "print", lambda: print), '\n2^p for all the elements of the said array:')
_l_(113046)
r1 = _c_(113050, _a_(113048, _n_(113047, "np", lambda: np), "exp2"), _n_(113049, "x", lambda: x))
_l_(113051)
r2 = 2 ** _n_(113052, "x", lambda: x)
_l_(113053)
assert _c_(113058, _a_(113055, _n_(113054, "np", lambda: np), "allclose"), _n_(113056, "r1", lambda: r1), _n_(113057, "r2", lambda: r2))
_l_(113059)
_c_(113062, _n_(113060, "print", lambda: print), _n_(113061, "r1", lambda: r1))
_l_(113063)