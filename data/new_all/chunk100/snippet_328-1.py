# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(110653)

except ImportError:
    pass
_c_(110655, _n_(110654, "print", lambda: print), 'Original array: ')
_l_(110656)
_c_(110659, _n_(110657, "print", lambda: print), _n_(110658, "x", lambda: x))
_l_(110660)
_c_(110662, _n_(110661, "print", lambda: print), 'Cumulative sum of the elements along a given axis:')
_l_(110663)
r = _c_(110667, _a_(110665, _n_(110664, "np", lambda: np), "cumsum"), _n_(110666, "x", lambda: x))
_l_(110668)
_c_(110671, _n_(110669, "print", lambda: print), _n_(110670, "r", lambda: r))
_l_(110672)
_c_(110674, _n_(110673, "print", lambda: print), '\nSum over rows for each of the 3 columns:')
_l_(110675)
r = _c_(110679, _a_(110677, _n_(110676, "np", lambda: np), "cumsum"), _n_(110678, "x", lambda: x), axis=0)
_l_(110680)
_c_(110683, _n_(110681, "print", lambda: print), _n_(110682, "r", lambda: r))
_l_(110684)
_c_(110686, _n_(110685, "print", lambda: print), '\nSum over columns for each of the 2 rows:')
_l_(110687)
r = _c_(110691, _a_(110689, _n_(110688, "np", lambda: np), "cumsum"), _n_(110690, "x", lambda: x), axis=1)
_l_(110692)
_c_(110695, _n_(110693, "print", lambda: print), _n_(110694, "r", lambda: r))
_l_(110696)