# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(113571)

except ImportError:
    pass
_c_(113573, _n_(113572, "print", lambda: print), 'Original array:')
_l_(113574)
_c_(113577, _n_(113575, "print", lambda: print), _n_(113576, "x", lambda: x))
_l_(113578)
_c_(113580, _n_(113579, "print", lambda: print), 'Sum of all elements:')
_l_(113581)
_c_(113587, _n_(113582, "print", lambda: print), _c_(113586, _a_(113584, _n_(113583, "np", lambda: np), "sum"), _n_(113585, "x", lambda: x)))
_l_(113588)
_c_(113590, _n_(113589, "print", lambda: print), 'Sum of each column:')
_l_(113591)
_c_(113597, _n_(113592, "print", lambda: print), _c_(113596, _a_(113594, _n_(113593, "np", lambda: np), "sum"), _n_(113595, "x", lambda: x), axis=0))
_l_(113598)
_c_(113600, _n_(113599, "print", lambda: print), 'Sum of each row:')
_l_(113601)
_c_(113607, _n_(113602, "print", lambda: print), _c_(113606, _a_(113604, _n_(113603, "np", lambda: np), "sum"), _n_(113605, "x", lambda: x), axis=1))
_l_(113608)