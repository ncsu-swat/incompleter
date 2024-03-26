# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(114222)

except ImportError:
    pass
_c_(114224, _n_(114223, "print", lambda: print), 'Original vector:')
_l_(114225)
_c_(114228, _n_(114226, "print", lambda: print), _n_(114227, "nums", lambda: nums))
_l_(114229)
bin_nums = _c_(114238, _a_(114236, (_c_(114232, _a_(114231, _n_(114230, "nums", lambda: nums), "reshape"), -1, 1) & 2 ** _c_(114235, _a_(114234, _n_(114233, "np", lambda: np), "arange"), 8) != 0), "astype"), _n_(114237, "int", lambda: int))
_l_(114239)
_c_(114241, _n_(114240, "print", lambda: print), '\nBinary representation of the said vector:')
_l_(114242)
_c_(114245, _n_(114243, "print", lambda: print), _n_(114244, "bin_nums", lambda: bin_nums)[:, ::-1])
_l_(114246)