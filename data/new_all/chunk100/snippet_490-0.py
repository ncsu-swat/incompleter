# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(118427)

except ImportError:
    pass
try:
    import os
    _l_(118429)

except ImportError:
    pass
y = _c_(118432, _a_(118431, _n_(118430, "np", lambda: np), "arange"), 11, 20)
_l_(118433)
_c_(118435, _n_(118434, "print", lambda: print), 'Original arrays:')
_l_(118436)
_c_(118439, _n_(118437, "print", lambda: print), _n_(118438, "x", lambda: x))
_l_(118440)
_c_(118443, _n_(118441, "print", lambda: print), _n_(118442, "y", lambda: y))
_l_(118444)
_c_(118449, _a_(118446, _n_(118445, "np", lambda: np), "savez"), 'temp_arra.npz', x=_n_(118447, "x", lambda: x), y=_n_(118448, "y", lambda: y))
_l_(118450)
_c_(118452, _n_(118451, "print", lambda: print), "Load arrays from the 'temp_arra.npz' file:")
_l_(118453)
with _c_(118456, _a_(118455, _n_(118454, "np", lambda: np), "load"), 'temp_arra.npz') as data:
    _l_(118469)

    x2 = _n_(118457, "data", lambda: data)['x']
    _l_(118458)
    y2 = _n_(118459, "data", lambda: data)['y']
    _l_(118460)
    _c_(118463, _n_(118461, "print", lambda: print), _n_(118462, "x2", lambda: x2))
    _l_(118464)
    _c_(118467, _n_(118465, "print", lambda: print), _n_(118466, "y2", lambda: y2))
    _l_(118468)