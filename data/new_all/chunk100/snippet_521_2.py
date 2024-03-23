# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import collections
    _l_(53198)

except ImportError:
    pass
tup1 = (1, 3, 5, 7, 9)
_l_(53199)
dq1 = _c_(53203, _a_(53201, _n_(53200, "collections", lambda: collections), "deque"), _n_(53202, "tup1", lambda: tup1))
_l_(53204)
_c_(53206, _n_(53205, "print", lambda: print), 'Content of dq1:')
_l_(53207)
_c_(53210, _n_(53208, "print", lambda: print), _n_(53209, "dq1", lambda: dq1))
_l_(53211)
_c_(53213, _n_(53212, "print", lambda: print), 'dq2 id:')
_l_(53214)
_c_(53219, _n_(53215, "print", lambda: print), _c_(53218, _n_(53216, "id", lambda: id), _n_(53217, "dq1", lambda: dq1)))
_l_(53220)
_c_(53222, _n_(53221, "print", lambda: print), '\nContent of dq2:')
_l_(53223)
_c_(53226, _n_(53224, "print", lambda: print), _n_(53225, "dq2", lambda: dq2))
_l_(53227)
_c_(53229, _n_(53228, "print", lambda: print), 'dq2 id:')
_l_(53230)
_c_(53235, _n_(53231, "print", lambda: print), _c_(53234, _n_(53232, "id", lambda: id), _n_(53233, "dq2", lambda: dq2)))
_l_(53236)
_c_(53238, _n_(53237, "print", lambda: print), '\nChecking the first element of dq1 and dq2 are shallow copies:')
_l_(53239)
_c_(53244, _n_(53240, "print", lambda: print), _c_(53243, _n_(53241, "id", lambda: id), _n_(53242, "dq1", lambda: dq1)[0]))
_l_(53245)
_c_(53250, _n_(53246, "print", lambda: print), _c_(53249, _n_(53247, "id", lambda: id), _n_(53248, "dq2", lambda: dq2)[0]))
_l_(53251)