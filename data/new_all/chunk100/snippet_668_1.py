# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(68742)

except ImportError:
    pass
x = _c_(68747, _a_(68746, _c_(68745, _a_(68744, _n_(68743, "np", lambda: np), "arange"), 24), "reshape"), (2, 3, 4))
_l_(68748)
_c_(68750, _n_(68749, "print", lambda: print), 'Array x:')
_l_(68751)
_c_(68754, _n_(68752, "print", lambda: print), _n_(68753, "x", lambda: x))
_l_(68755)
_c_(68757, _n_(68756, "print", lambda: print), 'Array y:')
_l_(68758)
_c_(68761, _n_(68759, "print", lambda: print), _n_(68760, "y", lambda: y))
_l_(68762)
_c_(68764, _n_(68763, "print", lambda: print), 'Inner of x and y arrays:')
_l_(68765)
_c_(68772, _n_(68766, "print", lambda: print), _c_(68771, _a_(68768, _n_(68767, "np", lambda: np), "inner"), _n_(68769, "x", lambda: x), _n_(68770, "y", lambda: y)))
_l_(68773)