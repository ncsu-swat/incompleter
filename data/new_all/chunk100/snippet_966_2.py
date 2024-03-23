# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(97156)

except ImportError:
    pass
x = _c_(97159, _a_(97158, _n_(97157, "np", lambda: np), "array"), [10, -10, 10, -10, -10, 10])
_l_(97160)
_c_(97162, _n_(97161, "print", lambda: print), 'Original arrays:')
_l_(97163)
_c_(97166, _n_(97164, "print", lambda: print), _n_(97165, "x", lambda: x))
_l_(97167)
_c_(97170, _n_(97168, "print", lambda: print), _n_(97169, "y", lambda: y))
_l_(97171)
result = _c_(97176, _a_(97173, _n_(97172, "np", lambda: np), "sum"), (_n_(97174, "x", lambda: x) == 10) & (_n_(97175, "y", lambda: y) > 0.5))
_l_(97177)
_c_(97179, _n_(97178, "print", lambda: print), '\nNumber of instances of a value occurring in one array on the condition of another array:')
_l_(97180)
_c_(97183, _n_(97181, "print", lambda: print), _n_(97182, "result", lambda: result))
_l_(97184)