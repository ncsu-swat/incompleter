# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(67042)

except ImportError:
    pass
a2 = _c_(67045, _a_(67044, _n_(67043, "np", lambda: np), "array"), ['Red', 'Green', 'White', 'Orange'])
_l_(67046)
a3 = _c_(67049, _a_(67048, _n_(67047, "np", lambda: np), "array"), [12.2, 15, 20, 40])
_l_(67050)
result = _c_(67058, _a_(67054, _a_(67053, _a_(67052, _n_(67051, "np", lambda: np), "core"), "records"), "fromarrays"), [_n_(67055, "a1", lambda: a1), _n_(67056, "a2", lambda: a2), _n_(67057, "a3", lambda: a3)], names='a,b,c')
_l_(67059)
_c_(67062, _n_(67060, "print", lambda: print), _n_(67061, "result", lambda: result)[0])
_l_(67063)
_c_(67066, _n_(67064, "print", lambda: print), _n_(67065, "result", lambda: result)[1])
_l_(67067)
_c_(67070, _n_(67068, "print", lambda: print), _n_(67069, "result", lambda: result)[2])
_l_(67071)