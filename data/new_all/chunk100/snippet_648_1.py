# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(66980)

except ImportError:
    pass
a1 = _c_(66983, _a_(66982, _n_(66981, "np", lambda: np), "array"), [1, 2, 3, 4])
_l_(66984)
a3 = _c_(66987, _a_(66986, _n_(66985, "np", lambda: np), "array"), [12.2, 15, 20, 40])
_l_(66988)
result = _c_(66996, _a_(66992, _a_(66991, _a_(66990, _n_(66989, "np", lambda: np), "core"), "records"), "fromarrays"), [_n_(66993, "a1", lambda: a1), _n_(66994, "a2", lambda: a2), _n_(66995, "a3", lambda: a3)], names='a,b,c')
_l_(66997)
_c_(67000, _n_(66998, "print", lambda: print), _n_(66999, "result", lambda: result)[0])
_l_(67001)
_c_(67004, _n_(67002, "print", lambda: print), _n_(67003, "result", lambda: result)[1])
_l_(67005)
_c_(67008, _n_(67006, "print", lambda: print), _n_(67007, "result", lambda: result)[2])
_l_(67009)