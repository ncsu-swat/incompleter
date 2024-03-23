# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(78902)

except ImportError:
    pass
z = _c_(78906, _a_(78905, _a_(78904, _n_(78903, "np", lambda: np), "random"), "random"), (10, 2))
_l_(78907)
(x, y) = (_n_(78908, "z", lambda: z)[:, 0], _n_(78909, "z", lambda: z)[:, 1])
_l_(78910)
t = _c_(78915, _a_(78912, _n_(78911, "np", lambda: np), "arctan2"), _n_(78913, "y", lambda: y), _n_(78914, "x", lambda: x))
_l_(78916)
_c_(78919, _n_(78917, "print", lambda: print), _n_(78918, "r", lambda: r))
_l_(78920)
_c_(78923, _n_(78921, "print", lambda: print), _n_(78922, "t", lambda: t))
_l_(78924)