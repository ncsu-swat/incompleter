# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(33500)

except ImportError:
    pass
x = _c_(33504, _a_(33503, _a_(33502, _n_(33501, "np", lambda: np), "random"), "uniform"), 1, 12, 5)
_l_(33505)
n = _a_(33507, _n_(33506, "x", lambda: x), "flat")[_c_(33514, _a_(33513, _c_(33512, _a_(33509, _n_(33508, "np", lambda: np), "abs"), _n_(33510, "x", lambda: x) - _n_(33511, "v", lambda: v)), "argmin"))]
_l_(33515)
_c_(33518, _n_(33516, "print", lambda: print), _n_(33517, "n", lambda: n))
_l_(33519)