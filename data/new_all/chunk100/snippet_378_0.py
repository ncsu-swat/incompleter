# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(37672)

except ImportError:
    pass
_c_(37674, _n_(37673, "print", lambda: print), 'Original array:')
_l_(37675)
_c_(37678, _n_(37676, "print", lambda: print), _n_(37677, "x", lambda: x))
_l_(37679)
_c_(37681, _n_(37680, "print", lambda: print), 'Sum of all elements:')
_l_(37682)
_c_(37688, _n_(37683, "print", lambda: print), _c_(37687, _a_(37685, _n_(37684, "np", lambda: np), "sum"), _n_(37686, "x", lambda: x)))
_l_(37689)
_c_(37691, _n_(37690, "print", lambda: print), 'Sum of each column:')
_l_(37692)
_c_(37698, _n_(37693, "print", lambda: print), _c_(37697, _a_(37695, _n_(37694, "np", lambda: np), "sum"), _n_(37696, "x", lambda: x), axis=0))
_l_(37699)
_c_(37701, _n_(37700, "print", lambda: print), 'Sum of each row:')
_l_(37702)
_c_(37708, _n_(37703, "print", lambda: print), _c_(37707, _a_(37705, _n_(37704, "np", lambda: np), "sum"), _n_(37706, "x", lambda: x), axis=1))
_l_(37709)