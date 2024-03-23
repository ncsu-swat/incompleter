# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(86751)

except ImportError:
    pass
nums = _c_(86754, _a_(86753, _n_(86752, "np", lambda: np), "array"), [1, 2, 3, 4, 5])
_l_(86755)
_c_(86757, _n_(86756, "print", lambda: print), '50th percentile (median):')
_l_(86758)
p = _c_(86762, _a_(86760, _n_(86759, "np", lambda: np), "percentile"), _n_(86761, "nums", lambda: nums), 50)
_l_(86763)
_c_(86766, _n_(86764, "print", lambda: print), _n_(86765, "p", lambda: p))
_l_(86767)
_c_(86769, _n_(86768, "print", lambda: print), '40th percentile:')
_l_(86770)
_c_(86773, _n_(86771, "print", lambda: print), _n_(86772, "p", lambda: p))
_l_(86774)
_c_(86776, _n_(86775, "print", lambda: print), '90th percentile:')
_l_(86777)
p = _c_(86781, _a_(86779, _n_(86778, "np", lambda: np), "percentile"), _n_(86780, "nums", lambda: nums), 90)
_l_(86782)
_c_(86785, _n_(86783, "print", lambda: print), _n_(86784, "p", lambda: p))
_l_(86786)