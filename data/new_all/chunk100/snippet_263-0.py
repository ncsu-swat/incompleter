# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(107598)

except ImportError:
    pass
np_array = _c_(107603, _a_(107602, _c_(107601, _a_(107600, _n_(107599, "np", lambda: np), "arange"), 3 * 4 * 5), "reshape"), 3, 4, 5)
_l_(107604)
_c_(107606, _n_(107605, "print", lambda: print), 'Original Numpy array:')
_l_(107607)
_c_(107610, _n_(107608, "print", lambda: print), _n_(107609, "np_array", lambda: np_array))
_l_(107611)
_c_(107616, _n_(107612, "print", lambda: print), 'Type: ', _c_(107615, _n_(107613, "type", lambda: type), _n_(107614, "np_array", lambda: np_array)))
_l_(107617)
_c_(107619, _n_(107618, "print", lambda: print), '\n2D diagonals: ')
_l_(107620)
_c_(107623, _n_(107621, "print", lambda: print), _n_(107622, "result", lambda: result))
_l_(107624)
_c_(107629, _n_(107625, "print", lambda: print), 'Type: ', _c_(107628, _n_(107626, "type", lambda: type), _n_(107627, "result", lambda: result)))
_l_(107630)