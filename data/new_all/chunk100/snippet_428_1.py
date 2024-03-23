# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(41851)

except ImportError:
    pass
q = [[1, 2], [3, 4]]
_l_(41852)
_c_(41854, _n_(41853, "print", lambda: print), 'original matrix:')
_l_(41855)
_c_(41858, _n_(41856, "print", lambda: print), _n_(41857, "p", lambda: p))
_l_(41859)
_c_(41862, _n_(41860, "print", lambda: print), _n_(41861, "q", lambda: q))
_l_(41863)
result1 = _c_(41868, _a_(41865, _n_(41864, "np", lambda: np), "cross"), _n_(41866, "p", lambda: p), _n_(41867, "q", lambda: q))
_l_(41869)
result2 = _c_(41874, _a_(41871, _n_(41870, "np", lambda: np), "cross"), _n_(41872, "q", lambda: q), _n_(41873, "p", lambda: p))
_l_(41875)
_c_(41877, _n_(41876, "print", lambda: print), 'cross product of the said two vectors(p, q):')
_l_(41878)
_c_(41881, _n_(41879, "print", lambda: print), _n_(41880, "result1", lambda: result1))
_l_(41882)
_c_(41884, _n_(41883, "print", lambda: print), 'cross product of the said two vectors(q, p):')
_l_(41885)
_c_(41888, _n_(41886, "print", lambda: print), _n_(41887, "result2", lambda: result2))
_l_(41889)