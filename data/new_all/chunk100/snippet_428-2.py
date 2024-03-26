# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(115841)

except ImportError:
    pass
p = [[1, 0], [0, 1]]
_l_(115842)
q = [[1, 2], [3, 4]]
_l_(115843)
_c_(115845, _n_(115844, "print", lambda: print), 'original matrix:')
_l_(115846)
_c_(115849, _n_(115847, "print", lambda: print), _n_(115848, "p", lambda: p))
_l_(115850)
_c_(115853, _n_(115851, "print", lambda: print), _n_(115852, "q", lambda: q))
_l_(115854)
result1 = _c_(115859, _a_(115856, _n_(115855, "np", lambda: np), "cross"), _n_(115857, "p", lambda: p), _n_(115858, "q", lambda: q))
_l_(115860)
_c_(115862, _n_(115861, "print", lambda: print), 'cross product of the said two vectors(p, q):')
_l_(115863)
_c_(115866, _n_(115864, "print", lambda: print), _n_(115865, "result1", lambda: result1))
_l_(115867)
_c_(115869, _n_(115868, "print", lambda: print), 'cross product of the said two vectors(q, p):')
_l_(115870)
_c_(115873, _n_(115871, "print", lambda: print), _n_(115872, "result2", lambda: result2))
_l_(115874)