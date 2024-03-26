# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(105524)

except ImportError:
    pass
nums = _c_(105528, _a_(105527, _a_(105526, _n_(105525, "np", lambda: np), "random"), "randint"), 0, 4, (6, 3))
_l_(105529)
_c_(105531, _n_(105530, "print", lambda: print), 'Original vector:')
_l_(105532)
_c_(105535, _n_(105533, "print", lambda: print), _n_(105534, "nums", lambda: nums))
_l_(105536)
result = _n_(105537, "nums", lambda: nums)[~_n_(105538, "new_nums", lambda: new_nums)]
_l_(105539)
_c_(105541, _n_(105540, "print", lambda: print), '\nRows with unequal values:')
_l_(105542)
_c_(105545, _n_(105543, "print", lambda: print), _n_(105544, "result", lambda: result))
_l_(105546)