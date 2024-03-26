# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(114605)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(114607)

except ImportError:
    pass
x = _c_(114612, _a_(114609, _n_(114608, "np", lambda: np), "arange"), 0, 3 * _a_(114611, _n_(114610, "np", lambda: np), "pi"), 0.2)
_l_(114613)
_c_(114615, _n_(114614, "print", lambda: print), 'Plot the points using matplotlib:')
_l_(114616)
_c_(114621, _a_(114618, _n_(114617, "plt", lambda: plt), "plot"), _n_(114619, "x", lambda: x), _n_(114620, "y", lambda: y))
_l_(114622)
_c_(114625, _a_(114624, _n_(114623, "plt", lambda: plt), "show"))
_l_(114626)