# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(36936)

except ImportError:
    pass
x = _c_(36941, _a_(36938, _n_(36937, "np", lambda: np), "array"), [1.0, 2.0, 3.0, 4.0], _a_(36940, _n_(36939, "np", lambda: np), "float32"))
_l_(36942)
_c_(36944, _n_(36943, "print", lambda: print), 'Original array: ')
_l_(36945)
_c_(36948, _n_(36946, "print", lambda: print), _n_(36947, "x", lambda: x))
_l_(36949)
_c_(36951, _n_(36950, "print", lambda: print), '\n2^p for all the elements of the said array:')
_l_(36952)
r1 = _c_(36956, _a_(36954, _n_(36953, "np", lambda: np), "exp2"), _n_(36955, "x", lambda: x))
_l_(36957)
assert _c_(36962, _a_(36959, _n_(36958, "np", lambda: np), "allclose"), _n_(36960, "r1", lambda: r1), _n_(36961, "r2", lambda: r2))
_l_(36963)
_c_(36966, _n_(36964, "print", lambda: print), _n_(36965, "r1", lambda: r1))
_l_(36967)