# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(40024)

except ImportError:
    pass
nums = _c_(40028, _a_(40027, _a_(40026, _n_(40025, "np", lambda: np), "random"), "random"), (8, 8, 3))
_l_(40029)
_c_(40031, _n_(40030, "print", lambda: print), 'Original array:')
_l_(40032)
_c_(40035, _n_(40033, "print", lambda: print), _n_(40034, "nums", lambda: nums))
_l_(40036)
_c_(40038, _n_(40037, "print", lambda: print), '\nExtract array of shape (6,6,3) from the said array:')
_l_(40039)
_c_(40042, _n_(40040, "print", lambda: print), _n_(40041, "new_nums", lambda: new_nums))
_l_(40043)