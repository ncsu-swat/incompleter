# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(114628)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(114630)

except ImportError:
    pass
y = _c_(114634, _a_(114632, _n_(114631, "np", lambda: np), "sin"), _n_(114633, "x", lambda: x))
_l_(114635)
_c_(114637, _n_(114636, "print", lambda: print), 'Plot the points using matplotlib:')
_l_(114638)
_c_(114643, _a_(114640, _n_(114639, "plt", lambda: plt), "plot"), _n_(114641, "x", lambda: x), _n_(114642, "y", lambda: y))
_l_(114644)
_c_(114647, _a_(114646, _n_(114645, "plt", lambda: plt), "show"))
_l_(114648)