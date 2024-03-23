# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(86713)

except ImportError:
    pass
_c_(86715, _n_(86714, "print", lambda: print), '50th percentile (median):')
_l_(86716)
p = _c_(86720, _a_(86718, _n_(86717, "np", lambda: np), "percentile"), _n_(86719, "nums", lambda: nums), 50)
_l_(86721)
_c_(86724, _n_(86722, "print", lambda: print), _n_(86723, "p", lambda: p))
_l_(86725)
_c_(86727, _n_(86726, "print", lambda: print), '40th percentile:')
_l_(86728)
p = _c_(86732, _a_(86730, _n_(86729, "np", lambda: np), "percentile"), _n_(86731, "nums", lambda: nums), 40)
_l_(86733)
_c_(86736, _n_(86734, "print", lambda: print), _n_(86735, "p", lambda: p))
_l_(86737)
_c_(86739, _n_(86738, "print", lambda: print), '90th percentile:')
_l_(86740)
p = _c_(86744, _a_(86742, _n_(86741, "np", lambda: np), "percentile"), _n_(86743, "nums", lambda: nums), 90)
_l_(86745)
_c_(86748, _n_(86746, "print", lambda: print), _n_(86747, "p", lambda: p))
_l_(86749)