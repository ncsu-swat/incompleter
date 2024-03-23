# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(64925)

except ImportError:
    pass
a = _c_(64928, _a_(64927, _n_(64926, "np", lambda: np), "array"), [1, 2, 3])
_l_(64929)
b = _c_(64932, _a_(64931, _n_(64930, "np", lambda: np), "array"), [0, 1, 0])
_l_(64933)
_c_(64935, _n_(64934, "print", lambda: print), 'Original 1-d arrays:')
_l_(64936)
_c_(64939, _n_(64937, "print", lambda: print), _n_(64938, "a", lambda: a))
_l_(64940)
_c_(64943, _n_(64941, "print", lambda: print), _n_(64942, "b", lambda: b))
_l_(64944)
_c_(64946, _n_(64945, "print", lambda: print), 'Einstein’s summation convention of the said arrays:')
_l_(64947)
_c_(64950, _n_(64948, "print", lambda: print), _n_(64949, "result", lambda: result))
_l_(64951)
x = _c_(64956, _a_(64955, _c_(64954, _a_(64953, _n_(64952, "np", lambda: np), "arange"), 9), "reshape"), 3, 3)
_l_(64957)
y = _c_(64962, _a_(64961, _c_(64960, _a_(64959, _n_(64958, "np", lambda: np), "arange"), 3, 12), "reshape"), 3, 3)
_l_(64963)
_c_(64965, _n_(64964, "print", lambda: print), 'Original Higher dimension:')
_l_(64966)
_c_(64969, _n_(64967, "print", lambda: print), _n_(64968, "x", lambda: x))
_l_(64970)
_c_(64973, _n_(64971, "print", lambda: print), _n_(64972, "y", lambda: y))
_l_(64974)
result = _c_(64979, _a_(64976, _n_(64975, "np", lambda: np), "einsum"), 'mk,kn', _n_(64977, "x", lambda: x), _n_(64978, "y", lambda: y))
_l_(64980)
_c_(64982, _n_(64981, "print", lambda: print), 'Einstein’s summation convention of the said arrays:')
_l_(64983)
_c_(64986, _n_(64984, "print", lambda: print), _n_(64985, "result", lambda: result))
_l_(64987)