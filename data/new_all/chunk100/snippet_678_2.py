# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(70148)

except ImportError:
    pass
b = _c_(70151, _a_(70150, _n_(70149, "np", lambda: np), "array"), [2, 1, 0])
_l_(70152)
_c_(70154, _n_(70153, "print", lambda: print), 'Original 1-d arrays:')
_l_(70155)
_c_(70158, _n_(70156, "print", lambda: print), _n_(70157, "a", lambda: a))
_l_(70159)
_c_(70162, _n_(70160, "print", lambda: print), _n_(70161, "b", lambda: b))
_l_(70163)
_n_(70164, "print", lambda: print)
_l_(70165)
result = _c_(70170, _a_(70167, _n_(70166, "np", lambda: np), "inner"), _n_(70168, "a", lambda: a), _n_(70169, "b", lambda: b))
_l_(70171)
_c_(70173, _n_(70172, "print", lambda: print), 'Inner product of the said vectors:')
_l_(70174)
x = _c_(70179, _a_(70178, _c_(70177, _a_(70176, _n_(70175, "np", lambda: np), "arange"), 9), "reshape"), 3, 3)
_l_(70180)
y = _c_(70185, _a_(70184, _c_(70183, _a_(70182, _n_(70181, "np", lambda: np), "arange"), 3, 12), "reshape"), 3, 3)
_l_(70186)
_c_(70188, _n_(70187, "print", lambda: print), 'Higher dimension arrays:')
_l_(70189)
_c_(70192, _n_(70190, "print", lambda: print), _n_(70191, "x", lambda: x))
_l_(70193)
_c_(70196, _n_(70194, "print", lambda: print), _n_(70195, "y", lambda: y))
_l_(70197)
result = _c_(70202, _a_(70199, _n_(70198, "np", lambda: np), "inner"), _n_(70200, "x", lambda: x), _n_(70201, "y", lambda: y))
_l_(70203)
_c_(70205, _n_(70204, "print", lambda: print), 'Inner product of the said vectors:')
_l_(70206)
_c_(70209, _n_(70207, "print", lambda: print), _n_(70208, "result", lambda: result))
_l_(70210)