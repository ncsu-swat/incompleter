# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(67011)

except ImportError:
    pass
a1 = _c_(67014, _a_(67013, _n_(67012, "np", lambda: np), "array"), [1, 2, 3, 4])
_l_(67015)
a2 = _c_(67018, _a_(67017, _n_(67016, "np", lambda: np), "array"), ['Red', 'Green', 'White', 'Orange'])
_l_(67019)
result = _c_(67027, _a_(67023, _a_(67022, _a_(67021, _n_(67020, "np", lambda: np), "core"), "records"), "fromarrays"), [_n_(67024, "a1", lambda: a1), _n_(67025, "a2", lambda: a2), _n_(67026, "a3", lambda: a3)], names='a,b,c')
_l_(67028)
_c_(67031, _n_(67029, "print", lambda: print), _n_(67030, "result", lambda: result)[0])
_l_(67032)
_c_(67035, _n_(67033, "print", lambda: print), _n_(67034, "result", lambda: result)[1])
_l_(67036)
_c_(67039, _n_(67037, "print", lambda: print), _n_(67038, "result", lambda: result)[2])
_l_(67040)