# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import collections
    _l_(53144)

except ImportError:
    pass
tup1 = (1, 3, 5, 7, 9)
_l_(53145)
dq2 = _c_(53148, _a_(53147, _n_(53146, "dq1", lambda: dq1), "copy"))
_l_(53149)
_c_(53151, _n_(53150, "print", lambda: print), 'Content of dq1:')
_l_(53152)
_c_(53155, _n_(53153, "print", lambda: print), _n_(53154, "dq1", lambda: dq1))
_l_(53156)
_c_(53158, _n_(53157, "print", lambda: print), 'dq2 id:')
_l_(53159)
_c_(53164, _n_(53160, "print", lambda: print), _c_(53163, _n_(53161, "id", lambda: id), _n_(53162, "dq1", lambda: dq1)))
_l_(53165)
_c_(53167, _n_(53166, "print", lambda: print), '\nContent of dq2:')
_l_(53168)
_c_(53171, _n_(53169, "print", lambda: print), _n_(53170, "dq2", lambda: dq2))
_l_(53172)
_c_(53174, _n_(53173, "print", lambda: print), 'dq2 id:')
_l_(53175)
_c_(53180, _n_(53176, "print", lambda: print), _c_(53179, _n_(53177, "id", lambda: id), _n_(53178, "dq2", lambda: dq2)))
_l_(53181)
_c_(53183, _n_(53182, "print", lambda: print), '\nChecking the first element of dq1 and dq2 are shallow copies:')
_l_(53184)
_c_(53189, _n_(53185, "print", lambda: print), _c_(53188, _n_(53186, "id", lambda: id), _n_(53187, "dq1", lambda: dq1)[0]))
_l_(53190)
_c_(53195, _n_(53191, "print", lambda: print), _c_(53194, _n_(53192, "id", lambda: id), _n_(53193, "dq2", lambda: dq2)[0]))
_l_(53196)