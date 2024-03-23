# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(88304)

except ImportError:
    pass
_c_(88306, _n_(88305, "print", lambda: print), '\nOriginal array:')
_l_(88307)
_c_(88310, _n_(88308, "print", lambda: print), _n_(88309, "x", lambda: x))
_l_(88311)
r1 = _c_(88315, _a_(88313, _n_(88312, "np", lambda: np), "percentile"), _n_(88314, "x", lambda: x), 80, 1)
_l_(88316)
_c_(88318, _n_(88317, "print", lambda: print), '\n80th percentile for all elements of the said array along the second axis:')
_l_(88319)
_c_(88322, _n_(88320, "print", lambda: print), _n_(88321, "r1", lambda: r1))
_l_(88323)