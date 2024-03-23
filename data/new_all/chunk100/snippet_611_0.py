# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from scipy.spatial import distance
    _l_(64546)

except ImportError:
    pass
p1 = (1, 2, 3)
_l_(64547)
d = _c_(64552, _a_(64549, _n_(64548, "distance", lambda: distance), "euclidean"), _n_(64550, "p1", lambda: p1), _n_(64551, "p2", lambda: p2))
_l_(64553)
_c_(64556, _n_(64554, "print", lambda: print), 'Euclidean distance: ', _n_(64555, "d", lambda: d))
_l_(64557)