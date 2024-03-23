# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(21395)

except ImportError:
    pass
np_array = _c_(21400, _a_(21399, _c_(21398, _a_(21397, _n_(21396, "np", lambda: np), "arange"), 3 * 4 * 5), "reshape"), 3, 4, 5)
_l_(21401)
_c_(21403, _n_(21402, "print", lambda: print), 'Original Numpy array:')
_l_(21404)
_c_(21407, _n_(21405, "print", lambda: print), _n_(21406, "np_array", lambda: np_array))
_l_(21408)
_c_(21413, _n_(21409, "print", lambda: print), 'Type: ', _c_(21412, _n_(21410, "type", lambda: type), _n_(21411, "np_array", lambda: np_array)))
_l_(21414)
_c_(21416, _n_(21415, "print", lambda: print), '\n2D diagonals: ')
_l_(21417)
_c_(21420, _n_(21418, "print", lambda: print), _n_(21419, "result", lambda: result))
_l_(21421)
_c_(21426, _n_(21422, "print", lambda: print), 'Type: ', _c_(21425, _n_(21423, "type", lambda: type), _n_(21424, "result", lambda: result)))
_l_(21427)