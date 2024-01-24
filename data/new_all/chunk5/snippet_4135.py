# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62465428/typeerror-list-indices-must-be-integers-or-slices-not-float
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
x = [811.91, 796.04, 796.14, 796.50, 796.81]
_l_(648400)

i = 0
_l_(648401)
for i in _n_(648402, "x", lambda: x):
    _l_(648412)

    difference = _n_(648403, "x", lambda: x)[_n_(648404, "i", lambda: i)+1] - _n_(648405, "x", lambda: x)[_n_(648406, "i", lambda: i)-1]
    _l_(648407)
    _c_(648410, _n_(648408, "print", lambda: print), _n_(648409, "difference", lambda: difference))
    _l_(648411)