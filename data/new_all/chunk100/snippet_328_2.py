# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(32826)

except ImportError:
    pass
_c_(32828, _n_(32827, "print", lambda: print), 'Original array: ')
_l_(32829)
_c_(32832, _n_(32830, "print", lambda: print), _n_(32831, "x", lambda: x))
_l_(32833)
_c_(32835, _n_(32834, "print", lambda: print), 'Cumulative sum of the elements along a given axis:')
_l_(32836)
r = _c_(32840, _a_(32838, _n_(32837, "np", lambda: np), "cumsum"), _n_(32839, "x", lambda: x))
_l_(32841)
_c_(32844, _n_(32842, "print", lambda: print), _n_(32843, "r", lambda: r))
_l_(32845)
_c_(32847, _n_(32846, "print", lambda: print), '\nSum over rows for each of the 3 columns:')
_l_(32848)
r = _c_(32852, _a_(32850, _n_(32849, "np", lambda: np), "cumsum"), _n_(32851, "x", lambda: x), axis=0)
_l_(32853)
_c_(32856, _n_(32854, "print", lambda: print), _n_(32855, "r", lambda: r))
_l_(32857)
_c_(32859, _n_(32858, "print", lambda: print), '\nSum over columns for each of the 2 rows:')
_l_(32860)
r = _c_(32864, _a_(32862, _n_(32861, "np", lambda: np), "cumsum"), _n_(32863, "x", lambda: x), axis=1)
_l_(32865)
_c_(32868, _n_(32866, "print", lambda: print), _n_(32867, "r", lambda: r))
_l_(32869)