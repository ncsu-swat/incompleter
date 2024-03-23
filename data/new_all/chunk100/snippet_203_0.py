# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(15904)

except ImportError:
    pass
_c_(15906, _n_(15905, "print", lambda: print), 'Original array:')
_l_(15907)
_c_(15910, _n_(15908, "print", lambda: print), _n_(15909, "a", lambda: a))
_l_(15911)
result = _c_(15919, _a_(15913, _n_(15912, "np", lambda: np), "where"), _c_(15918, _a_(15915, _n_(15914, "np", lambda: np), "logical_and"), _n_(15916, "a", lambda: a) >= 7, _n_(15917, "a", lambda: a) <= 20))
_l_(15920)
_c_(15922, _n_(15921, "print", lambda: print), '\nElements within range: index position')
_l_(15923)
_c_(15926, _n_(15924, "print", lambda: print), _n_(15925, "result", lambda: result))
_l_(15927)