# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(48172)

except ImportError:
    pass
array1 = _c_(48175, _a_(48174, _n_(48173, "np", lambda: np), "array"), [0, 10, 20, 40, 60])
_l_(48176)
_c_(48179, _n_(48177, "print", lambda: print), 'Array1: ', _n_(48178, "array1", lambda: array1))
_l_(48180)
_c_(48183, _n_(48181, "print", lambda: print), 'Array2: ', _n_(48182, "array2", lambda: array2))
_l_(48184)
_c_(48186, _n_(48185, "print", lambda: print), 'Compare each element of array1 and array2')
_l_(48187)
_c_(48194, _n_(48188, "print", lambda: print), _c_(48193, _a_(48190, _n_(48189, "np", lambda: np), "in1d"), _n_(48191, "array1", lambda: array1), _n_(48192, "array2", lambda: array2)))
_l_(48195)