# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67128403/sympy-attributeerror-multiply-polynomial-by-complex-constant
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from sympy import *
    _l_(567670)

except ImportError:
    pass
try:
    from sympy.abc import x, y, z, w
    _l_(567672)

except ImportError:
    pass

p = _c_(567676, _n_(567673, "Poly", lambda: Poly), 1.0*_n_(567674, "x", lambda: x), _n_(567675, "x", lambda: x), domain='C')
_l_(567677)
_n_(567678, "p", lambda: p)*_n_(567679, "I", lambda: I)
_l_(567680)