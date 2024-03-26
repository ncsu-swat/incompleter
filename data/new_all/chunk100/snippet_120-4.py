# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import Counter
    _l_(101552)

except ImportError:
    pass
l2 = [1, 1, 2, 4, 5, 6]
_l_(101553)
_c_(101555, _n_(101554, "print", lambda: print), 'Original lists:')
_l_(101556)
c1 = _c_(101559, _n_(101557, "Counter", lambda: Counter), _n_(101558, "l1", lambda: l1))
_l_(101560)
c2 = _c_(101563, _n_(101561, "Counter", lambda: Counter), _n_(101562, "l2", lambda: l2))
_l_(101564)
diff = _n_(101565, "c1", lambda: c1) - _n_(101566, "c2", lambda: c2)
_l_(101567)
_c_(101574, _n_(101568, "print", lambda: print), _c_(101573, _n_(101569, "list", lambda: list), _c_(101572, _a_(101571, _n_(101570, "diff", lambda: diff), "elements"))))
_l_(101575)