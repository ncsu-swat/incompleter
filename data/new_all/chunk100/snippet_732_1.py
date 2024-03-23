# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(73927)

except ImportError:
    pass
_c_(73930, _n_(73928, "print", lambda: print), 'Array1: ', _n_(73929, "array1", lambda: array1))
_l_(73931)
array2 = [10, 30, 40]
_l_(73932)
_c_(73935, _n_(73933, "print", lambda: print), 'Array2: ', _n_(73934, "array2", lambda: array2))
_l_(73936)
_c_(73938, _n_(73937, "print", lambda: print), 'Common values between two arrays:')
_l_(73939)
_c_(73946, _n_(73940, "print", lambda: print), _c_(73945, _a_(73942, _n_(73941, "np", lambda: np), "intersect1d"), _n_(73943, "array1", lambda: array1), _n_(73944, "array2", lambda: array2)))
_l_(73947)