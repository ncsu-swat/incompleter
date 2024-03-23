# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(93871)

except ImportError:
    pass
y = [4, 5]
_l_(93872)
z = [6, 7]
_l_(93873)
_c_(93875, _n_(93874, "print", lambda: print), 'Original arrays:')
_l_(93876)
_c_(93878, _n_(93877, "print", lambda: print), 'Array-1')
_l_(93879)
_c_(93882, _n_(93880, "print", lambda: print), _n_(93881, "x", lambda: x))
_l_(93883)
_c_(93885, _n_(93884, "print", lambda: print), 'Array-2')
_l_(93886)
_c_(93889, _n_(93887, "print", lambda: print), _n_(93888, "y", lambda: y))
_l_(93890)
_c_(93892, _n_(93891, "print", lambda: print), 'Array-3')
_l_(93893)
_c_(93896, _n_(93894, "print", lambda: print), _n_(93895, "z", lambda: z))
_l_(93897)
new_array = _c_(93909, _a_(93908, _a_(93907, _c_(93906, _a_(93899, _n_(93898, "np", lambda: np), "array"), _c_(93905, _a_(93901, _n_(93900, "np", lambda: np), "meshgrid"), _n_(93902, "x", lambda: x), _n_(93903, "y", lambda: y), _n_(93904, "z", lambda: z))), "T"), "reshape"), -1, 3)
_l_(93910)
_c_(93912, _n_(93911, "print", lambda: print), 'Combine array:')
_l_(93913)
_c_(93916, _n_(93914, "print", lambda: print), _n_(93915, "new_array", lambda: new_array))
_l_(93917)