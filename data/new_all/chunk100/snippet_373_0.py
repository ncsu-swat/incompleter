# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(36877)

except ImportError:
    pass
x = _c_(36882, _a_(36879, _n_(36878, "np", lambda: np), "array"), [1.0, 2.0, 3.0, 4.0], _a_(36881, _n_(36880, "np", lambda: np), "float32"))
_l_(36883)
_c_(36885, _n_(36884, "print", lambda: print), 'Original array: ')
_l_(36886)
_c_(36889, _n_(36887, "print", lambda: print), _n_(36888, "x", lambda: x))
_l_(36890)
_c_(36892, _n_(36891, "print", lambda: print), '\n2^p for all the elements of the said array:')
_l_(36893)
r2 = 2 ** _n_(36894, "x", lambda: x)
_l_(36895)
assert _c_(36900, _a_(36897, _n_(36896, "np", lambda: np), "allclose"), _n_(36898, "r1", lambda: r1), _n_(36899, "r2", lambda: r2))
_l_(36901)
_c_(36904, _n_(36902, "print", lambda: print), _n_(36903, "r1", lambda: r1))
_l_(36905)