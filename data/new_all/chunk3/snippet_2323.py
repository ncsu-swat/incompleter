# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50616850/python-3-sympy-typeerror-cant-convert-expression-to-float
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import math
    _l_(532062)

except ImportError:
    pass
try:
    from sympy import solve, Poly, Eq, Function, exp
    _l_(532064)

except ImportError:
    pass
try:
    from sympy.abc import x, y, z, a, b, c
    _l_(532066)

except ImportError:
    pass
_c_(532088, _n_(532067, "print", lambda: print), _c_(532087, _n_(532068, "solve", lambda: solve), (((_c_(532077, _a_(532070, _n_(532069, "math", lambda: math), "sin"), (((_n_(532071, "x", lambda: x) - (_n_(532072, "a", lambda: a) + 1)) / (_n_(532073, "b", lambda: b) - _n_(532074, "a", lambda: a))) - 0.5) * _a_(532076, _n_(532075, "math", lambda: math), "pi")) + 1) / 2) * 1) / _c_(532082, _a_(532079, _n_(532078, "math", lambda: math), "pow"), 1.00571, (_n_(532080, "b", lambda: b) + 1 - _n_(532081, "x", lambda: x))) *_n_(532083, "c", lambda: c),  _n_(532084, "a", lambda: a), _n_(532085, "b", lambda: b),_n_(532086, "c", lambda: c)))
_l_(532089)