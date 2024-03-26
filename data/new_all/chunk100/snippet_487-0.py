# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(118205)

except ImportError:
    pass
_c_(118207, _n_(118206, "print", lambda: print), 'Original arrays:')
_l_(118208)
_c_(118211, _n_(118209, "print", lambda: print), _n_(118210, "array_nums1", lambda: array_nums1))
_l_(118212)
result = _n_(118213, "array_nums1", lambda: array_nums1)[(_n_(118214, "array_nums1", lambda: array_nums1) > 6) & (_n_(118215, "array_nums1", lambda: array_nums1) % 3 == 0)]
_l_(118216)
_c_(118218, _n_(118217, "print", lambda: print), '\nItems greater than 6 and a multiple of 3 of the said array:')
_l_(118219)
_c_(118222, _n_(118220, "print", lambda: print), _n_(118221, "result", lambda: result))
_l_(118223)