# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(17016)

except ImportError:
    pass
nums = _c_(17020, _a_(17019, _a_(17018, _n_(17017, "np", lambda: np), "random"), "randint"), 0, 4, (6, 3))
_l_(17021)
_c_(17023, _n_(17022, "print", lambda: print), 'Original vector:')
_l_(17024)
_c_(17027, _n_(17025, "print", lambda: print), _n_(17026, "nums", lambda: nums))
_l_(17028)
new_nums = _c_(17034, _a_(17031, _a_(17030, _n_(17029, "np", lambda: np), "logical_and"), "reduce"), _n_(17032, "nums", lambda: nums)[:, 1:] == _n_(17033, "nums", lambda: nums)[:, :-1], axis=1)
_l_(17035)
_c_(17037, _n_(17036, "print", lambda: print), '\nRows with unequal values:')
_l_(17038)
_c_(17041, _n_(17039, "print", lambda: print), _n_(17040, "result", lambda: result))
_l_(17042)