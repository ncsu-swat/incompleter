# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(5788)

except ImportError:
    pass
nums1 = _c_(5791, _a_(5790, _n_(5789, "np", lambda: np), "ones"), (2, 2, 3))
_l_(5792)
nums2 = 3 * _c_(5795, _a_(5794, _n_(5793, "np", lambda: np), "ones"), (2, 2))
_l_(5796)
_c_(5798, _n_(5797, "print", lambda: print), 'Original array:')
_l_(5799)
_c_(5802, _n_(5800, "print", lambda: print), _n_(5801, "nums1", lambda: nums1))
_l_(5803)
_c_(5805, _n_(5804, "print", lambda: print), '\nNew array:')
_l_(5806)
_c_(5809, _n_(5807, "print", lambda: print), _n_(5808, "new_array", lambda: new_array))
_l_(5810)