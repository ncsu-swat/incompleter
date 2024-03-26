# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(118746)

except ImportError:
    pass
_c_(118748, _n_(118747, "print", lambda: print), 'Original array:')
_l_(118749)
_c_(118752, _n_(118750, "print", lambda: print), _n_(118751, "a", lambda: a))
_l_(118753)
L = _c_(118758, _a_(118756, _a_(118755, _n_(118754, "np", lambda: np), "linalg"), "cholesky"), _n_(118757, "a", lambda: a))
_l_(118759)
_c_(118761, _n_(118760, "print", lambda: print), 'Lower-trianglular L in the Cholesky decomposition of the said array:')
_l_(118762)
_c_(118765, _n_(118763, "print", lambda: print), _n_(118764, "L", lambda: L))
_l_(118766)