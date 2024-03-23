# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(71842)

except ImportError:
    pass
_c_(71844, _n_(71843, "print", lambda: print), 'Original matrix:')
_l_(71845)
_c_(71848, _n_(71846, "print", lambda: print), 'a\n', _n_(71847, "m", lambda: m))
_l_(71849)
(w, v) = _c_(71854, _a_(71852, _a_(71851, _n_(71850, "np", lambda: np), "linalg"), "eig"), _n_(71853, "m", lambda: m))
_l_(71855)
_c_(71858, _n_(71856, "print", lambda: print), 'Eigenvalues of the said matrix', _n_(71857, "w", lambda: w))
_l_(71859)
_c_(71862, _n_(71860, "print", lambda: print), 'Eigenvectors of the said matrix', _n_(71861, "v", lambda: v))
_l_(71863)