# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(51413)

except ImportError:
    pass
try:
    import os
    _l_(51415)

except ImportError:
    pass
x = _c_(51418, _a_(51417, _n_(51416, "np", lambda: np), "arange"), 10)
_l_(51419)
y = _c_(51422, _a_(51421, _n_(51420, "np", lambda: np), "arange"), 11, 20)
_l_(51423)
_c_(51425, _n_(51424, "print", lambda: print), 'Original arrays:')
_l_(51426)
_c_(51429, _n_(51427, "print", lambda: print), _n_(51428, "x", lambda: x))
_l_(51430)
_c_(51433, _n_(51431, "print", lambda: print), _n_(51432, "y", lambda: y))
_l_(51434)
_c_(51439, _a_(51436, _n_(51435, "np", lambda: np), "savez"), 'temp_arra.npz', x=_n_(51437, "x", lambda: x), y=_n_(51438, "y", lambda: y))
_l_(51440)
_c_(51442, _n_(51441, "print", lambda: print), "Load arrays from the 'temp_arra.npz' file:")
_l_(51443)
with _c_(51446, _a_(51445, _n_(51444, "np", lambda: np), "load"), 'temp_arra.npz') as data:
    _l_(51457)

    x2 = _n_(51447, "data", lambda: data)['x']
    _l_(51448)
    _c_(51451, _n_(51449, "print", lambda: print), _n_(51450, "x2", lambda: x2))
    _l_(51452)
    _c_(51455, _n_(51453, "print", lambda: print), _n_(51454, "y2", lambda: y2))
    _l_(51456)