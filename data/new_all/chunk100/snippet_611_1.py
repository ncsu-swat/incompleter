# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from scipy.spatial import distance
    _l_(64559)

except ImportError:
    pass
p2 = (4, 5, 6)
_l_(64560)
d = _c_(64565, _a_(64562, _n_(64561, "distance", lambda: distance), "euclidean"), _n_(64563, "p1", lambda: p1), _n_(64564, "p2", lambda: p2))
_l_(64566)
_c_(64569, _n_(64567, "print", lambda: print), 'Euclidean distance: ', _n_(64568, "d", lambda: d))
_l_(64570)