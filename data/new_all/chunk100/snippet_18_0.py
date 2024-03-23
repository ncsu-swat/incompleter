# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(15181)

except ImportError:
    pass
array1 = _c_(15184, _a_(15183, _n_(15182, "np", lambda: np), "array"), [1, 7, 8, 2, 0.1, 3, 15, 2.5])
_l_(15185)
_c_(15187, _n_(15186, "print", lambda: print), 'Original arrays:')
_l_(15188)
_c_(15191, _n_(15189, "print", lambda: print), _n_(15190, "array1", lambda: array1))
_l_(15192)
k = 4
_l_(15193)
_c_(15195, _n_(15194, "print", lambda: print), '\nk smallest values:')
_l_(15196)
_c_(15201, _n_(15197, "print", lambda: print), _n_(15198, "array1", lambda: array1)[_n_(15199, "result", lambda: result)[:_n_(15200, "k", lambda: k)]])
_l_(15202)