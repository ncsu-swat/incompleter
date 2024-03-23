# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(39145)

except ImportError:
    pass
nums = _c_(39148, _a_(39147, _n_(39146, "np", lambda: np), "array"), [0, 1, 3, 5, 7, 9, 11, 13, 15])
_l_(39149)
_c_(39151, _n_(39150, "print", lambda: print), 'Original vector:')
_l_(39152)
_c_(39155, _n_(39153, "print", lambda: print), _n_(39154, "nums", lambda: nums))
_l_(39156)
_c_(39158, _n_(39157, "print", lambda: print), '\nBinary representation of the said vector:')
_l_(39159)
_c_(39162, _n_(39160, "print", lambda: print), _n_(39161, "bin_nums", lambda: bin_nums)[:, ::-1])
_l_(39163)