# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(115876)

except ImportError:
    pass
q = [[1, 2], [3, 4]]
_l_(115877)
_c_(115879, _n_(115878, "print", lambda: print), 'original matrix:')
_l_(115880)
_c_(115883, _n_(115881, "print", lambda: print), _n_(115882, "p", lambda: p))
_l_(115884)
_c_(115887, _n_(115885, "print", lambda: print), _n_(115886, "q", lambda: q))
_l_(115888)
result1 = _c_(115893, _a_(115890, _n_(115889, "np", lambda: np), "cross"), _n_(115891, "p", lambda: p), _n_(115892, "q", lambda: q))
_l_(115894)
result2 = _c_(115899, _a_(115896, _n_(115895, "np", lambda: np), "cross"), _n_(115897, "q", lambda: q), _n_(115898, "p", lambda: p))
_l_(115900)
_c_(115902, _n_(115901, "print", lambda: print), 'cross product of the said two vectors(p, q):')
_l_(115903)
_c_(115906, _n_(115904, "print", lambda: print), _n_(115905, "result1", lambda: result1))
_l_(115907)
_c_(115909, _n_(115908, "print", lambda: print), 'cross product of the said two vectors(q, p):')
_l_(115910)
_c_(115913, _n_(115911, "print", lambda: print), _n_(115912, "result2", lambda: result2))
_l_(115914)