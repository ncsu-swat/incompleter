# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(101175)

except ImportError:
    pass
v = _c_(101178, _a_(101177, _n_(101176, "np", lambda: np), "arange"), 7)
_l_(101179)
_c_(101181, _n_(101180, "print", lambda: print), 'Vector norm:')
_l_(101182)
_c_(101185, _n_(101183, "print", lambda: print), _n_(101184, "result", lambda: result))
_l_(101186)
m = _c_(101189, _a_(101188, _n_(101187, "np", lambda: np), "matrix"), '1, 2; 3, 4')
_l_(101190)
result1 = _c_(101195, _a_(101193, _a_(101192, _n_(101191, "np", lambda: np), "linalg"), "norm"), _n_(101194, "m", lambda: m))
_l_(101196)
_c_(101198, _n_(101197, "print", lambda: print), 'Matrix norm:')
_l_(101199)
_c_(101202, _n_(101200, "print", lambda: print), _n_(101201, "result1", lambda: result1))
_l_(101203)