# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(35577)

except ImportError:
    pass
try:
    import os
    _l_(35579)

except ImportError:
    pass
_c_(35581, _n_(35580, "print", lambda: print), 'Original array:')
_l_(35582)
_c_(35585, _n_(35583, "print", lambda: print), _n_(35584, "a", lambda: a))
_l_(35586)
a_bytes = _c_(35589, _a_(35588, _n_(35587, "a", lambda: a), "tostring"))
_l_(35590)
a2 = _c_(35596, _a_(35592, _n_(35591, "np", lambda: np), "fromstring"), _n_(35593, "a_bytes", lambda: a_bytes), dtype=_a_(35595, _n_(35594, "a", lambda: a), "dtype"))
_l_(35597)
_c_(35599, _n_(35598, "print", lambda: print), 'After loading, content of the text file:')
_l_(35600)
_c_(35603, _n_(35601, "print", lambda: print), _n_(35602, "a2", lambda: a2))
_l_(35604)
_c_(35611, _n_(35605, "print", lambda: print), _c_(35610, _a_(35607, _n_(35606, "np", lambda: np), "array_equal"), _n_(35608, "a", lambda: a), _n_(35609, "a2", lambda: a2)))
_l_(35612)