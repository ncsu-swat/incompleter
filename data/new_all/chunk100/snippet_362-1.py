# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(112224)

except ImportError:
    pass
a = _c_(112227, _a_(112226, _n_(112225, "np", lambda: np), "array"), [[4, 6], [2, 1]])
_l_(112228)
_c_(112230, _n_(112229, "print", lambda: print), 'Original array: ')
_l_(112231)
_c_(112234, _n_(112232, "print", lambda: print), _n_(112233, "a", lambda: a))
_l_(112235)
_c_(112237, _n_(112236, "print", lambda: print), 'Sort along the first axis: ')
_l_(112238)
_c_(112241, _n_(112239, "print", lambda: print), _n_(112240, "x", lambda: x))
_l_(112242)
_c_(112244, _n_(112243, "print", lambda: print), 'Sort along the last axis: ')
_l_(112245)
y = _c_(112249, _a_(112247, _n_(112246, "np", lambda: np), "sort"), _n_(112248, "x", lambda: x), axis=1)
_l_(112250)
_c_(112253, _n_(112251, "print", lambda: print), _n_(112252, "y", lambda: y))
_l_(112254)