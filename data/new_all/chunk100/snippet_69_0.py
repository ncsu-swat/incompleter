# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(71889)

except ImportError:
    pass
x = _c_(71892, _a_(71891, _n_(71890, "np", lambda: np), "array"), [-180.0, -90.0, 90.0, 180.0])
_l_(71893)
r2 = _c_(71897, _a_(71895, _n_(71894, "np", lambda: np), "deg2rad"), _n_(71896, "x", lambda: x))
_l_(71898)
assert _c_(71903, _a_(71900, _n_(71899, "np", lambda: np), "array_equiv"), _n_(71901, "r1", lambda: r1), _n_(71902, "r2", lambda: r2))
_l_(71904)
_c_(71907, _n_(71905, "print", lambda: print), _n_(71906, "r1", lambda: r1))
_l_(71908)