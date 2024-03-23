# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from numpy.polynomial import polynomial as P
    _l_(15786)

except ImportError:
    pass
y = (30, 40, 50)
_l_(15787)
_c_(15789, _n_(15788, "print", lambda: print), 'Add one polynomial to another:')
_l_(15790)
_c_(15797, _n_(15791, "print", lambda: print), _c_(15796, _a_(15793, _n_(15792, "P", lambda: P), "polyadd"), _n_(15794, "x", lambda: x), _n_(15795, "y", lambda: y)))
_l_(15798)
_c_(15800, _n_(15799, "print", lambda: print), 'Subtract one polynomial from another:')
_l_(15801)
_c_(15808, _n_(15802, "print", lambda: print), _c_(15807, _a_(15804, _n_(15803, "P", lambda: P), "polysub"), _n_(15805, "x", lambda: x), _n_(15806, "y", lambda: y)))
_l_(15809)
_c_(15811, _n_(15810, "print", lambda: print), 'Multiply one polynomial by another:')
_l_(15812)
_c_(15819, _n_(15813, "print", lambda: print), _c_(15818, _a_(15815, _n_(15814, "P", lambda: P), "polymul"), _n_(15816, "x", lambda: x), _n_(15817, "y", lambda: y)))
_l_(15820)
_c_(15822, _n_(15821, "print", lambda: print), 'Divide one polynomial by another:')
_l_(15823)
_c_(15830, _n_(15824, "print", lambda: print), _c_(15829, _a_(15826, _n_(15825, "P", lambda: P), "polydiv"), _n_(15827, "x", lambda: x), _n_(15828, "y", lambda: y)))
_l_(15831)