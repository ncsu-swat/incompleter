# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(115766)

except ImportError:
    pass
p = [[1, 0], [0, 1]]
_l_(115767)
q = [[1, 2], [3, 4]]
_l_(115768)
_c_(115770, _n_(115769, "print", lambda: print), 'original matrix:')
_l_(115771)
_c_(115774, _n_(115772, "print", lambda: print), _n_(115773, "p", lambda: p))
_l_(115775)
_c_(115778, _n_(115776, "print", lambda: print), _n_(115777, "q", lambda: q))
_l_(115779)
result2 = _c_(115784, _a_(115781, _n_(115780, "np", lambda: np), "cross"), _n_(115782, "q", lambda: q), _n_(115783, "p", lambda: p))
_l_(115785)
_c_(115787, _n_(115786, "print", lambda: print), 'cross product of the said two vectors(p, q):')
_l_(115788)
_c_(115791, _n_(115789, "print", lambda: print), _n_(115790, "result1", lambda: result1))
_l_(115792)
_c_(115794, _n_(115793, "print", lambda: print), 'cross product of the said two vectors(q, p):')
_l_(115795)
_c_(115798, _n_(115796, "print", lambda: print), _n_(115797, "result2", lambda: result2))
_l_(115799)