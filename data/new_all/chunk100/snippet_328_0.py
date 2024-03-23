# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(32738)

except ImportError:
    pass
x = _c_(32741, _a_(32740, _n_(32739, "np", lambda: np), "array"), [[1, 2, 3], [4, 5, 6]])
_l_(32742)
_c_(32744, _n_(32743, "print", lambda: print), 'Original array: ')
_l_(32745)
_c_(32748, _n_(32746, "print", lambda: print), _n_(32747, "x", lambda: x))
_l_(32749)
_c_(32751, _n_(32750, "print", lambda: print), 'Cumulative sum of the elements along a given axis:')
_l_(32752)
r = _c_(32756, _a_(32754, _n_(32753, "np", lambda: np), "cumsum"), _n_(32755, "x", lambda: x))
_l_(32757)
_c_(32760, _n_(32758, "print", lambda: print), _n_(32759, "r", lambda: r))
_l_(32761)
_c_(32763, _n_(32762, "print", lambda: print), '\nSum over rows for each of the 3 columns:')
_l_(32764)
_c_(32767, _n_(32765, "print", lambda: print), _n_(32766, "r", lambda: r))
_l_(32768)
_c_(32770, _n_(32769, "print", lambda: print), '\nSum over columns for each of the 2 rows:')
_l_(32771)
r = _c_(32775, _a_(32773, _n_(32772, "np", lambda: np), "cumsum"), _n_(32774, "x", lambda: x), axis=1)
_l_(32776)
_c_(32779, _n_(32777, "print", lambda: print), _n_(32778, "r", lambda: r))
_l_(32780)