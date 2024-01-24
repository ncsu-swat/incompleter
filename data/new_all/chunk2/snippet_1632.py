# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66885501/why-do-i-recieve-typeerror-module-object-is-not-callable-for-scipy-integrat
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import math
    _l_(475176)

except ImportError:
    pass
try:
    import scipy.integrate._quadrature as quad
    _l_(475178)

except ImportError:
    pass

def func(x):
    _l_(475185)

    aux = _n_(475179, "x", lambda: x)*_c_(475183, _a_(475181, _n_(475180, "np", lambda: np), "sin"), _n_(475182, "x", lambda: x))
    _l_(475184)
    return aux

def exactIntegral(a, b):
    _l_(475207)

    Iab = -_n_(475186, "b", lambda: b)*_c_(475190, _a_(475188, _n_(475187, "np", lambda: np), "cos"), _n_(475189, "b", lambda: b)) + _c_(475194, _a_(475192, _n_(475191, "np", lambda: np), "sin"), _n_(475193, "b", lambda: b)) + _n_(475195, "a", lambda: a)*_c_(475199, _a_(475197, _n_(475196, "np", lambda: np), "cos"), _n_(475198, "b", lambda: b)) - _c_(475203, _a_(475201, _n_(475200, "np", lambda: np), "sin"), _n_(475202, "a", lambda: a))
    _l_(475204)
    aux = _n_(475205, "Iab", lambda: Iab)
    _l_(475206)
    return aux

a = 0.0
_l_(475208)
b = 2.0 
_l_(475209) 

exact = _c_(475213, _n_(475210, "exactIntegral", lambda: exactIntegral), _n_(475211, "a", lambda: a), _n_(475212, "b", lambda: b))
_l_(475214)
estimate = _c_(475219, _n_(475215, "quad", lambda: quad), _n_(475216, "func", lambda: func), _n_(475217, "a", lambda: a), _n_(475218, "b", lambda: b))                               #TypeError: 'module' object is not callable
_l_(475220)                               #TypeError: 'module' object is not callable

_c_(475224, _n_(475221, "print", lambda: print), 'Exact %1.6f Numerical %1.6f' %(_n_(475222, "exact", lambda: exact), _n_(475223, "estimate", lambda: estimate)[0]))
_l_(475225)
_c_(475232, _n_(475226, "print", lambda: print), 'Error %1.3e' % _c_(475231, _a_(475228, _n_(475227, "np", lambda: np), "abs"), _n_(475229, "exact", lambda: exact)-_n_(475230, "estimate", lambda: estimate)[0]))
_l_(475233)