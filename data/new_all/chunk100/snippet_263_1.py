# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(21429)

except ImportError:
    pass
_c_(21431, _n_(21430, "print", lambda: print), 'Original Numpy array:')
_l_(21432)
_c_(21435, _n_(21433, "print", lambda: print), _n_(21434, "np_array", lambda: np_array))
_l_(21436)
_c_(21441, _n_(21437, "print", lambda: print), 'Type: ', _c_(21440, _n_(21438, "type", lambda: type), _n_(21439, "np_array", lambda: np_array)))
_l_(21442)
result = _c_(21446, _a_(21444, _n_(21443, "np", lambda: np), "diagonal"), _n_(21445, "np_array", lambda: np_array), axis1=1, axis2=2)
_l_(21447)
_c_(21449, _n_(21448, "print", lambda: print), '\n2D diagonals: ')
_l_(21450)
_c_(21453, _n_(21451, "print", lambda: print), _n_(21452, "result", lambda: result))
_l_(21454)
_c_(21459, _n_(21455, "print", lambda: print), 'Type: ', _c_(21458, _n_(21456, "type", lambda: type), _n_(21457, "result", lambda: result)))
_l_(21460)