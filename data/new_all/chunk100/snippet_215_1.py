# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(17044)

except ImportError:
    pass
_c_(17046, _n_(17045, "print", lambda: print), 'Original vector:')
_l_(17047)
_c_(17050, _n_(17048, "print", lambda: print), _n_(17049, "nums", lambda: nums))
_l_(17051)
new_nums = _c_(17057, _a_(17054, _a_(17053, _n_(17052, "np", lambda: np), "logical_and"), "reduce"), _n_(17055, "nums", lambda: nums)[:, 1:] == _n_(17056, "nums", lambda: nums)[:, :-1], axis=1)
_l_(17058)
result = _n_(17059, "nums", lambda: nums)[~_n_(17060, "new_nums", lambda: new_nums)]
_l_(17061)
_c_(17063, _n_(17062, "print", lambda: print), '\nRows with unequal values:')
_l_(17064)
_c_(17067, _n_(17065, "print", lambda: print), _n_(17066, "result", lambda: result))
_l_(17068)