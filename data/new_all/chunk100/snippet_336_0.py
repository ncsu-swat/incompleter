# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(33418)

except ImportError:
    pass
_c_(33420, _n_(33419, "print", lambda: print), 'Checkerboard pattern:')
_l_(33421)
x = _c_(33425, _a_(33423, _n_(33422, "np", lambda: np), "zeros"), (8, 8), dtype=_n_(33424, "int", lambda: int))
_l_(33426)
_n_(33427, "x", lambda: x)[1::2, ::2] = 1
_l_(33428)
_n_(33429, "x", lambda: x)[::2, 1::2] = 1
_l_(33430)
_c_(33433, _n_(33431, "print", lambda: print), _n_(33432, "x", lambda: x))
_l_(33434)