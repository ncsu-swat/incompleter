# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(35614)

except ImportError:
    pass
try:
    import os
    _l_(35616)

except ImportError:
    pass
a = _c_(35619, _a_(35618, _n_(35617, "np", lambda: np), "array"), [1, 2, 3, 4, 5, 6])
_l_(35620)
_c_(35622, _n_(35621, "print", lambda: print), 'Original array:')
_l_(35623)
_c_(35626, _n_(35624, "print", lambda: print), _n_(35625, "a", lambda: a))
_l_(35627)
a_bytes = _c_(35630, _a_(35629, _n_(35628, "a", lambda: a), "tostring"))
_l_(35631)
_c_(35633, _n_(35632, "print", lambda: print), 'After loading, content of the text file:')
_l_(35634)
_c_(35637, _n_(35635, "print", lambda: print), _n_(35636, "a2", lambda: a2))
_l_(35638)
_c_(35645, _n_(35639, "print", lambda: print), _c_(35644, _a_(35641, _n_(35640, "np", lambda: np), "array_equal"), _n_(35642, "a", lambda: a), _n_(35643, "a2", lambda: a2)))
_l_(35646)