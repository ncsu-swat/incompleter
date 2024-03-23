# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(86676)

except ImportError:
    pass
nums = _c_(86679, _a_(86678, _n_(86677, "np", lambda: np), "array"), [1, 2, 3, 4, 5])
_l_(86680)
_c_(86682, _n_(86681, "print", lambda: print), '50th percentile (median):')
_l_(86683)
p = _c_(86687, _a_(86685, _n_(86684, "np", lambda: np), "percentile"), _n_(86686, "nums", lambda: nums), 50)
_l_(86688)
_c_(86691, _n_(86689, "print", lambda: print), _n_(86690, "p", lambda: p))
_l_(86692)
_c_(86694, _n_(86693, "print", lambda: print), '40th percentile:')
_l_(86695)
p = _c_(86699, _a_(86697, _n_(86696, "np", lambda: np), "percentile"), _n_(86698, "nums", lambda: nums), 40)
_l_(86700)
_c_(86703, _n_(86701, "print", lambda: print), _n_(86702, "p", lambda: p))
_l_(86704)
_c_(86706, _n_(86705, "print", lambda: print), '90th percentile:')
_l_(86707)
_c_(86710, _n_(86708, "print", lambda: print), _n_(86709, "p", lambda: p))
_l_(86711)