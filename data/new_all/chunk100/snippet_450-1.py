# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(116784)

except ImportError:
    pass
array1 = _c_(116787, _a_(116786, _n_(116785, "np", lambda: np), "array"), [0, 10, 20, 40, 60])
_l_(116788)
_c_(116791, _n_(116789, "print", lambda: print), 'Array1: ', _n_(116790, "array1", lambda: array1))
_l_(116792)
_c_(116795, _n_(116793, "print", lambda: print), 'Array2: ', _n_(116794, "array2", lambda: array2))
_l_(116796)
_c_(116798, _n_(116797, "print", lambda: print), 'Compare each element of array1 and array2')
_l_(116799)
_c_(116806, _n_(116800, "print", lambda: print), _c_(116805, _a_(116802, _n_(116801, "np", lambda: np), "in1d"), _n_(116803, "array1", lambda: array1), _n_(116804, "array2", lambda: array2)))
_l_(116807)