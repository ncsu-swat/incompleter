# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(58844)

except ImportError:
    pass
x = _c_(58847, _a_(58846, _n_(58845, "np", lambda: np), "array"), [1 + 2j, 3 + 4j])
_l_(58848)
_c_(58850, _n_(58849, "print", lambda: print), 'First array:')
_l_(58851)
_c_(58854, _n_(58852, "print", lambda: print), _n_(58853, "x", lambda: x))
_l_(58855)
_c_(58857, _n_(58856, "print", lambda: print), 'Second array:')
_l_(58858)
_c_(58861, _n_(58859, "print", lambda: print), _n_(58860, "y", lambda: y))
_l_(58862)
z = _c_(58867, _a_(58864, _n_(58863, "np", lambda: np), "vdot"), _n_(58865, "x", lambda: x), _n_(58866, "y", lambda: y))
_l_(58868)
_c_(58870, _n_(58869, "print", lambda: print), 'Product of above two arrays:')
_l_(58871)
_c_(58874, _n_(58872, "print", lambda: print), _n_(58873, "z", lambda: z))
_l_(58875)