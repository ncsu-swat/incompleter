# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(65053)

except ImportError:
    pass
b = _c_(65056, _a_(65055, _n_(65054, "np", lambda: np), "array"), [0, 1, 0])
_l_(65057)
_c_(65059, _n_(65058, "print", lambda: print), 'Original 1-d arrays:')
_l_(65060)
_c_(65063, _n_(65061, "print", lambda: print), _n_(65062, "a", lambda: a))
_l_(65064)
_c_(65067, _n_(65065, "print", lambda: print), _n_(65066, "b", lambda: b))
_l_(65068)
result = _c_(65073, _a_(65070, _n_(65069, "np", lambda: np), "einsum"), 'n,n', _n_(65071, "a", lambda: a), _n_(65072, "b", lambda: b))
_l_(65074)
_c_(65076, _n_(65075, "print", lambda: print), 'Einstein’s summation convention of the said arrays:')
_l_(65077)
_c_(65080, _n_(65078, "print", lambda: print), _n_(65079, "result", lambda: result))
_l_(65081)
x = _c_(65086, _a_(65085, _c_(65084, _a_(65083, _n_(65082, "np", lambda: np), "arange"), 9), "reshape"), 3, 3)
_l_(65087)
y = _c_(65092, _a_(65091, _c_(65090, _a_(65089, _n_(65088, "np", lambda: np), "arange"), 3, 12), "reshape"), 3, 3)
_l_(65093)
_c_(65095, _n_(65094, "print", lambda: print), 'Original Higher dimension:')
_l_(65096)
_c_(65099, _n_(65097, "print", lambda: print), _n_(65098, "x", lambda: x))
_l_(65100)
_c_(65103, _n_(65101, "print", lambda: print), _n_(65102, "y", lambda: y))
_l_(65104)
result = _c_(65109, _a_(65106, _n_(65105, "np", lambda: np), "einsum"), 'mk,kn', _n_(65107, "x", lambda: x), _n_(65108, "y", lambda: y))
_l_(65110)
_c_(65112, _n_(65111, "print", lambda: print), 'Einstein’s summation convention of the said arrays:')
_l_(65113)
_c_(65116, _n_(65114, "print", lambda: print), _n_(65115, "result", lambda: result))
_l_(65117)