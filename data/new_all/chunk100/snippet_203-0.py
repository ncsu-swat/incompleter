# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(104943)

except ImportError:
    pass
_c_(104945, _n_(104944, "print", lambda: print), 'Original array:')
_l_(104946)
_c_(104949, _n_(104947, "print", lambda: print), _n_(104948, "a", lambda: a))
_l_(104950)
result = _c_(104958, _a_(104952, _n_(104951, "np", lambda: np), "where"), _c_(104957, _a_(104954, _n_(104953, "np", lambda: np), "logical_and"), _n_(104955, "a", lambda: a) >= 7, _n_(104956, "a", lambda: a) <= 20))
_l_(104959)
_c_(104961, _n_(104960, "print", lambda: print), '\nElements within range: index position')
_l_(104962)
_c_(104965, _n_(104963, "print", lambda: print), _n_(104964, "result", lambda: result))
_l_(104966)