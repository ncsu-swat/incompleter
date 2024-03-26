# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(121028)

except ImportError:
    pass
x = _c_(121031, _a_(121030, _n_(121029, "np", lambda: np), "array"), [1.0, 2.0, 0.2, 0.3])
_l_(121032)
_c_(121034, _n_(121033, "print", lambda: print), 'Original array: ')
_l_(121035)
_c_(121038, _n_(121036, "print", lambda: print), _n_(121037, "x", lambda: x))
_l_(121039)
r2 = 1 / _n_(121040, "x", lambda: x)
_l_(121041)
assert _c_(121046, _a_(121043, _n_(121042, "np", lambda: np), "array_equal"), _n_(121044, "r1", lambda: r1), _n_(121045, "r2", lambda: r2))
_l_(121047)
_c_(121049, _n_(121048, "print", lambda: print), 'Reciprocal for all elements of the said array:')
_l_(121050)
_c_(121053, _n_(121051, "print", lambda: print), _n_(121052, "r1", lambda: r1))
_l_(121054)