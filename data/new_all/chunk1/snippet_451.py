# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55558011/intenum-returning-attributeerror-cant-set-attribute
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from magnitude import Magnitude, MValue
    _l_(388549)

except ImportError:
    pass
try:
    from derivative import Derivative, DValue
    _l_(388551)

except ImportError:
    pass

class Quantity:
    _l_(388559)

    def __init__(self, magnitude, derivative):
        _l_(388558)

        _n_(388552, "self", lambda: self).magnitude = _n_(388553, "magnitude", lambda: magnitude)
        _l_(388554)
        _n_(388555, "self", lambda: self).derivative = _n_(388556, "derivative", lambda: derivative)
        _l_(388557)