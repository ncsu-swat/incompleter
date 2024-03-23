# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(58877)

except ImportError:
    pass
_c_(58879, _n_(58878, "print", lambda: print), 'First array:')
_l_(58880)
_c_(58883, _n_(58881, "print", lambda: print), _n_(58882, "x", lambda: x))
_l_(58884)
y = _c_(58887, _a_(58886, _n_(58885, "np", lambda: np), "array"), [5 + 6j, 7 + 8j])
_l_(58888)
_c_(58890, _n_(58889, "print", lambda: print), 'Second array:')
_l_(58891)
_c_(58894, _n_(58892, "print", lambda: print), _n_(58893, "y", lambda: y))
_l_(58895)
z = _c_(58900, _a_(58897, _n_(58896, "np", lambda: np), "vdot"), _n_(58898, "x", lambda: x), _n_(58899, "y", lambda: y))
_l_(58901)
_c_(58903, _n_(58902, "print", lambda: print), 'Product of above two arrays:')
_l_(58904)
_c_(58907, _n_(58905, "print", lambda: print), _n_(58906, "z", lambda: z))
_l_(58908)