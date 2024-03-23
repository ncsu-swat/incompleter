# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import Counter
    _l_(8211)

except ImportError:
    pass
l1 = [1, 1, 2, 3, 3, 4, 4, 5, 6, 7]
_l_(8212)
l2 = [1, 1, 2, 4, 5, 6]
_l_(8213)
_c_(8215, _n_(8214, "print", lambda: print), 'Original lists:')
_l_(8216)
c2 = _c_(8219, _n_(8217, "Counter", lambda: Counter), _n_(8218, "l2", lambda: l2))
_l_(8220)
diff = _n_(8221, "c1", lambda: c1) - _n_(8222, "c2", lambda: c2)
_l_(8223)
_c_(8230, _n_(8224, "print", lambda: print), _c_(8229, _n_(8225, "list", lambda: list), _c_(8228, _a_(8227, _n_(8226, "diff", lambda: diff), "elements"))))
_l_(8231)