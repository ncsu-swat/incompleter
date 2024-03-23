# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(80932)

except ImportError:
    pass
y = _c_(80935, _a_(80934, _n_(80933, "np", lambda: np), "array"), [4, 5])
_l_(80936)
result = _c_(80953, _a_(80938, _n_(80937, "np", lambda: np), "transpose"), [_c_(80945, _a_(80940, _n_(80939, "np", lambda: np), "tile"), _n_(80941, "x", lambda: x), _c_(80944, _n_(80942, "len", lambda: len), _n_(80943, "y", lambda: y))), _c_(80952, _a_(80947, _n_(80946, "np", lambda: np), "repeat"), _n_(80948, "y", lambda: y), _c_(80951, _n_(80949, "len", lambda: len), _n_(80950, "x", lambda: x)))])
_l_(80954)
_c_(80957, _n_(80955, "print", lambda: print), _n_(80956, "result", lambda: result))
_l_(80958)