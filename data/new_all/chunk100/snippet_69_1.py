# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(71910)

except ImportError:
    pass
r1 = _c_(71914, _a_(71912, _n_(71911, "np", lambda: np), "radians"), _n_(71913, "x", lambda: x))
_l_(71915)
r2 = _c_(71919, _a_(71917, _n_(71916, "np", lambda: np), "deg2rad"), _n_(71918, "x", lambda: x))
_l_(71920)
assert _c_(71925, _a_(71922, _n_(71921, "np", lambda: np), "array_equiv"), _n_(71923, "r1", lambda: r1), _n_(71924, "r2", lambda: r2))
_l_(71926)
_c_(71929, _n_(71927, "print", lambda: print), _n_(71928, "r1", lambda: r1))
_l_(71930)