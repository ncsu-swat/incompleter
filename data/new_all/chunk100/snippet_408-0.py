# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(114776)

except ImportError:
    pass
nums = _c_(114780, _a_(114779, _a_(114778, _n_(114777, "np", lambda: np), "random"), "random"), (8, 8, 3))
_l_(114781)
_c_(114783, _n_(114782, "print", lambda: print), 'Original array:')
_l_(114784)
_c_(114787, _n_(114785, "print", lambda: print), _n_(114786, "nums", lambda: nums))
_l_(114788)
_c_(114790, _n_(114789, "print", lambda: print), '\nExtract array of shape (6,6,3) from the said array:')
_l_(114791)
_c_(114794, _n_(114792, "print", lambda: print), _n_(114793, "new_nums", lambda: new_nums))
_l_(114795)