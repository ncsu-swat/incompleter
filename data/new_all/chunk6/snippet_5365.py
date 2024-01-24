# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61710648/typeerror-int-object-is-not-subscriptable-while-doing-feature-engineering
# Creation of X1_new
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
X1_new = []
_l_(361993)
for x in _n_(361994, "X1", lambda: X1):
    _l_(362007)

    torque = _n_(361995, "x", lambda: x)[0]**2 + _n_(361996, "x", lambda: x)[1]**2 + _n_(361997, "x", lambda: x)[2]**2
    _l_(361998)
    sqr = _n_(361999, "torque", lambda: torque) ** 0.5
    _l_(362000)
    _c_(362005, _a_(362002, _n_(362001, "X1_new", lambda: X1_new), "append"), _n_(362003, "x", lambda: x) + [_n_(362004, "sqr", lambda: sqr)])
    _l_(362006)
_c_(362010, _n_(362008, "print", lambda: print), _n_(362009, "X1_new", lambda: X1_new)[0]) # Look at the first input
_l_(362011) # Look at the first input