# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(112102)

except ImportError:
    pass
try:
    import os
    _l_(112104)

except ImportError:
    pass
a = _c_(112107, _a_(112106, _n_(112105, "np", lambda: np), "array"), [1, 2, 3, 4, 5, 6])
_l_(112108)
_c_(112110, _n_(112109, "print", lambda: print), 'Original array:')
_l_(112111)
_c_(112114, _n_(112112, "print", lambda: print), _n_(112113, "a", lambda: a))
_l_(112115)
a2 = _c_(112121, _a_(112117, _n_(112116, "np", lambda: np), "fromstring"), _n_(112118, "a_bytes", lambda: a_bytes), dtype=_a_(112120, _n_(112119, "a", lambda: a), "dtype"))
_l_(112122)
_c_(112124, _n_(112123, "print", lambda: print), 'After loading, content of the text file:')
_l_(112125)
_c_(112128, _n_(112126, "print", lambda: print), _n_(112127, "a2", lambda: a2))
_l_(112129)
_c_(112136, _n_(112130, "print", lambda: print), _c_(112135, _a_(112132, _n_(112131, "np", lambda: np), "array_equal"), _n_(112133, "a", lambda: a), _n_(112134, "a2", lambda: a2)))
_l_(112137)