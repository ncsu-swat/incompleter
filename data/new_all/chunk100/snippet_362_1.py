# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(35732)

except ImportError:
    pass
_c_(35734, _n_(35733, "print", lambda: print), 'Original array: ')
_l_(35735)
_c_(35738, _n_(35736, "print", lambda: print), _n_(35737, "a", lambda: a))
_l_(35739)
_c_(35741, _n_(35740, "print", lambda: print), 'Sort along the first axis: ')
_l_(35742)
x = _c_(35746, _a_(35744, _n_(35743, "np", lambda: np), "sort"), _n_(35745, "a", lambda: a), axis=0)
_l_(35747)
_c_(35750, _n_(35748, "print", lambda: print), _n_(35749, "x", lambda: x))
_l_(35751)
_c_(35753, _n_(35752, "print", lambda: print), 'Sort along the last axis: ')
_l_(35754)
y = _c_(35758, _a_(35756, _n_(35755, "np", lambda: np), "sort"), _n_(35757, "x", lambda: x), axis=1)
_l_(35759)
_c_(35762, _n_(35760, "print", lambda: print), _n_(35761, "y", lambda: y))
_l_(35763)