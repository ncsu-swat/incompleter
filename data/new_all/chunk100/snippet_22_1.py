# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(18211)

except ImportError:
    pass
nums1 = _c_(18214, _a_(18213, _n_(18212, "np", lambda: np), "array"), [[2, 5, 2], [1, 5, 5]])
_l_(18215)
_c_(18217, _n_(18216, "print", lambda: print), 'Array1:')
_l_(18218)
_c_(18221, _n_(18219, "print", lambda: print), _n_(18220, "nums1", lambda: nums1))
_l_(18222)
_c_(18224, _n_(18223, "print", lambda: print), 'Array2:')
_l_(18225)
_c_(18228, _n_(18226, "print", lambda: print), _n_(18227, "nums2", lambda: nums2))
_l_(18229)
_c_(18231, _n_(18230, "print", lambda: print), '\nMultiply said arrays of same size element-by-element:')
_l_(18232)
_c_(18239, _n_(18233, "print", lambda: print), _c_(18238, _a_(18235, _n_(18234, "np", lambda: np), "multiply"), _n_(18236, "nums1", lambda: nums1), _n_(18237, "nums2", lambda: nums2)))
_l_(18240)