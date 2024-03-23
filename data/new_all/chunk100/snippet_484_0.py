# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(50568)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(50570)

except ImportError:
    pass
bins = _c_(50573, _a_(50572, _n_(50571, "np", lambda: np), "array"), [0, 1, 2, 3])
_l_(50574)
_c_(50577, _n_(50575, "print", lambda: print), 'nums: ', _n_(50576, "nums", lambda: nums))
_l_(50578)
_c_(50581, _n_(50579, "print", lambda: print), 'bins: ', _n_(50580, "bins", lambda: bins))
_l_(50582)
_c_(50589, _n_(50583, "print", lambda: print), 'Result:', _c_(50588, _a_(50585, _n_(50584, "np", lambda: np), "histogram"), _n_(50586, "nums", lambda: nums), _n_(50587, "bins", lambda: bins)))
_l_(50590)
_c_(50595, _a_(50592, _n_(50591, "plt", lambda: plt), "hist"), _n_(50593, "nums", lambda: nums), bins=_n_(50594, "bins", lambda: bins))
_l_(50596)
_c_(50599, _a_(50598, _n_(50597, "plt", lambda: plt), "show"))
_l_(50600)