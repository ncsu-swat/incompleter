# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(82730)

except ImportError:
    pass
num = _c_(82733, _a_(82732, _n_(82731, "np", lambda: np), "arange"), 36)
_l_(82734)
_c_(82736, _n_(82735, "print", lambda: print), 'Original array:')
_l_(82737)
_c_(82740, _n_(82738, "print", lambda: print), _n_(82739, "arr1", lambda: arr1))
_l_(82741)
result = _c_(82744, _a_(82743, _n_(82742, "arr1", lambda: arr1), "sum"), axis=0)
_l_(82745)
_c_(82747, _n_(82746, "print", lambda: print), '\nSum of all columns:')
_l_(82748)
_c_(82751, _n_(82749, "print", lambda: print), _n_(82750, "result", lambda: result))
_l_(82752)