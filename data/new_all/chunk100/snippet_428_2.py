# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(41891)

except ImportError:
    pass
p = [[1, 0], [0, 1]]
_l_(41892)
_c_(41894, _n_(41893, "print", lambda: print), 'original matrix:')
_l_(41895)
_c_(41898, _n_(41896, "print", lambda: print), _n_(41897, "p", lambda: p))
_l_(41899)
_c_(41902, _n_(41900, "print", lambda: print), _n_(41901, "q", lambda: q))
_l_(41903)
result1 = _c_(41908, _a_(41905, _n_(41904, "np", lambda: np), "cross"), _n_(41906, "p", lambda: p), _n_(41907, "q", lambda: q))
_l_(41909)
result2 = _c_(41914, _a_(41911, _n_(41910, "np", lambda: np), "cross"), _n_(41912, "q", lambda: q), _n_(41913, "p", lambda: p))
_l_(41915)
_c_(41917, _n_(41916, "print", lambda: print), 'cross product of the said two vectors(p, q):')
_l_(41918)
_c_(41921, _n_(41919, "print", lambda: print), _n_(41920, "result1", lambda: result1))
_l_(41922)
_c_(41924, _n_(41923, "print", lambda: print), 'cross product of the said two vectors(q, p):')
_l_(41925)
_c_(41928, _n_(41926, "print", lambda: print), _n_(41927, "result2", lambda: result2))
_l_(41929)