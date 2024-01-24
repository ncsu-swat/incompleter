# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61710648/typeerror-int-object-is-not-subscriptable-while-doing-feature-engineering
# Creation of X1_new
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
X1_new = []
_l_(336710)
for x in _n_(336711, "X1", lambda: X1):
    _l_(336724)

    torque = _n_(336712, "x", lambda: x)[0]**2 + _n_(336713, "x", lambda: x)[1]**2 + _n_(336714, "x", lambda: x)[2]**2
    _l_(336715)
    sqr = _n_(336716, "torque", lambda: torque) ** 0.5
    _l_(336717)
    _c_(336722, _a_(336719, _n_(336718, "X1_new", lambda: X1_new), "append"), _n_(336720, "x", lambda: x) + [_n_(336721, "sqr", lambda: sqr)])
    _l_(336723)
_c_(336727, _n_(336725, "print", lambda: print), _n_(336726, "X1_new", lambda: X1_new)[0]) # Look at the first input
_l_(336728) # Look at the first input