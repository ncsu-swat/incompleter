# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(86420)

except ImportError:
    pass
x = _c_(86429, _a_(86422, _n_(86421, "np", lambda: np), "array"), [200, 300, _a_(86424, _n_(86423, "np", lambda: np), "nan"), _a_(86426, _n_(86425, "np", lambda: np), "nan"), _a_(86428, _n_(86427, "np", lambda: np), "nan"), 700])
_l_(86430)
y = _c_(86439, _a_(86432, _n_(86431, "np", lambda: np), "array"), [[1, 2, 3], [_a_(86434, _n_(86433, "np", lambda: np), "nan"), 0, _a_(86436, _n_(86435, "np", lambda: np), "nan")], [6, 7, _a_(86438, _n_(86437, "np", lambda: np), "nan")]])
_l_(86440)
_c_(86442, _n_(86441, "print", lambda: print), 'Original array:')
_l_(86443)
_c_(86446, _n_(86444, "print", lambda: print), _n_(86445, "x", lambda: x))
_l_(86447)
_c_(86449, _n_(86448, "print", lambda: print), 'After removing nan values:')
_l_(86450)
_c_(86453, _n_(86451, "print", lambda: print), _n_(86452, "result", lambda: result))
_l_(86454)
_c_(86456, _n_(86455, "print", lambda: print), '\nOriginal array:')
_l_(86457)
_c_(86460, _n_(86458, "print", lambda: print), _n_(86459, "y", lambda: y))
_l_(86461)
_c_(86463, _n_(86462, "print", lambda: print), 'After removing nan values:')
_l_(86464)
result = _n_(86465, "y", lambda: y)[_c_(86472, _a_(86467, _n_(86466, "np", lambda: np), "logical_not"), _c_(86471, _a_(86469, _n_(86468, "np", lambda: np), "isnan"), _n_(86470, "y", lambda: y)))]
_l_(86473)
_c_(86476, _n_(86474, "print", lambda: print), _n_(86475, "result", lambda: result))
_l_(86477)