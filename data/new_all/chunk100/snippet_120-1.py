# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import Counter
    _l_(101482)

except ImportError:
    pass
l1 = [1, 1, 2, 3, 3, 4, 4, 5, 6, 7]
_l_(101483)
l2 = [1, 1, 2, 4, 5, 6]
_l_(101484)
_c_(101486, _n_(101485, "print", lambda: print), 'Original lists:')
_l_(101487)
c1 = _c_(101490, _n_(101488, "Counter", lambda: Counter), _n_(101489, "l1", lambda: l1))
_l_(101491)
c2 = _c_(101494, _n_(101492, "Counter", lambda: Counter), _n_(101493, "l2", lambda: l2))
_l_(101495)
_c_(101502, _n_(101496, "print", lambda: print), _c_(101501, _n_(101497, "list", lambda: list), _c_(101500, _a_(101499, _n_(101498, "diff", lambda: diff), "elements"))))
_l_(101503)