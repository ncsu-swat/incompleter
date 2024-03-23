# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(70024)

except ImportError:
    pass
a = _c_(70027, _a_(70026, _n_(70025, "np", lambda: np), "array"), [1, 2, 5])
_l_(70028)
b = _c_(70031, _a_(70030, _n_(70029, "np", lambda: np), "array"), [2, 1, 0])
_l_(70032)
_c_(70034, _n_(70033, "print", lambda: print), 'Original 1-d arrays:')
_l_(70035)
_c_(70038, _n_(70036, "print", lambda: print), _n_(70037, "a", lambda: a))
_l_(70039)
_c_(70042, _n_(70040, "print", lambda: print), _n_(70041, "b", lambda: b))
_l_(70043)
_n_(70044, "print", lambda: print)
_l_(70045)
result = _c_(70050, _a_(70047, _n_(70046, "np", lambda: np), "inner"), _n_(70048, "a", lambda: a), _n_(70049, "b", lambda: b))
_l_(70051)
_c_(70053, _n_(70052, "print", lambda: print), 'Inner product of the said vectors:')
_l_(70054)
x = _c_(70059, _a_(70058, _c_(70057, _a_(70056, _n_(70055, "np", lambda: np), "arange"), 9), "reshape"), 3, 3)
_l_(70060)
y = _c_(70065, _a_(70064, _c_(70063, _a_(70062, _n_(70061, "np", lambda: np), "arange"), 3, 12), "reshape"), 3, 3)
_l_(70066)
_c_(70068, _n_(70067, "print", lambda: print), 'Higher dimension arrays:')
_l_(70069)
_c_(70072, _n_(70070, "print", lambda: print), _n_(70071, "x", lambda: x))
_l_(70073)
_c_(70076, _n_(70074, "print", lambda: print), _n_(70075, "y", lambda: y))
_l_(70077)
_c_(70079, _n_(70078, "print", lambda: print), 'Inner product of the said vectors:')
_l_(70080)
_c_(70083, _n_(70081, "print", lambda: print), _n_(70082, "result", lambda: result))
_l_(70084)