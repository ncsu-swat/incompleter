# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(98733)

except ImportError:
    pass
nums = _c_(98738, _a_(98737, _c_(98736, _a_(98735, _n_(98734, "np", lambda: np), "arange"), 16, dtype='int'), "reshape"), -1, 4)
_l_(98739)
_c_(98741, _n_(98740, "print", lambda: print), 'Original array:')
_l_(98742)
_c_(98745, _n_(98743, "print", lambda: print), _n_(98744, "nums", lambda: nums))
_l_(98746)
_c_(98748, _n_(98747, "print", lambda: print), '\nNew array after swapping first and last columns of the said array:')
_l_(98749)
_c_(98752, _n_(98750, "print", lambda: print), _n_(98751, "new_nums", lambda: new_nums))
_l_(98753)