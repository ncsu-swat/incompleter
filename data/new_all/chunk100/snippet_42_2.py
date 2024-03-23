# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(42076)

except ImportError:
    pass
q = _c_(42079, _a_(42078, _n_(42077, "np", lambda: np), "array"), [10, 11, 12])
_l_(42080)
_c_(42082, _n_(42081, "print", lambda: print), 'Original arrays:')
_l_(42083)
_c_(42085, _n_(42084, "print", lambda: print), 'Array-1')
_l_(42086)
_c_(42089, _n_(42087, "print", lambda: print), _n_(42088, "p", lambda: p))
_l_(42090)
_c_(42092, _n_(42091, "print", lambda: print), 'Array-2')
_l_(42093)
_c_(42096, _n_(42094, "print", lambda: print), _n_(42095, "q", lambda: q))
_l_(42097)
_c_(42099, _n_(42098, "print", lambda: print), '\nNew Array:')
_l_(42100)
new_array1 = _n_(42101, "p", lambda: p) + _n_(42102, "q", lambda: q)
_l_(42103)
_c_(42106, _n_(42104, "print", lambda: print), _n_(42105, "new_array1", lambda: new_array1))
_l_(42107)