# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(41931)

except ImportError:
    pass
p = [[1, 0], [0, 1]]
_l_(41932)
q = [[1, 2], [3, 4]]
_l_(41933)
_c_(41935, _n_(41934, "print", lambda: print), 'original matrix:')
_l_(41936)
_c_(41939, _n_(41937, "print", lambda: print), _n_(41938, "p", lambda: p))
_l_(41940)
_c_(41943, _n_(41941, "print", lambda: print), _n_(41942, "q", lambda: q))
_l_(41944)
result1 = _c_(41949, _a_(41946, _n_(41945, "np", lambda: np), "cross"), _n_(41947, "p", lambda: p), _n_(41948, "q", lambda: q))
_l_(41950)
_c_(41952, _n_(41951, "print", lambda: print), 'cross product of the said two vectors(p, q):')
_l_(41953)
_c_(41956, _n_(41954, "print", lambda: print), _n_(41955, "result1", lambda: result1))
_l_(41957)
_c_(41959, _n_(41958, "print", lambda: print), 'cross product of the said two vectors(q, p):')
_l_(41960)
_c_(41963, _n_(41961, "print", lambda: print), _n_(41962, "result2", lambda: result2))
_l_(41964)