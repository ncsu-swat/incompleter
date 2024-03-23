# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(79757)

except ImportError:
    pass
_c_(79759, _n_(79758, "print", lambda: print), '\nTest element-wise for finiteness (not infinity or not Not a Number):')
_l_(79760)
_c_(79765, _n_(79761, "print", lambda: print), _c_(79764, _a_(79763, _n_(79762, "np", lambda: np), "isfinite"), 1))
_l_(79766)
_c_(79771, _n_(79767, "print", lambda: print), _c_(79770, _a_(79769, _n_(79768, "np", lambda: np), "isfinite"), 0))
_l_(79772)
_c_(79779, _n_(79773, "print", lambda: print), _c_(79778, _a_(79775, _n_(79774, "np", lambda: np), "isfinite"), _a_(79777, _n_(79776, "np", lambda: np), "nan")))
_l_(79780)
_c_(79782, _n_(79781, "print", lambda: print), '\nTest element-wise for positive or negative infinity:')
_l_(79783)
_c_(79790, _n_(79784, "print", lambda: print), _c_(79789, _a_(79786, _n_(79785, "np", lambda: np), "isinf"), _a_(79788, _n_(79787, "np", lambda: np), "inf")))
_l_(79791)
_c_(79798, _n_(79792, "print", lambda: print), _c_(79797, _a_(79794, _n_(79793, "np", lambda: np), "isinf"), _a_(79796, _n_(79795, "np", lambda: np), "nan")))
_l_(79799)
_c_(79806, _n_(79800, "print", lambda: print), _c_(79805, _a_(79802, _n_(79801, "np", lambda: np), "isinf"), _a_(79804, _n_(79803, "np", lambda: np), "NINF")))
_l_(79807)
_c_(79809, _n_(79808, "print", lambda: print), 'Test element-wise for NaN:')
_l_(79810)
_c_(79821, _n_(79811, "print", lambda: print), _c_(79820, _a_(79813, _n_(79812, "np", lambda: np), "isnan"), [_c_(79816, _a_(79815, _n_(79814, "np", lambda: np), "log"), -1.0), 1.0, _c_(79819, _a_(79818, _n_(79817, "np", lambda: np), "log"), 0)]))
_l_(79822)
_c_(79824, _n_(79823, "print", lambda: print), 'Test element-wise for NaT (not a time):')
_l_(79825)
_c_(79833, _n_(79826, "print", lambda: print), _c_(79832, _a_(79828, _n_(79827, "np", lambda: np), "isnat"), _c_(79831, _a_(79830, _n_(79829, "np", lambda: np), "array"), ['NaT', '2016-01-01'], dtype='datetime64[ns]')))
_l_(79834)
_c_(79836, _n_(79835, "print", lambda: print), 'Test element-wise for negative infinity:')
_l_(79837)
x = _c_(79844, _a_(79839, _n_(79838, "np", lambda: np), "array"), [-_a_(79841, _n_(79840, "np", lambda: np), "inf"), 0.0, _a_(79843, _n_(79842, "np", lambda: np), "inf")])
_l_(79845)
y = _c_(79848, _a_(79847, _n_(79846, "np", lambda: np), "array"), [2, 2, 2])
_l_(79849)
_c_(79856, _n_(79850, "print", lambda: print), _c_(79855, _a_(79852, _n_(79851, "np", lambda: np), "isneginf"), _n_(79853, "x", lambda: x), _n_(79854, "y", lambda: y)))
_l_(79857)
_c_(79859, _n_(79858, "print", lambda: print), 'Test element-wise for positive infinity:')
_l_(79860)
y = _c_(79863, _a_(79862, _n_(79861, "np", lambda: np), "array"), [2, 2, 2])
_l_(79864)
_c_(79871, _n_(79865, "print", lambda: print), _c_(79870, _a_(79867, _n_(79866, "np", lambda: np), "isposinf"), _n_(79868, "x", lambda: x), _n_(79869, "y", lambda: y)))
_l_(79872)