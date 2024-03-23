# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(40095)

except ImportError:
    pass
_c_(40097, _n_(40096, "print", lambda: print), 'Original array:')
_l_(40098)
_c_(40101, _n_(40099, "print", lambda: print), _n_(40100, "a", lambda: a))
_l_(40102)
(U, s, V) = _c_(40107, _a_(40105, _a_(40104, _n_(40103, "np", lambda: np), "linalg"), "svd"), _n_(40106, "a", lambda: a), full_matrices=False)
_l_(40108)
(q, r) = _c_(40113, _a_(40111, _a_(40110, _n_(40109, "np", lambda: np), "linalg"), "qr"), _n_(40112, "a", lambda: a))
_l_(40114)
_c_(40116, _n_(40115, "print", lambda: print), 'Factor of a given array  by Singular Value Decomposition:')
_l_(40117)
_c_(40122, _n_(40118, "print", lambda: print), 'U=\n', _n_(40119, "U", lambda: U), '\ns=\n', _n_(40120, "s", lambda: s), '\nV=\n', _n_(40121, "V", lambda: V))
_l_(40123)