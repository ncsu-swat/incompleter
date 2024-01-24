# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64241489/multiplication-returning-error-typeerror-int-object-is-not-subscriptable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def distance_constraint(coords):
    _l_(568180)

    cos = 0.099567846
    _l_(568168)
    sin = 0.995030775
    _l_(568169)
    outer = 2
    _l_(568170)

    t = (_n_(568171, "coords", lambda: coords)[_n_(568172, "outer", lambda: outer), 1] * _n_(568173, "cos", lambda: cos)) - (_n_(568174, "coords", lambda: coords)[_n_(568175, "outer", lambda: outer), 0] * _n_(568176, "sin", lambda: sin))
    _l_(568177)
    aux = _n_(568178, "t", lambda: t)
    _l_(568179)
    return aux

_c_(568184, _n_(568181, "print", lambda: print), _c_(568183, _n_(568182, "distance_constraint", lambda: distance_constraint), 5))
_l_(568185)