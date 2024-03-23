# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import collections
    _l_(53086)

except ImportError:
    pass
dq1 = _c_(53090, _a_(53088, _n_(53087, "collections", lambda: collections), "deque"), _n_(53089, "tup1", lambda: tup1))
_l_(53091)
dq2 = _c_(53094, _a_(53093, _n_(53092, "dq1", lambda: dq1), "copy"))
_l_(53095)
_c_(53097, _n_(53096, "print", lambda: print), 'Content of dq1:')
_l_(53098)
_c_(53101, _n_(53099, "print", lambda: print), _n_(53100, "dq1", lambda: dq1))
_l_(53102)
_c_(53104, _n_(53103, "print", lambda: print), 'dq2 id:')
_l_(53105)
_c_(53110, _n_(53106, "print", lambda: print), _c_(53109, _n_(53107, "id", lambda: id), _n_(53108, "dq1", lambda: dq1)))
_l_(53111)
_c_(53113, _n_(53112, "print", lambda: print), '\nContent of dq2:')
_l_(53114)
_c_(53117, _n_(53115, "print", lambda: print), _n_(53116, "dq2", lambda: dq2))
_l_(53118)
_c_(53120, _n_(53119, "print", lambda: print), 'dq2 id:')
_l_(53121)
_c_(53126, _n_(53122, "print", lambda: print), _c_(53125, _n_(53123, "id", lambda: id), _n_(53124, "dq2", lambda: dq2)))
_l_(53127)
_c_(53129, _n_(53128, "print", lambda: print), '\nChecking the first element of dq1 and dq2 are shallow copies:')
_l_(53130)
_c_(53135, _n_(53131, "print", lambda: print), _c_(53134, _n_(53132, "id", lambda: id), _n_(53133, "dq1", lambda: dq1)[0]))
_l_(53136)
_c_(53141, _n_(53137, "print", lambda: print), _c_(53140, _n_(53138, "id", lambda: id), _n_(53139, "dq2", lambda: dq2)[0]))
_l_(53142)