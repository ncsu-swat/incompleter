# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(64772)

except ImportError:
    pass
array1 = _c_(64775, _a_(64774, _n_(64773, "np", lambda: np), "array"), [0, 10, 20, 40, 60, 80])
_l_(64776)
_c_(64779, _n_(64777, "print", lambda: print), 'Array1: ', _n_(64778, "array1", lambda: array1))
_l_(64780)
_c_(64783, _n_(64781, "print", lambda: print), 'Array2: ', _n_(64782, "array2", lambda: array2))
_l_(64784)
_c_(64786, _n_(64785, "print", lambda: print), 'Unique values in array1 that are not in array2:')
_l_(64787)
_c_(64794, _n_(64788, "print", lambda: print), _c_(64793, _a_(64790, _n_(64789, "np", lambda: np), "setdiff1d"), _n_(64791, "array1", lambda: array1), _n_(64792, "array2", lambda: array2)))
_l_(64795)