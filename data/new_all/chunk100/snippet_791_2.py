# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(79874)

except ImportError:
    pass
_c_(79876, _n_(79875, "print", lambda: print), '\nTest element-wise for finiteness (not infinity or not Not a Number):')
_l_(79877)
_c_(79882, _n_(79878, "print", lambda: print), _c_(79881, _a_(79880, _n_(79879, "np", lambda: np), "isfinite"), 1))
_l_(79883)
_c_(79888, _n_(79884, "print", lambda: print), _c_(79887, _a_(79886, _n_(79885, "np", lambda: np), "isfinite"), 0))
_l_(79889)
_c_(79896, _n_(79890, "print", lambda: print), _c_(79895, _a_(79892, _n_(79891, "np", lambda: np), "isfinite"), _a_(79894, _n_(79893, "np", lambda: np), "nan")))
_l_(79897)
_c_(79899, _n_(79898, "print", lambda: print), '\nTest element-wise for positive or negative infinity:')
_l_(79900)
_c_(79907, _n_(79901, "print", lambda: print), _c_(79906, _a_(79903, _n_(79902, "np", lambda: np), "isinf"), _a_(79905, _n_(79904, "np", lambda: np), "inf")))
_l_(79908)
_c_(79915, _n_(79909, "print", lambda: print), _c_(79914, _a_(79911, _n_(79910, "np", lambda: np), "isinf"), _a_(79913, _n_(79912, "np", lambda: np), "nan")))
_l_(79916)
_c_(79923, _n_(79917, "print", lambda: print), _c_(79922, _a_(79919, _n_(79918, "np", lambda: np), "isinf"), _a_(79921, _n_(79920, "np", lambda: np), "NINF")))
_l_(79924)
_c_(79926, _n_(79925, "print", lambda: print), 'Test element-wise for NaN:')
_l_(79927)
_c_(79938, _n_(79928, "print", lambda: print), _c_(79937, _a_(79930, _n_(79929, "np", lambda: np), "isnan"), [_c_(79933, _a_(79932, _n_(79931, "np", lambda: np), "log"), -1.0), 1.0, _c_(79936, _a_(79935, _n_(79934, "np", lambda: np), "log"), 0)]))
_l_(79939)
_c_(79941, _n_(79940, "print", lambda: print), 'Test element-wise for NaT (not a time):')
_l_(79942)
_c_(79950, _n_(79943, "print", lambda: print), _c_(79949, _a_(79945, _n_(79944, "np", lambda: np), "isnat"), _c_(79948, _a_(79947, _n_(79946, "np", lambda: np), "array"), ['NaT', '2016-01-01'], dtype='datetime64[ns]')))
_l_(79951)
_c_(79953, _n_(79952, "print", lambda: print), 'Test element-wise for negative infinity:')
_l_(79954)
x = _c_(79961, _a_(79956, _n_(79955, "np", lambda: np), "array"), [-_a_(79958, _n_(79957, "np", lambda: np), "inf"), 0.0, _a_(79960, _n_(79959, "np", lambda: np), "inf")])
_l_(79962)
_c_(79969, _n_(79963, "print", lambda: print), _c_(79968, _a_(79965, _n_(79964, "np", lambda: np), "isneginf"), _n_(79966, "x", lambda: x), _n_(79967, "y", lambda: y)))
_l_(79970)
_c_(79972, _n_(79971, "print", lambda: print), 'Test element-wise for positive infinity:')
_l_(79973)
x = _c_(79980, _a_(79975, _n_(79974, "np", lambda: np), "array"), [-_a_(79977, _n_(79976, "np", lambda: np), "inf"), 0.0, _a_(79979, _n_(79978, "np", lambda: np), "inf")])
_l_(79981)
y = _c_(79984, _a_(79983, _n_(79982, "np", lambda: np), "array"), [2, 2, 2])
_l_(79985)
_c_(79992, _n_(79986, "print", lambda: print), _c_(79991, _a_(79988, _n_(79987, "np", lambda: np), "isposinf"), _n_(79989, "x", lambda: x), _n_(79990, "y", lambda: y)))
_l_(79993)