# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(47872)

except ImportError:
    pass
_c_(47874, _n_(47873, "print", lambda: print), 'Original array:')
_l_(47875)
_c_(47878, _n_(47876, "print", lambda: print), _n_(47877, "array_nums", lambda: array_nums))
_l_(47879)
_c_(47881, _n_(47880, "print", lambda: print), '\nAfter swapping column1 with column4:')
_l_(47882)
_n_(47883, "array_nums", lambda: array_nums)[:, [0, 3]] = _n_(47884, "array_nums", lambda: array_nums)[:, [3, 0]]
_l_(47885)
_c_(47888, _n_(47886, "print", lambda: print), _n_(47887, "array_nums", lambda: array_nums))
_l_(47889)