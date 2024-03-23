# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(79995)

except ImportError:
    pass
_c_(79997, _n_(79996, "print", lambda: print), '\nTest element-wise for finiteness (not infinity or not Not a Number):')
_l_(79998)
_c_(80003, _n_(79999, "print", lambda: print), _c_(80002, _a_(80001, _n_(80000, "np", lambda: np), "isfinite"), 1))
_l_(80004)
_c_(80009, _n_(80005, "print", lambda: print), _c_(80008, _a_(80007, _n_(80006, "np", lambda: np), "isfinite"), 0))
_l_(80010)
_c_(80017, _n_(80011, "print", lambda: print), _c_(80016, _a_(80013, _n_(80012, "np", lambda: np), "isfinite"), _a_(80015, _n_(80014, "np", lambda: np), "nan")))
_l_(80018)
_c_(80020, _n_(80019, "print", lambda: print), '\nTest element-wise for positive or negative infinity:')
_l_(80021)
_c_(80028, _n_(80022, "print", lambda: print), _c_(80027, _a_(80024, _n_(80023, "np", lambda: np), "isinf"), _a_(80026, _n_(80025, "np", lambda: np), "inf")))
_l_(80029)
_c_(80036, _n_(80030, "print", lambda: print), _c_(80035, _a_(80032, _n_(80031, "np", lambda: np), "isinf"), _a_(80034, _n_(80033, "np", lambda: np), "nan")))
_l_(80037)
_c_(80044, _n_(80038, "print", lambda: print), _c_(80043, _a_(80040, _n_(80039, "np", lambda: np), "isinf"), _a_(80042, _n_(80041, "np", lambda: np), "NINF")))
_l_(80045)
_c_(80047, _n_(80046, "print", lambda: print), 'Test element-wise for NaN:')
_l_(80048)
_c_(80059, _n_(80049, "print", lambda: print), _c_(80058, _a_(80051, _n_(80050, "np", lambda: np), "isnan"), [_c_(80054, _a_(80053, _n_(80052, "np", lambda: np), "log"), -1.0), 1.0, _c_(80057, _a_(80056, _n_(80055, "np", lambda: np), "log"), 0)]))
_l_(80060)
_c_(80062, _n_(80061, "print", lambda: print), 'Test element-wise for NaT (not a time):')
_l_(80063)
_c_(80071, _n_(80064, "print", lambda: print), _c_(80070, _a_(80066, _n_(80065, "np", lambda: np), "isnat"), _c_(80069, _a_(80068, _n_(80067, "np", lambda: np), "array"), ['NaT', '2016-01-01'], dtype='datetime64[ns]')))
_l_(80072)
_c_(80074, _n_(80073, "print", lambda: print), 'Test element-wise for negative infinity:')
_l_(80075)
x = _c_(80082, _a_(80077, _n_(80076, "np", lambda: np), "array"), [-_a_(80079, _n_(80078, "np", lambda: np), "inf"), 0.0, _a_(80081, _n_(80080, "np", lambda: np), "inf")])
_l_(80083)
y = _c_(80086, _a_(80085, _n_(80084, "np", lambda: np), "array"), [2, 2, 2])
_l_(80087)
_c_(80094, _n_(80088, "print", lambda: print), _c_(80093, _a_(80090, _n_(80089, "np", lambda: np), "isneginf"), _n_(80091, "x", lambda: x), _n_(80092, "y", lambda: y)))
_l_(80095)
_c_(80097, _n_(80096, "print", lambda: print), 'Test element-wise for positive infinity:')
_l_(80098)
x = _c_(80105, _a_(80100, _n_(80099, "np", lambda: np), "array"), [-_a_(80102, _n_(80101, "np", lambda: np), "inf"), 0.0, _a_(80104, _n_(80103, "np", lambda: np), "inf")])
_l_(80106)
_c_(80113, _n_(80107, "print", lambda: print), _c_(80112, _a_(80109, _n_(80108, "np", lambda: np), "isposinf"), _n_(80110, "x", lambda: x), _n_(80111, "y", lambda: y)))
_l_(80114)