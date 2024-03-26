# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import Counter
    _l_(101527)

except ImportError:
    pass
l1 = [1, 1, 2, 3, 3, 4, 4, 5, 6, 7]
_l_(101528)
_c_(101530, _n_(101529, "print", lambda: print), 'Original lists:')
_l_(101531)
c1 = _c_(101534, _n_(101532, "Counter", lambda: Counter), _n_(101533, "l1", lambda: l1))
_l_(101535)
c2 = _c_(101538, _n_(101536, "Counter", lambda: Counter), _n_(101537, "l2", lambda: l2))
_l_(101539)
diff = _n_(101540, "c1", lambda: c1) - _n_(101541, "c2", lambda: c2)
_l_(101542)
_c_(101549, _n_(101543, "print", lambda: print), _c_(101548, _n_(101544, "list", lambda: list), _c_(101547, _a_(101546, _n_(101545, "diff", lambda: diff), "elements"))))
_l_(101550)