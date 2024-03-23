# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(70212)

except ImportError:
    pass
a = _c_(70215, _a_(70214, _n_(70213, "np", lambda: np), "array"), [1, 2, 5])
_l_(70216)
b = _c_(70219, _a_(70218, _n_(70217, "np", lambda: np), "array"), [2, 1, 0])
_l_(70220)
_c_(70222, _n_(70221, "print", lambda: print), 'Original 1-d arrays:')
_l_(70223)
_c_(70226, _n_(70224, "print", lambda: print), _n_(70225, "a", lambda: a))
_l_(70227)
_c_(70230, _n_(70228, "print", lambda: print), _n_(70229, "b", lambda: b))
_l_(70231)
_n_(70232, "print", lambda: print)
_l_(70233)
_c_(70235, _n_(70234, "print", lambda: print), 'Inner product of the said vectors:')
_l_(70236)
x = _c_(70241, _a_(70240, _c_(70239, _a_(70238, _n_(70237, "np", lambda: np), "arange"), 9), "reshape"), 3, 3)
_l_(70242)
y = _c_(70247, _a_(70246, _c_(70245, _a_(70244, _n_(70243, "np", lambda: np), "arange"), 3, 12), "reshape"), 3, 3)
_l_(70248)
_c_(70250, _n_(70249, "print", lambda: print), 'Higher dimension arrays:')
_l_(70251)
_c_(70254, _n_(70252, "print", lambda: print), _n_(70253, "x", lambda: x))
_l_(70255)
_c_(70258, _n_(70256, "print", lambda: print), _n_(70257, "y", lambda: y))
_l_(70259)
result = _c_(70264, _a_(70261, _n_(70260, "np", lambda: np), "inner"), _n_(70262, "x", lambda: x), _n_(70263, "y", lambda: y))
_l_(70265)
_c_(70267, _n_(70266, "print", lambda: print), 'Inner product of the said vectors:')
_l_(70268)
_c_(70271, _n_(70269, "print", lambda: print), _n_(70270, "result", lambda: result))
_l_(70272)