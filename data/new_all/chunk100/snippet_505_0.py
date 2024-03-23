# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(52323)

except ImportError:
    pass
_c_(52325, _n_(52324, "print", lambda: print), 'Original array:')
_l_(52326)
_c_(52329, _n_(52327, "print", lambda: print), _n_(52328, "a", lambda: a))
_l_(52330)
(q, r) = _c_(52335, _a_(52333, _a_(52332, _n_(52331, "np", lambda: np), "linalg"), "qr"), _n_(52334, "a", lambda: a))
_l_(52336)
_c_(52338, _n_(52337, "print", lambda: print), 'qr factorization of the said array:')
_l_(52339)
_c_(52343, _n_(52340, "print", lambda: print), 'q=\n', _n_(52341, "q", lambda: q), '\nr=\n', _n_(52342, "r", lambda: r))
_l_(52344)