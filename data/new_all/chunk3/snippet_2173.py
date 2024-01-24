# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59908880/jacobian-matrix-typeerror-function-object-does-not-support-item-assignment
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import autograd.numpy as np
    _l_(571759)

except ImportError:
    pass
try:
    from autograd import grad, jacobian
    _l_(571761)

except ImportError:
    pass

def f(x):
    _l_(571792)

    f = _c_(571767, _a_(571763, _n_(571762, "np", lambda: np), "zeros"), _c_(571766, _n_(571764, "len", lambda: len), _n_(571765, "x", lambda: x)))
    _l_(571768)
    _n_(571769, "f", lambda: f)[0] = _c_(571773, _a_(571771, _n_(571770, "np", lambda: np), "sin"), _n_(571772, "x", lambda: x)[0])+_n_(571774, "x", lambda: x)[1]**2 +_c_(571778, _a_(571776, _n_(571775, "np", lambda: np), "log"), _n_(571777, "x", lambda: x)[2])-7 
    _l_(571779) 
    _n_(571780, "f", lambda: f)[1] = 3.0*_n_(571781, "x", lambda: x)[0] + 2.0**_n_(571782, "x", lambda: x)[1] - _n_(571783, "x", lambda: x)[2]**3 + 1.0
    _l_(571784)
    _n_(571785, "f", lambda: f)[2] = _n_(571786, "x", lambda: x)[0] + _n_(571787, "x", lambda: x)[1] + _n_(571788, "x", lambda: x)[2] - 5.0
    _l_(571789)
    aux = _n_(571790, "f", lambda: f)
    _l_(571791)
    return aux
x = _c_(571795, _a_(571794, _n_(571793, "np", lambda: np), "array"), [-1.0,0.2,0.3])
_l_(571796)
gradient_cost = _c_(571799, _n_(571797, "grad", lambda: grad), _n_(571798, "f", lambda: f))
_l_(571800)
jacobian_cost = _c_(571803, _n_(571801, "jacobian", lambda: jacobian), _n_(571802, "f", lambda: f))
_l_(571804)

_c_(571807, _n_(571805, "gradient_cost", lambda: gradient_cost), _n_(571806, "x", lambda: x))
_l_(571808)
_c_(571816, _n_(571809, "jacobian_cost", lambda: jacobian_cost), _c_(571815, _a_(571811, _n_(571810, "np", lambda: np), "array"), [_n_(571812, "x", lambda: x),_n_(571813, "x", lambda: x),_n_(571814, "x", lambda: x)]))
_l_(571817)