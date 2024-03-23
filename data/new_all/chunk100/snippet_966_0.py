# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(97098)

except ImportError:
    pass
y = _c_(97101, _a_(97100, _n_(97099, "np", lambda: np), "array"), [0.85, 0.45, 0.9, 0.8, 0.12, 0.6])
_l_(97102)
_c_(97104, _n_(97103, "print", lambda: print), 'Original arrays:')
_l_(97105)
_c_(97108, _n_(97106, "print", lambda: print), _n_(97107, "x", lambda: x))
_l_(97109)
_c_(97112, _n_(97110, "print", lambda: print), _n_(97111, "y", lambda: y))
_l_(97113)
result = _c_(97118, _a_(97115, _n_(97114, "np", lambda: np), "sum"), (_n_(97116, "x", lambda: x) == 10) & (_n_(97117, "y", lambda: y) > 0.5))
_l_(97119)
_c_(97121, _n_(97120, "print", lambda: print), '\nNumber of instances of a value occurring in one array on the condition of another array:')
_l_(97122)
_c_(97125, _n_(97123, "print", lambda: print), _n_(97124, "result", lambda: result))
_l_(97126)