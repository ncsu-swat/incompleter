# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(32871)

except ImportError:
    pass
x = _c_(32874, _a_(32873, _n_(32872, "np", lambda: np), "array"), [[1, 2, 3], [4, 5, 6]])
_l_(32875)
_c_(32877, _n_(32876, "print", lambda: print), 'Original array: ')
_l_(32878)
_c_(32881, _n_(32879, "print", lambda: print), _n_(32880, "x", lambda: x))
_l_(32882)
_c_(32884, _n_(32883, "print", lambda: print), 'Cumulative sum of the elements along a given axis:')
_l_(32885)
r = _c_(32889, _a_(32887, _n_(32886, "np", lambda: np), "cumsum"), _n_(32888, "x", lambda: x))
_l_(32890)
_c_(32893, _n_(32891, "print", lambda: print), _n_(32892, "r", lambda: r))
_l_(32894)
_c_(32896, _n_(32895, "print", lambda: print), '\nSum over rows for each of the 3 columns:')
_l_(32897)
r = _c_(32901, _a_(32899, _n_(32898, "np", lambda: np), "cumsum"), _n_(32900, "x", lambda: x), axis=0)
_l_(32902)
_c_(32905, _n_(32903, "print", lambda: print), _n_(32904, "r", lambda: r))
_l_(32906)
_c_(32908, _n_(32907, "print", lambda: print), '\nSum over columns for each of the 2 rows:')
_l_(32909)
_c_(32912, _n_(32910, "print", lambda: print), _n_(32911, "r", lambda: r))
_l_(32913)