# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(64490)

except ImportError:
    pass
_c_(64492, _n_(64491, "print", lambda: print), 'One dimensional array:')
_l_(64493)
_c_(64496, _n_(64494, "print", lambda: print), _n_(64495, "x", lambda: x))
_l_(64497)
y = _c_(64502, _a_(64501, _c_(64500, _a_(64499, _n_(64498, "np", lambda: np), "arange"), 8), "reshape"), 2, 4)
_l_(64503)
_c_(64505, _n_(64504, "print", lambda: print), 'Two dimensional array:')
_l_(64506)
_c_(64509, _n_(64507, "print", lambda: print), _n_(64508, "y", lambda: y))
_l_(64510)
for (a, b) in _c_(64515, _a_(64512, _n_(64511, "np", lambda: np), "nditer"), [_n_(64513, "x", lambda: x), _n_(64514, "y", lambda: y)]):
    _l_(64521)

    _c_(64519, _n_(64516, "print", lambda: print), '%d:%d' % (_n_(64517, "a", lambda: a), _n_(64518, "b", lambda: b)))
    _l_(64520)