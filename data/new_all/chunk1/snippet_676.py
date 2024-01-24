# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59459414/sympy-typeerror-cant-convert-expression-to-float
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sympy as sp
    _l_(396260)

except ImportError:
    pass
try:
    from scipy.integrate import quad
    _l_(396262)

except ImportError:
    pass
try:
    import math
    _l_(396264)

except ImportError:
    pass
def f(x):
    _l_(396275)

    aux = _c_(396273, _a_(396266, _n_(396265, "math", lambda: math), "exp"), -2.0*_a_(396268, _n_(396267, "math", lambda: math), "pi")*_a_(396270, _n_(396269, "sp", lambda: sp), "I")*_n_(396271, "x", lambda: x)*_n_(396272, "n", lambda: n))
    _l_(396274)
    return aux
x = _c_(396278, _a_(396277, _n_(396276, "sp", lambda: sp), "Symbol"), 'x')
_l_(396279)
n = _c_(396282, _a_(396281, _n_(396280, "sp", lambda: sp), "Symbol"), 'n')
_l_(396283)
res,err = _c_(396286, _n_(396284, "quad", lambda: quad), _n_(396285, "f", lambda: f),0,1)
_l_(396287)
_c_(396290, _n_(396288, "print", lambda: print), _n_(396289, "res", lambda: res))
_l_(396291)