# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(36907)

except ImportError:
    pass
_c_(36909, _n_(36908, "print", lambda: print), 'Original array: ')
_l_(36910)
_c_(36913, _n_(36911, "print", lambda: print), _n_(36912, "x", lambda: x))
_l_(36914)
_c_(36916, _n_(36915, "print", lambda: print), '\n2^p for all the elements of the said array:')
_l_(36917)
r1 = _c_(36921, _a_(36919, _n_(36918, "np", lambda: np), "exp2"), _n_(36920, "x", lambda: x))
_l_(36922)
r2 = 2 ** _n_(36923, "x", lambda: x)
_l_(36924)
assert _c_(36929, _a_(36926, _n_(36925, "np", lambda: np), "allclose"), _n_(36927, "r1", lambda: r1), _n_(36928, "r2", lambda: r2))
_l_(36930)
_c_(36933, _n_(36931, "print", lambda: print), _n_(36932, "r1", lambda: r1))
_l_(36934)