# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(87866)

except ImportError:
    pass
_c_(87868, _n_(87867, "print", lambda: print), 'Original array:')
_l_(87869)
_c_(87872, _n_(87870, "print", lambda: print), _n_(87871, "nums", lambda: nums))
_l_(87873)
_c_(87875, _n_(87874, "print", lambda: print), '\nIncrease the number of items (10 edge elements) shown by the print statement:')
_l_(87876)
_c_(87879, _a_(87878, _n_(87877, "np", lambda: np), "set_printoptions"), edgeitems=10)
_l_(87880)
_c_(87883, _n_(87881, "print", lambda: print), _n_(87882, "nums", lambda: nums))
_l_(87884)