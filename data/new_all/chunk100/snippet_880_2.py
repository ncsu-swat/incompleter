# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(86537)

except ImportError:
    pass
x = _c_(86546, _a_(86539, _n_(86538, "np", lambda: np), "array"), [200, 300, _a_(86541, _n_(86540, "np", lambda: np), "nan"), _a_(86543, _n_(86542, "np", lambda: np), "nan"), _a_(86545, _n_(86544, "np", lambda: np), "nan"), 700])
_l_(86547)
_c_(86549, _n_(86548, "print", lambda: print), 'Original array:')
_l_(86550)
_c_(86553, _n_(86551, "print", lambda: print), _n_(86552, "x", lambda: x))
_l_(86554)
_c_(86556, _n_(86555, "print", lambda: print), 'After removing nan values:')
_l_(86557)
result = _n_(86558, "x", lambda: x)[_c_(86565, _a_(86560, _n_(86559, "np", lambda: np), "logical_not"), _c_(86564, _a_(86562, _n_(86561, "np", lambda: np), "isnan"), _n_(86563, "x", lambda: x)))]
_l_(86566)
_c_(86569, _n_(86567, "print", lambda: print), _n_(86568, "result", lambda: result))
_l_(86570)
_c_(86572, _n_(86571, "print", lambda: print), '\nOriginal array:')
_l_(86573)
_c_(86576, _n_(86574, "print", lambda: print), _n_(86575, "y", lambda: y))
_l_(86577)
_c_(86579, _n_(86578, "print", lambda: print), 'After removing nan values:')
_l_(86580)
result = _n_(86581, "y", lambda: y)[_c_(86588, _a_(86583, _n_(86582, "np", lambda: np), "logical_not"), _c_(86587, _a_(86585, _n_(86584, "np", lambda: np), "isnan"), _n_(86586, "y", lambda: y)))]
_l_(86589)
_c_(86592, _n_(86590, "print", lambda: print), _n_(86591, "result", lambda: result))
_l_(86593)