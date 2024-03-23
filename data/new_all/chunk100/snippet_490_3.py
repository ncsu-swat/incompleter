# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(51459)

except ImportError:
    pass
try:
    import os
    _l_(51461)

except ImportError:
    pass
x = _c_(51464, _a_(51463, _n_(51462, "np", lambda: np), "arange"), 10)
_l_(51465)
_c_(51467, _n_(51466, "print", lambda: print), 'Original arrays:')
_l_(51468)
_c_(51471, _n_(51469, "print", lambda: print), _n_(51470, "x", lambda: x))
_l_(51472)
_c_(51475, _n_(51473, "print", lambda: print), _n_(51474, "y", lambda: y))
_l_(51476)
_c_(51481, _a_(51478, _n_(51477, "np", lambda: np), "savez"), 'temp_arra.npz', x=_n_(51479, "x", lambda: x), y=_n_(51480, "y", lambda: y))
_l_(51482)
_c_(51484, _n_(51483, "print", lambda: print), "Load arrays from the 'temp_arra.npz' file:")
_l_(51485)
with _c_(51488, _a_(51487, _n_(51486, "np", lambda: np), "load"), 'temp_arra.npz') as data:
    _l_(51501)

    x2 = _n_(51489, "data", lambda: data)['x']
    _l_(51490)
    y2 = _n_(51491, "data", lambda: data)['y']
    _l_(51492)
    _c_(51495, _n_(51493, "print", lambda: print), _n_(51494, "x2", lambda: x2))
    _l_(51496)
    _c_(51499, _n_(51497, "print", lambda: print), _n_(51498, "y2", lambda: y2))
    _l_(51500)