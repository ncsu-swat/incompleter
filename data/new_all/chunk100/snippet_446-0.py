# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(116664)

except ImportError:
    pass
_c_(116666, _n_(116665, "print", lambda: print), 'Original array:')
_l_(116667)
_c_(116670, _n_(116668, "print", lambda: print), _n_(116669, "array_nums", lambda: array_nums))
_l_(116671)
_c_(116673, _n_(116672, "print", lambda: print), '\nAfter swapping column1 with column4:')
_l_(116674)
_n_(116675, "array_nums", lambda: array_nums)[:, [0, 3]] = _n_(116676, "array_nums", lambda: array_nums)[:, [3, 0]]
_l_(116677)
_c_(116680, _n_(116678, "print", lambda: print), _n_(116679, "array_nums", lambda: array_nums))
_l_(116681)