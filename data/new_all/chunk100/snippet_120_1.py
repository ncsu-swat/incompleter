# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import Counter
    _l_(8164)

except ImportError:
    pass
l1 = [1, 1, 2, 3, 3, 4, 4, 5, 6, 7]
_l_(8165)
l2 = [1, 1, 2, 4, 5, 6]
_l_(8166)
_c_(8168, _n_(8167, "print", lambda: print), 'Original lists:')
_l_(8169)
c1 = _c_(8172, _n_(8170, "Counter", lambda: Counter), _n_(8171, "l1", lambda: l1))
_l_(8173)
diff = _n_(8174, "c1", lambda: c1) - _n_(8175, "c2", lambda: c2)
_l_(8176)
_c_(8183, _n_(8177, "print", lambda: print), _c_(8182, _n_(8178, "list", lambda: list), _c_(8181, _a_(8180, _n_(8179, "diff", lambda: diff), "elements"))))
_l_(8184)