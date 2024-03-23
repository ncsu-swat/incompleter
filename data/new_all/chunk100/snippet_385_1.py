# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(38535)

except ImportError:
    pass
_c_(38537, _n_(38536, "print", lambda: print), 'Original array:')
_l_(38538)
_c_(38541, _n_(38539, "print", lambda: print), _n_(38540, "x", lambda: x))
_l_(38542)
y = _c_(38546, _a_(38544, _n_(38543, "np", lambda: np), "empty_like"), _n_(38545, "x", lambda: x))
_l_(38547)
_n_(38548, "y", lambda: y)[:] = _n_(38549, "x", lambda: x)
_l_(38550)
_c_(38552, _n_(38551, "print", lambda: print), '\nCopy of the said array:')
_l_(38553)
_c_(38556, _n_(38554, "print", lambda: print), _n_(38555, "y", lambda: y))
_l_(38557)