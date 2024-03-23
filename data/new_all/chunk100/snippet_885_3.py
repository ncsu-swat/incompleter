# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(86788)

except ImportError:
    pass
nums = _c_(86791, _a_(86790, _n_(86789, "np", lambda: np), "array"), [1, 2, 3, 4, 5])
_l_(86792)
_c_(86794, _n_(86793, "print", lambda: print), '50th percentile (median):')
_l_(86795)
_c_(86798, _n_(86796, "print", lambda: print), _n_(86797, "p", lambda: p))
_l_(86799)
_c_(86801, _n_(86800, "print", lambda: print), '40th percentile:')
_l_(86802)
p = _c_(86806, _a_(86804, _n_(86803, "np", lambda: np), "percentile"), _n_(86805, "nums", lambda: nums), 40)
_l_(86807)
_c_(86810, _n_(86808, "print", lambda: print), _n_(86809, "p", lambda: p))
_l_(86811)
_c_(86813, _n_(86812, "print", lambda: print), '90th percentile:')
_l_(86814)
p = _c_(86818, _a_(86816, _n_(86815, "np", lambda: np), "percentile"), _n_(86817, "nums", lambda: nums), 90)
_l_(86819)
_c_(86822, _n_(86820, "print", lambda: print), _n_(86821, "p", lambda: p))
_l_(86823)