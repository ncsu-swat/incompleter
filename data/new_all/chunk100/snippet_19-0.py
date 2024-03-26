# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from numpy.polynomial import polynomial as P
    _l_(104092)

except ImportError:
    pass
x = (10, 20, 30)
_l_(104093)
_c_(104095, _n_(104094, "print", lambda: print), 'Add one polynomial to another:')
_l_(104096)
_c_(104103, _n_(104097, "print", lambda: print), _c_(104102, _a_(104099, _n_(104098, "P", lambda: P), "polyadd"), _n_(104100, "x", lambda: x), _n_(104101, "y", lambda: y)))
_l_(104104)
_c_(104106, _n_(104105, "print", lambda: print), 'Subtract one polynomial from another:')
_l_(104107)
_c_(104114, _n_(104108, "print", lambda: print), _c_(104113, _a_(104110, _n_(104109, "P", lambda: P), "polysub"), _n_(104111, "x", lambda: x), _n_(104112, "y", lambda: y)))
_l_(104115)
_c_(104117, _n_(104116, "print", lambda: print), 'Multiply one polynomial by another:')
_l_(104118)
_c_(104125, _n_(104119, "print", lambda: print), _c_(104124, _a_(104121, _n_(104120, "P", lambda: P), "polymul"), _n_(104122, "x", lambda: x), _n_(104123, "y", lambda: y)))
_l_(104126)
_c_(104128, _n_(104127, "print", lambda: print), 'Divide one polynomial by another:')
_l_(104129)
_c_(104136, _n_(104130, "print", lambda: print), _c_(104135, _a_(104132, _n_(104131, "P", lambda: P), "polydiv"), _n_(104133, "x", lambda: x), _n_(104134, "y", lambda: y)))
_l_(104137)