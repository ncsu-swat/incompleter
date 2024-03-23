# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import Counter
    _l_(8186)

except ImportError:
    pass
l2 = [1, 1, 2, 4, 5, 6]
_l_(8187)
_c_(8189, _n_(8188, "print", lambda: print), 'Original lists:')
_l_(8190)
c1 = _c_(8193, _n_(8191, "Counter", lambda: Counter), _n_(8192, "l1", lambda: l1))
_l_(8194)
c2 = _c_(8197, _n_(8195, "Counter", lambda: Counter), _n_(8196, "l2", lambda: l2))
_l_(8198)
diff = _n_(8199, "c1", lambda: c1) - _n_(8200, "c2", lambda: c2)
_l_(8201)
_c_(8208, _n_(8202, "print", lambda: print), _c_(8207, _n_(8203, "list", lambda: list), _c_(8206, _a_(8205, _n_(8204, "diff", lambda: diff), "elements"))))
_l_(8209)