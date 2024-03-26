# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(101368)

except ImportError:
    pass
nums = _c_(101371, _a_(101370, _n_(101369, "np", lambda: np), "array"), [1, 2, 3, 4, 5, 6, 7, 8])
_l_(101372)
_c_(101374, _n_(101373, "print", lambda: print), 'Original array:')
_l_(101375)
_c_(101378, _n_(101376, "print", lambda: print), _n_(101377, "nums", lambda: nums))
_l_(101379)
p = 2
_l_(101380)
_n_(101381, "new_nums", lambda: new_nums)[::_n_(101382, "p", lambda: p) + 1] = _n_(101383, "nums", lambda: nums)
_l_(101384)
_c_(101386, _n_(101385, "print", lambda: print), '\nNew array:')
_l_(101387)
_c_(101390, _n_(101388, "print", lambda: print), _n_(101389, "new_nums", lambda: new_nums))
_l_(101391)