# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(92432)

except ImportError:
    pass
x = _c_(92435, _a_(92434, _n_(92433, "np", lambda: np), "array"), [1, 2, 3])
_l_(92436)
y = _c_(92439, _a_(92438, _n_(92437, "np", lambda: np), "array"), [2, 3, 4])
_l_(92440)
_c_(92442, _n_(92441, "print", lambda: print), 'Original arrays:')
_l_(92443)
_c_(92446, _n_(92444, "print", lambda: print), _n_(92445, "x", lambda: x))
_l_(92447)
_c_(92450, _n_(92448, "print", lambda: print), _n_(92449, "y", lambda: y))
_l_(92451)
_c_(92453, _n_(92452, "print", lambda: print), 'Sequence of arrays along a new axis:')
_l_(92454)
_c_(92461, _n_(92455, "print", lambda: print), _c_(92460, _a_(92457, _n_(92456, "np", lambda: np), "vstack"), (_n_(92458, "x", lambda: x), _n_(92459, "y", lambda: y))))
_l_(92462)
x = _c_(92465, _a_(92464, _n_(92463, "np", lambda: np), "array"), [[1], [2], [3]])
_l_(92466)
_c_(92468, _n_(92467, "print", lambda: print), '\nOriginal arrays:')
_l_(92469)
_c_(92472, _n_(92470, "print", lambda: print), _n_(92471, "x", lambda: x))
_l_(92473)
_c_(92475, _n_(92474, "print", lambda: print))
_l_(92476)
_c_(92479, _n_(92477, "print", lambda: print), _n_(92478, "y", lambda: y))
_l_(92480)
_c_(92482, _n_(92481, "print", lambda: print), 'Sequence of arrays along a new axis:')
_l_(92483)
_c_(92490, _n_(92484, "print", lambda: print), _c_(92489, _a_(92486, _n_(92485, "np", lambda: np), "vstack"), (_n_(92487, "x", lambda: x), _n_(92488, "y", lambda: y))))
_l_(92491)