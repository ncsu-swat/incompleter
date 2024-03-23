# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from numpy.polynomial import polynomial as P
    _l_(15739)

except ImportError:
    pass
x = (10, 20, 30)
_l_(15740)
_c_(15742, _n_(15741, "print", lambda: print), 'Add one polynomial to another:')
_l_(15743)
_c_(15750, _n_(15744, "print", lambda: print), _c_(15749, _a_(15746, _n_(15745, "P", lambda: P), "polyadd"), _n_(15747, "x", lambda: x), _n_(15748, "y", lambda: y)))
_l_(15751)
_c_(15753, _n_(15752, "print", lambda: print), 'Subtract one polynomial from another:')
_l_(15754)
_c_(15761, _n_(15755, "print", lambda: print), _c_(15760, _a_(15757, _n_(15756, "P", lambda: P), "polysub"), _n_(15758, "x", lambda: x), _n_(15759, "y", lambda: y)))
_l_(15762)
_c_(15764, _n_(15763, "print", lambda: print), 'Multiply one polynomial by another:')
_l_(15765)
_c_(15772, _n_(15766, "print", lambda: print), _c_(15771, _a_(15768, _n_(15767, "P", lambda: P), "polymul"), _n_(15769, "x", lambda: x), _n_(15770, "y", lambda: y)))
_l_(15773)
_c_(15775, _n_(15774, "print", lambda: print), 'Divide one polynomial by another:')
_l_(15776)
_c_(15783, _n_(15777, "print", lambda: print), _c_(15782, _a_(15779, _n_(15778, "P", lambda: P), "polydiv"), _n_(15780, "x", lambda: x), _n_(15781, "y", lambda: y)))
_l_(15784)