# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(112191)

except ImportError:
    pass
_c_(112193, _n_(112192, "print", lambda: print), 'Original array: ')
_l_(112194)
_c_(112197, _n_(112195, "print", lambda: print), _n_(112196, "a", lambda: a))
_l_(112198)
_c_(112200, _n_(112199, "print", lambda: print), 'Sort along the first axis: ')
_l_(112201)
x = _c_(112205, _a_(112203, _n_(112202, "np", lambda: np), "sort"), _n_(112204, "a", lambda: a), axis=0)
_l_(112206)
_c_(112209, _n_(112207, "print", lambda: print), _n_(112208, "x", lambda: x))
_l_(112210)
_c_(112212, _n_(112211, "print", lambda: print), 'Sort along the last axis: ')
_l_(112213)
y = _c_(112217, _a_(112215, _n_(112214, "np", lambda: np), "sort"), _n_(112216, "x", lambda: x), axis=1)
_l_(112218)
_c_(112221, _n_(112219, "print", lambda: print), _n_(112220, "y", lambda: y))
_l_(112222)