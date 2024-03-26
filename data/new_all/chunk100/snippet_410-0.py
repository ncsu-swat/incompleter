# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(114908)

except ImportError:
    pass
_c_(114910, _n_(114909, "print", lambda: print), 'Original array:')
_l_(114911)
_c_(114914, _n_(114912, "print", lambda: print), _n_(114913, "a", lambda: a))
_l_(114915)
U, s, V = _c_(114920, _a_(114918, _a_(114917, _n_(114916, "np", lambda: np), "linalg"), "svd"), _n_(114919, "a", lambda: a), full_matrices=False)
_l_(114921)
q, r = _c_(114926, _a_(114924, _a_(114923, _n_(114922, "np", lambda: np), "linalg"), "qr"), _n_(114925, "a", lambda: a))
_l_(114927)
_c_(114929, _n_(114928, "print", lambda: print), 'Factor of a given array  by Singular Value Decomposition:')
_l_(114930)
_c_(114935, _n_(114931, "print", lambda: print), 'U=\n', _n_(114932, "U", lambda: U), '\ns=\n', _n_(114933, "s", lambda: s), '\nV=\n', _n_(114934, "V", lambda: V))
_l_(114936)