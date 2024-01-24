# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54452804/typeerror-only-size-1-arrays-can-be-converted-to-python-scalars-solution
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import math as m
    _l_(693372)

except ImportError:
    pass
try:
    import pylab as pyl
    _l_(693374)

except ImportError:
    pass
try:
    import numpy as np
    _l_(693376)

except ImportError:
    pass

#normal distribution function
def normal(x,mu,sigma):
    _l_(693392)

    P=(1/_c_(693382, _a_(693378, _n_(693377, "m", lambda: m), "sqrt"), 2*_a_(693380, _n_(693379, "m", lambda: m), "pi")*_n_(693381, "sigma", lambda: sigma)**2))*_c_(693388, _a_(693384, _n_(693383, "m", lambda: m), "exp"), (-(_n_(693385, "x", lambda: x)-_n_(693386, "mu", lambda: mu))**2)/2*_n_(693387, "sigma", lambda: sigma)**2)
    _l_(693389)
    aux = _n_(693390, "P", lambda: P)
    _l_(693391)
    return aux

#solution
x = _c_(693395, _a_(693394, _n_(693393, "np", lambda: np), "linspace"), -5,5,1000)
_l_(693396)
P = _c_(693399, _n_(693397, "normal", lambda: normal), _n_(693398, "x", lambda: x),0,1)
_l_(693400)
#plotting the function
_c_(693405, _a_(693402, _n_(693401, "pyl", lambda: pyl), "plot"), _n_(693403, "x", lambda: x),_n_(693404, "P", lambda: P))
_l_(693406)
_c_(693409, _a_(693408, _n_(693407, "pyl", lambda: pyl), "show"))
_l_(693410)