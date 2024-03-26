# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(106198)

except ImportError:
    pass
_c_(106200, _n_(106199, "print", lambda: print), '\nOriginal arrays:')
_l_(106201)
x = _c_(106204, _a_(106203, _n_(106202, "np", lambda: np), "array"), (1, 2, 3))
_l_(106205)
y = _c_(106208, _a_(106207, _n_(106206, "np", lambda: np), "array"), (2, 3, 4))
_l_(106209)
_c_(106211, _n_(106210, "print", lambda: print), 'Array-1')
_l_(106212)
_c_(106215, _n_(106213, "print", lambda: print), _n_(106214, "x", lambda: x))
_l_(106216)
_c_(106218, _n_(106217, "print", lambda: print), 'Array-2')
_l_(106219)
_c_(106222, _n_(106220, "print", lambda: print), _n_(106221, "y", lambda: y))
_l_(106223)
_c_(106225, _n_(106224, "print", lambda: print), '\nStack 1-D arrays as rows wise:')
_l_(106226)
_c_(106229, _n_(106227, "print", lambda: print), _n_(106228, "new_array", lambda: new_array))
_l_(106230)