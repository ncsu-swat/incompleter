# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(93919)

except ImportError:
    pass
x = [1, 2, 3]
_l_(93920)
z = [6, 7]
_l_(93921)
_c_(93923, _n_(93922, "print", lambda: print), 'Original arrays:')
_l_(93924)
_c_(93926, _n_(93925, "print", lambda: print), 'Array-1')
_l_(93927)
_c_(93930, _n_(93928, "print", lambda: print), _n_(93929, "x", lambda: x))
_l_(93931)
_c_(93933, _n_(93932, "print", lambda: print), 'Array-2')
_l_(93934)
_c_(93937, _n_(93935, "print", lambda: print), _n_(93936, "y", lambda: y))
_l_(93938)
_c_(93940, _n_(93939, "print", lambda: print), 'Array-3')
_l_(93941)
_c_(93944, _n_(93942, "print", lambda: print), _n_(93943, "z", lambda: z))
_l_(93945)
new_array = _c_(93957, _a_(93956, _a_(93955, _c_(93954, _a_(93947, _n_(93946, "np", lambda: np), "array"), _c_(93953, _a_(93949, _n_(93948, "np", lambda: np), "meshgrid"), _n_(93950, "x", lambda: x), _n_(93951, "y", lambda: y), _n_(93952, "z", lambda: z))), "T"), "reshape"), -1, 3)
_l_(93958)
_c_(93960, _n_(93959, "print", lambda: print), 'Combine array:')
_l_(93961)
_c_(93964, _n_(93962, "print", lambda: print), _n_(93963, "new_array", lambda: new_array))
_l_(93965)