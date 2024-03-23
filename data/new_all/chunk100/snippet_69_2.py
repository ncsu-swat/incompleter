# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(71932)

except ImportError:
    pass
x = _c_(71935, _a_(71934, _n_(71933, "np", lambda: np), "array"), [-180.0, -90.0, 90.0, 180.0])
_l_(71936)
r1 = _c_(71940, _a_(71938, _n_(71937, "np", lambda: np), "radians"), _n_(71939, "x", lambda: x))
_l_(71941)
assert _c_(71946, _a_(71943, _n_(71942, "np", lambda: np), "array_equiv"), _n_(71944, "r1", lambda: r1), _n_(71945, "r2", lambda: r2))
_l_(71947)
_c_(71950, _n_(71948, "print", lambda: print), _n_(71949, "r1", lambda: r1))
_l_(71951)