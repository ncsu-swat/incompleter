# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(102225)

except ImportError:
    pass
y = _c_(102228, _a_(102227, _n_(102226, "np", lambda: np), "array"), [2, 4, 5])
_l_(102229)
_c_(102231, _n_(102230, "print", lambda: print), '\nOriginal array1:')
_l_(102232)
_c_(102235, _n_(102233, "print", lambda: print), _n_(102234, "x", lambda: x))
_l_(102236)
_c_(102238, _n_(102237, "print", lambda: print), '\nOriginal array1:')
_l_(102239)
_c_(102242, _n_(102240, "print", lambda: print), _n_(102241, "y", lambda: y))
_l_(102243)
_c_(102250, _n_(102244, "print", lambda: print), '\nCross-correlation of the said arrays:\n', _c_(102249, _a_(102246, _n_(102245, "np", lambda: np), "cov"), _n_(102247, "x", lambda: x), _n_(102248, "y", lambda: y)))
_l_(102251)