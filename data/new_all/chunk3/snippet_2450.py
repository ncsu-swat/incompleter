# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/25178925/i-dont-understand-this-typeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class vector2D:
    _l_(552101)


    def __init__(self, x=0.0, y=0.0):
        _l_(552078)

        _n_(552072, "self", lambda: self).x = _n_(552073, "x", lambda: x)
        _l_(552074)
        _n_(552075, "self", lambda: self).y = _n_(552076, "y", lambda: y)
        _l_(552077)

    def __str__(self):
        _l_(552086)

        aux = _c_(552084, _a_(552079, "({}, {})", "format"), _a_(552081, _n_(552080, "self", lambda: self), "x"), _a_(552083, _n_(552082, "self", lambda: self), "y"))
        _l_(552085)
        return aux

    @_n_(552087, "classmethod", lambda: classmethod)
    def frompoints(cls, P1, P2):
        _l_(552100)

        x = _n_(552088, "P2", lambda: P2)[0] - _n_(552089, "P1", lambda: P1)[0]
        _l_(552090)
        y = _n_(552091, "P2", lambda: P2)[1] - _n_(552092, "P1", lambda: P1)[1]
        _l_(552093)
        aux = _c_(552098, _n_(552094, "vector2D", lambda: vector2D), _n_(552095, "cls", lambda: cls), _n_(552096, "x", lambda: x), _n_(552097, "y", lambda: y))
        _l_(552099)
        return aux

P1 = (10.0, 5.0)
_l_(552102)
P2 = (17.0, 10.0)
_l_(552103)
v2 = _c_(552108, _a_(552105, _n_(552104, "vector2D", lambda: vector2D), "frompoints"), _n_(552106, "P1", lambda: P1), _n_(552107, "P2", lambda: P2))
_l_(552109)