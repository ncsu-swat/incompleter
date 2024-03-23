# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(80960)

except ImportError:
    pass
x = _c_(80963, _a_(80962, _n_(80961, "np", lambda: np), "array"), [1, 2, 3])
_l_(80964)
result = _c_(80981, _a_(80966, _n_(80965, "np", lambda: np), "transpose"), [_c_(80973, _a_(80968, _n_(80967, "np", lambda: np), "tile"), _n_(80969, "x", lambda: x), _c_(80972, _n_(80970, "len", lambda: len), _n_(80971, "y", lambda: y))), _c_(80980, _a_(80975, _n_(80974, "np", lambda: np), "repeat"), _n_(80976, "y", lambda: y), _c_(80979, _n_(80977, "len", lambda: len), _n_(80978, "x", lambda: x)))])
_l_(80982)
_c_(80985, _n_(80983, "print", lambda: print), _n_(80984, "result", lambda: result))
_l_(80986)