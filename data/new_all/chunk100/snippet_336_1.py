# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(33436)

except ImportError:
    pass
x = _c_(33439, _a_(33438, _n_(33437, "np", lambda: np), "ones"), (3, 3))
_l_(33440)
_c_(33442, _n_(33441, "print", lambda: print), 'Checkerboard pattern:')
_l_(33443)
_n_(33444, "x", lambda: x)[1::2, ::2] = 1
_l_(33445)
_n_(33446, "x", lambda: x)[::2, 1::2] = 1
_l_(33447)
_c_(33450, _n_(33448, "print", lambda: print), _n_(33449, "x", lambda: x))
_l_(33451)