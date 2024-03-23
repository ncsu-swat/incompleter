# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(51905)

except ImportError:
    pass
_c_(51907, _n_(51906, "print", lambda: print), 'Original matrix:')
_l_(51908)
_c_(51911, _n_(51909, "print", lambda: print), _n_(51910, "m", lambda: m))
_l_(51912)
result = _c_(51917, _a_(51915, _a_(51914, _n_(51913, "np", lambda: np), "linalg"), "cond"), _n_(51916, "m", lambda: m))
_l_(51918)
_c_(51920, _n_(51919, "print", lambda: print), 'Condition number of the said matrix:')
_l_(51921)
_c_(51924, _n_(51922, "print", lambda: print), _n_(51923, "result", lambda: result))
_l_(51925)