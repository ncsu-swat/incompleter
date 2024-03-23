# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import Counter
    _l_(8139)

except ImportError:
    pass
l1 = [1, 1, 2, 3, 3, 4, 4, 5, 6, 7]
_l_(8140)
_c_(8142, _n_(8141, "print", lambda: print), 'Original lists:')
_l_(8143)
c1 = _c_(8146, _n_(8144, "Counter", lambda: Counter), _n_(8145, "l1", lambda: l1))
_l_(8147)
c2 = _c_(8150, _n_(8148, "Counter", lambda: Counter), _n_(8149, "l2", lambda: l2))
_l_(8151)
diff = _n_(8152, "c1", lambda: c1) - _n_(8153, "c2", lambda: c2)
_l_(8154)
_c_(8161, _n_(8155, "print", lambda: print), _c_(8160, _n_(8156, "list", lambda: list), _c_(8159, _a_(8158, _n_(8157, "diff", lambda: diff), "elements"))))
_l_(8162)