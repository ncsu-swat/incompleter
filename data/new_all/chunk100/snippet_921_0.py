# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(93787)

except ImportError:
    pass
x = [1, 2, 3]
_l_(93788)
y = [4, 5]
_l_(93789)
_c_(93791, _n_(93790, "print", lambda: print), 'Original arrays:')
_l_(93792)
_c_(93794, _n_(93793, "print", lambda: print), 'Array-1')
_l_(93795)
_c_(93798, _n_(93796, "print", lambda: print), _n_(93797, "x", lambda: x))
_l_(93799)
_c_(93801, _n_(93800, "print", lambda: print), 'Array-2')
_l_(93802)
_c_(93805, _n_(93803, "print", lambda: print), _n_(93804, "y", lambda: y))
_l_(93806)
_c_(93808, _n_(93807, "print", lambda: print), 'Array-3')
_l_(93809)
_c_(93812, _n_(93810, "print", lambda: print), _n_(93811, "z", lambda: z))
_l_(93813)
new_array = _c_(93825, _a_(93824, _a_(93823, _c_(93822, _a_(93815, _n_(93814, "np", lambda: np), "array"), _c_(93821, _a_(93817, _n_(93816, "np", lambda: np), "meshgrid"), _n_(93818, "x", lambda: x), _n_(93819, "y", lambda: y), _n_(93820, "z", lambda: z))), "T"), "reshape"), -1, 3)
_l_(93826)
_c_(93828, _n_(93827, "print", lambda: print), 'Combine array:')
_l_(93829)
_c_(93832, _n_(93830, "print", lambda: print), _n_(93831, "new_array", lambda: new_array))
_l_(93833)