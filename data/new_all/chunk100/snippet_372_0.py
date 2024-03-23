# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(36804)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(36806)

except ImportError:
    pass
np_array = _c_(36810, _a_(36809, _a_(36808, _n_(36807, "np", lambda: np), "random"), "rand"), 12, 3)
_l_(36811)
_c_(36813, _n_(36812, "print", lambda: print), 'Original Numpy array:')
_l_(36814)
_c_(36817, _n_(36815, "print", lambda: print), _n_(36816, "np_array", lambda: np_array))
_l_(36818)
_c_(36823, _n_(36819, "print", lambda: print), 'Type: ', _c_(36822, _n_(36820, "type", lambda: type), _n_(36821, "np_array", lambda: np_array)))
_l_(36824)
_c_(36826, _n_(36825, "print", lambda: print), "\nPanda's DataFrame: ")
_l_(36827)
_c_(36830, _n_(36828, "print", lambda: print), _n_(36829, "df", lambda: df))
_l_(36831)
_c_(36836, _n_(36832, "print", lambda: print), 'Type: ', _c_(36835, _n_(36833, "type", lambda: type), _n_(36834, "df", lambda: df)))
_l_(36837)