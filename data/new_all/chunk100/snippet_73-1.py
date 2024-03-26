# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(119958)

except ImportError:
    pass
_c_(119960, _n_(119959, "print", lambda: print), '\nOriginal arrays:')
_l_(119961)
_c_(119964, _n_(119962, "print", lambda: print), _n_(119963, "x", lambda: x))
_l_(119965)
new_array1 = _c_(119969, _a_(119967, _n_(119966, "np", lambda: np), "vsplit"), _n_(119968, "x", lambda: x), 2)
_l_(119970)
_c_(119972, _n_(119971, "print", lambda: print), '\nSplit an array into multiple sub-arrays vertically:')
_l_(119973)
_c_(119976, _n_(119974, "print", lambda: print), _n_(119975, "new_array1", lambda: new_array1))
_l_(119977)