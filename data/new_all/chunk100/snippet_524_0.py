# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(53316)

except ImportError:
    pass
_c_(53318, _n_(53317, "print", lambda: print), 'Original array:')
_l_(53319)
_c_(53322, _n_(53320, "print", lambda: print), _n_(53321, "my_array", lambda: my_array))
_l_(53323)
_n_(53324, "my_array", lambda: my_array)[:, [0, 1]] = _n_(53325, "my_array", lambda: my_array)[:, [1, 0]]
_l_(53326)
_c_(53328, _n_(53327, "print", lambda: print), '\nAfter swapping arrays:')
_l_(53329)
_c_(53332, _n_(53330, "print", lambda: print), _n_(53331, "my_array", lambda: my_array))
_l_(53333)