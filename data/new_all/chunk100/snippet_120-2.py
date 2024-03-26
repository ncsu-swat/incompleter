# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import Counter
    _l_(101505)

except ImportError:
    pass
l1 = [1, 1, 2, 3, 3, 4, 4, 5, 6, 7]
_l_(101506)
l2 = [1, 1, 2, 4, 5, 6]
_l_(101507)
_c_(101509, _n_(101508, "print", lambda: print), 'Original lists:')
_l_(101510)
c1 = _c_(101513, _n_(101511, "Counter", lambda: Counter), _n_(101512, "l1", lambda: l1))
_l_(101514)
diff = _n_(101515, "c1", lambda: c1) - _n_(101516, "c2", lambda: c2)
_l_(101517)
_c_(101524, _n_(101518, "print", lambda: print), _c_(101523, _n_(101519, "list", lambda: list), _c_(101522, _a_(101521, _n_(101520, "diff", lambda: diff), "elements"))))
_l_(101525)