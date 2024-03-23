# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(70086)

except ImportError:
    pass
a = _c_(70089, _a_(70088, _n_(70087, "np", lambda: np), "array"), [1, 2, 5])
_l_(70090)
b = _c_(70093, _a_(70092, _n_(70091, "np", lambda: np), "array"), [2, 1, 0])
_l_(70094)
_c_(70096, _n_(70095, "print", lambda: print), 'Original 1-d arrays:')
_l_(70097)
_c_(70100, _n_(70098, "print", lambda: print), _n_(70099, "a", lambda: a))
_l_(70101)
_c_(70104, _n_(70102, "print", lambda: print), _n_(70103, "b", lambda: b))
_l_(70105)
_n_(70106, "print", lambda: print)
_l_(70107)
result = _c_(70112, _a_(70109, _n_(70108, "np", lambda: np), "inner"), _n_(70110, "a", lambda: a), _n_(70111, "b", lambda: b))
_l_(70113)
_c_(70115, _n_(70114, "print", lambda: print), 'Inner product of the said vectors:')
_l_(70116)
x = _c_(70121, _a_(70120, _c_(70119, _a_(70118, _n_(70117, "np", lambda: np), "arange"), 9), "reshape"), 3, 3)
_l_(70122)
_c_(70124, _n_(70123, "print", lambda: print), 'Higher dimension arrays:')
_l_(70125)
_c_(70128, _n_(70126, "print", lambda: print), _n_(70127, "x", lambda: x))
_l_(70129)
_c_(70132, _n_(70130, "print", lambda: print), _n_(70131, "y", lambda: y))
_l_(70133)
result = _c_(70138, _a_(70135, _n_(70134, "np", lambda: np), "inner"), _n_(70136, "x", lambda: x), _n_(70137, "y", lambda: y))
_l_(70139)
_c_(70141, _n_(70140, "print", lambda: print), 'Inner product of the said vectors:')
_l_(70142)
_c_(70145, _n_(70143, "print", lambda: print), _n_(70144, "result", lambda: result))
_l_(70146)