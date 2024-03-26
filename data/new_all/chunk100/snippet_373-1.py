# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(113006)

except ImportError:
    pass
x = _c_(113011, _a_(113008, _n_(113007, "np", lambda: np), "array"), [1.0, 2.0, 3.0, 4.0], _a_(113010, _n_(113009, "np", lambda: np), "float32"))
_l_(113012)
_c_(113014, _n_(113013, "print", lambda: print), 'Original array: ')
_l_(113015)
_c_(113018, _n_(113016, "print", lambda: print), _n_(113017, "x", lambda: x))
_l_(113019)
_c_(113021, _n_(113020, "print", lambda: print), '\n2^p for all the elements of the said array:')
_l_(113022)
r2 = 2 ** _n_(113023, "x", lambda: x)
_l_(113024)
assert _c_(113029, _a_(113026, _n_(113025, "np", lambda: np), "allclose"), _n_(113027, "r1", lambda: r1), _n_(113028, "r2", lambda: r2))
_l_(113030)
_c_(113033, _n_(113031, "print", lambda: print), _n_(113032, "r1", lambda: r1))
_l_(113034)