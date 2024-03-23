# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import Counter
    _l_(64742)

except ImportError:
    pass
_c_(64744, _n_(64743, "print", lambda: print), 'Original list of tuples:')
_l_(64745)
_c_(64748, _n_(64746, "print", lambda: print), _n_(64747, "nums", lambda: nums))
_l_(64749)
result = _c_(64757, _n_(64750, "Counter", lambda: Counter), (_c_(64755, _n_(64751, "tuple", lambda: tuple), _c_(64754, _n_(64752, "sorted", lambda: sorted), _n_(64753, "i", lambda: i))) for i in _n_(64756, "nums", lambda: nums)[0]))
_l_(64758)
_c_(64760, _n_(64759, "print", lambda: print), '\nTuples', '    ', 'frequency')
_l_(64761)
for (key, val) in _c_(64764, _a_(64763, _n_(64762, "result", lambda: result), "items")):
    _l_(64770)

    _c_(64768, _n_(64765, "print", lambda: print), _n_(64766, "key", lambda: key), ' ', _n_(64767, "val", lambda: val))
    _l_(64769)