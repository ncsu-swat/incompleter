# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(114202)

except ImportError:
    pass
nums = _c_(114205, _a_(114204, _n_(114203, "np", lambda: np), "array"), [0, 1, 3, 5, 7, 9, 11, 13, 15])
_l_(114206)
_c_(114208, _n_(114207, "print", lambda: print), 'Original vector:')
_l_(114209)
_c_(114212, _n_(114210, "print", lambda: print), _n_(114211, "nums", lambda: nums))
_l_(114213)
_c_(114215, _n_(114214, "print", lambda: print), '\nBinary representation of the said vector:')
_l_(114216)
_c_(114219, _n_(114217, "print", lambda: print), _n_(114218, "bin_nums", lambda: bin_nums)[:, ::-1])
_l_(114220)