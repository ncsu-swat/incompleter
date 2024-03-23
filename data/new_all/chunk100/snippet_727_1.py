# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(73707)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(73709)

except ImportError:
    pass
np_array = _c_(73712, _a_(73711, _n_(73710, "np", lambda: np), "array"), [10, 20, 30, 40, 50])
_l_(73713)
_c_(73715, _n_(73714, "print", lambda: print), 'NumPy array:')
_l_(73716)
_c_(73719, _n_(73717, "print", lambda: print), _n_(73718, "np_array", lambda: np_array))
_l_(73720)
_c_(73722, _n_(73721, "print", lambda: print), 'Converted Pandas series:')
_l_(73723)
_c_(73726, _n_(73724, "print", lambda: print), _n_(73725, "new_series", lambda: new_series))
_l_(73727)