# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(42009)

except ImportError:
    pass
p = _c_(42012, _a_(42011, _n_(42010, "np", lambda: np), "array"), [[0, 0, 0], [1, 2, 3], [4, 5, 6]])
_l_(42013)
q = _c_(42016, _a_(42015, _n_(42014, "np", lambda: np), "array"), [10, 11, 12])
_l_(42017)
_c_(42019, _n_(42018, "print", lambda: print), 'Original arrays:')
_l_(42020)
_c_(42022, _n_(42021, "print", lambda: print), 'Array-1')
_l_(42023)
_c_(42026, _n_(42024, "print", lambda: print), _n_(42025, "p", lambda: p))
_l_(42027)
_c_(42029, _n_(42028, "print", lambda: print), 'Array-2')
_l_(42030)
_c_(42033, _n_(42031, "print", lambda: print), _n_(42032, "q", lambda: q))
_l_(42034)
_c_(42036, _n_(42035, "print", lambda: print), '\nNew Array:')
_l_(42037)
_c_(42040, _n_(42038, "print", lambda: print), _n_(42039, "new_array1", lambda: new_array1))
_l_(42041)