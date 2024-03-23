# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(80838)

except ImportError:
    pass
_c_(80840, _n_(80839, "print", lambda: print), 'Original array:')
_l_(80841)
_c_(80844, _n_(80842, "print", lambda: print), _n_(80843, "x", lambda: x))
_l_(80845)
_c_(80847, _n_(80846, "print", lambda: print), 'Remove all non-numeric elements of the said array')
_l_(80848)
_c_(80857, _n_(80849, "print", lambda: print), _n_(80850, "x", lambda: x)[~_c_(80856, _a_(80855, _c_(80854, _a_(80852, _n_(80851, "np", lambda: np), "isnan"), _n_(80853, "x", lambda: x)), "any"), axis=1)])
_l_(80858)