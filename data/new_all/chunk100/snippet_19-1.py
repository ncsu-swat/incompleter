# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from numpy.polynomial import polynomial as P
    _l_(104139)

except ImportError:
    pass
y = (30, 40, 50)
_l_(104140)
_c_(104142, _n_(104141, "print", lambda: print), 'Add one polynomial to another:')
_l_(104143)
_c_(104150, _n_(104144, "print", lambda: print), _c_(104149, _a_(104146, _n_(104145, "P", lambda: P), "polyadd"), _n_(104147, "x", lambda: x), _n_(104148, "y", lambda: y)))
_l_(104151)
_c_(104153, _n_(104152, "print", lambda: print), 'Subtract one polynomial from another:')
_l_(104154)
_c_(104161, _n_(104155, "print", lambda: print), _c_(104160, _a_(104157, _n_(104156, "P", lambda: P), "polysub"), _n_(104158, "x", lambda: x), _n_(104159, "y", lambda: y)))
_l_(104162)
_c_(104164, _n_(104163, "print", lambda: print), 'Multiply one polynomial by another:')
_l_(104165)
_c_(104172, _n_(104166, "print", lambda: print), _c_(104171, _a_(104168, _n_(104167, "P", lambda: P), "polymul"), _n_(104169, "x", lambda: x), _n_(104170, "y", lambda: y)))
_l_(104173)
_c_(104175, _n_(104174, "print", lambda: print), 'Divide one polynomial by another:')
_l_(104176)
_c_(104183, _n_(104177, "print", lambda: print), _c_(104182, _a_(104179, _n_(104178, "P", lambda: P), "polydiv"), _n_(104180, "x", lambda: x), _n_(104181, "y", lambda: y)))
_l_(104184)