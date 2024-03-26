# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(119786)

except ImportError:
    pass
r1 = _c_(119790, _a_(119788, _n_(119787, "np", lambda: np), "radians"), _n_(119789, "x", lambda: x))
_l_(119791)
r2 = _c_(119795, _a_(119793, _n_(119792, "np", lambda: np), "deg2rad"), _n_(119794, "x", lambda: x))
_l_(119796)
assert _c_(119801, _a_(119798, _n_(119797, "np", lambda: np), "array_equiv"), _n_(119799, "r1", lambda: r1), _n_(119800, "r2", lambda: r2))
_l_(119802)
_c_(119805, _n_(119803, "print", lambda: print), _n_(119804, "r1", lambda: r1))
_l_(119806)