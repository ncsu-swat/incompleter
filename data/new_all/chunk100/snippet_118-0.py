# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(101113)

except ImportError:
    pass
v = _c_(101116, _a_(101115, _n_(101114, "np", lambda: np), "arange"), 7)
_l_(101117)
result = _c_(101122, _a_(101120, _a_(101119, _n_(101118, "np", lambda: np), "linalg"), "norm"), _n_(101121, "v", lambda: v))
_l_(101123)
_c_(101125, _n_(101124, "print", lambda: print), 'Vector norm:')
_l_(101126)
_c_(101129, _n_(101127, "print", lambda: print), _n_(101128, "result", lambda: result))
_l_(101130)
result1 = _c_(101135, _a_(101133, _a_(101132, _n_(101131, "np", lambda: np), "linalg"), "norm"), _n_(101134, "m", lambda: m))
_l_(101136)
_c_(101138, _n_(101137, "print", lambda: print), 'Matrix norm:')
_l_(101139)
_c_(101142, _n_(101140, "print", lambda: print), _n_(101141, "result1", lambda: result1))
_l_(101143)