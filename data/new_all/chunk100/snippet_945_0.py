# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(94912)

except ImportError:
    pass
_c_(94914, _n_(94913, "print", lambda: print), 'Original array:')
_l_(94915)
_c_(94918, _n_(94916, "print", lambda: print), _n_(94917, "arr1", lambda: arr1))
_l_(94919)
temp = _c_(94928, _a_(94922, _a_(94921, _n_(94920, "np", lambda: np), "ma"), "masked_array"), _n_(94923, "arr1", lambda: arr1), _c_(94927, _a_(94925, _n_(94924, "np", lambda: np), "isnan"), _n_(94926, "arr1", lambda: arr1)))
_l_(94929)
result = _c_(94933, _a_(94931, _n_(94930, "np", lambda: np), "mean"), _n_(94932, "temp", lambda: temp), axis=1)
_l_(94934)
_c_(94936, _n_(94935, "print", lambda: print), 'Averages without NaNs along the said array:')
_l_(94937)
_c_(94944, _n_(94938, "print", lambda: print), _c_(94943, _a_(94940, _n_(94939, "result", lambda: result), "filled"), _a_(94942, _n_(94941, "np", lambda: np), "nan")))
_l_(94945)