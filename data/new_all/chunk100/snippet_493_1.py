# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(51664)

except ImportError:
    pass
_c_(51666, _n_(51665, "print", lambda: print), '\nOriginal arrays:')
_l_(51667)
x = _c_(51670, _a_(51669, _n_(51668, "np", lambda: np), "array"), (1, 2, 3))
_l_(51671)
y = _c_(51674, _a_(51673, _n_(51672, "np", lambda: np), "array"), (2, 3, 4))
_l_(51675)
_c_(51677, _n_(51676, "print", lambda: print), 'Array-1')
_l_(51678)
_c_(51681, _n_(51679, "print", lambda: print), _n_(51680, "x", lambda: x))
_l_(51682)
_c_(51684, _n_(51683, "print", lambda: print), 'Array-2')
_l_(51685)
_c_(51688, _n_(51686, "print", lambda: print), _n_(51687, "y", lambda: y))
_l_(51689)
_c_(51691, _n_(51690, "print", lambda: print), '\nStack 1-D arrays as columns wise:')
_l_(51692)
_c_(51695, _n_(51693, "print", lambda: print), _n_(51694, "new_array", lambda: new_array))
_l_(51696)