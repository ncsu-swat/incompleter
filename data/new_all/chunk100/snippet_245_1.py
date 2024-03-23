# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(19408)

except ImportError:
    pass
_c_(19410, _n_(19409, "print", lambda: print), 'Original array:')
_l_(19411)
_c_(19414, _n_(19412, "print", lambda: print), _n_(19413, "x", lambda: x))
_l_(19415)
_c_(19420, _a_(19418, _a_(19417, _n_(19416, "np", lambda: np), "random"), "shuffle"), _n_(19419, "x", lambda: x))
_l_(19421)
n = 1
_l_(19422)
_c_(19430, _n_(19423, "print", lambda: print), _n_(19424, "x", lambda: x)[_c_(19428, _a_(19426, _n_(19425, "np", lambda: np), "argsort"), _n_(19427, "x", lambda: x))[-_n_(19429, "n", lambda: n):]])
_l_(19431)