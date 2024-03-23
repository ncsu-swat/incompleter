# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(39165)

except ImportError:
    pass
_c_(39167, _n_(39166, "print", lambda: print), 'Original vector:')
_l_(39168)
_c_(39171, _n_(39169, "print", lambda: print), _n_(39170, "nums", lambda: nums))
_l_(39172)
bin_nums = _c_(39181, _a_(39179, (_c_(39175, _a_(39174, _n_(39173, "nums", lambda: nums), "reshape"), -1, 1) & 2 ** _c_(39178, _a_(39177, _n_(39176, "np", lambda: np), "arange"), 8) != 0), "astype"), _n_(39180, "int", lambda: int))
_l_(39182)
_c_(39184, _n_(39183, "print", lambda: print), '\nBinary representation of the said vector:')
_l_(39185)
_c_(39188, _n_(39186, "print", lambda: print), _n_(39187, "bin_nums", lambda: bin_nums)[:, ::-1])
_l_(39189)