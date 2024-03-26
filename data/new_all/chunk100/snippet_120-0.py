# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import Counter
    _l_(101460)

except ImportError:
    pass
l1 = [1, 1, 2, 3, 3, 4, 4, 5, 6, 7]
_l_(101461)
l2 = [1, 1, 2, 4, 5, 6]
_l_(101462)
_c_(101464, _n_(101463, "print", lambda: print), 'Original lists:')
_l_(101465)
c2 = _c_(101468, _n_(101466, "Counter", lambda: Counter), _n_(101467, "l2", lambda: l2))
_l_(101469)
diff = _n_(101470, "c1", lambda: c1) - _n_(101471, "c2", lambda: c2)
_l_(101472)
_c_(101479, _n_(101473, "print", lambda: print), _c_(101478, _n_(101474, "list", lambda: list), _c_(101477, _a_(101476, _n_(101475, "diff", lambda: diff), "elements"))))
_l_(101480)