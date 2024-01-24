# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68157511/typeerror-when-drawing-circle-in-pygame
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from Box2D import (b2FixtureDef, b2CircleShape)
    _l_(632775)

except ImportError:
    pass

class Circle:
    _l_(632806)

    def __init__(self, world, x, y, PPM):
        _l_(632805)

        _n_(632776, "self", lambda: self).x = _n_(632777, "x", lambda: x) / _n_(632778, "PPM", lambda: PPM)
        _l_(632779)
        _n_(632780, "self", lambda: self).y = _n_(632781, "y", lambda: y) / _n_(632782, "PPM", lambda: PPM)
        _l_(632783)
        _n_(632784, "self", lambda: self).r = 1
        _l_(632785)

        _n_(632786, "self", lambda: self).world = _n_(632787, "world", lambda: world)
        _l_(632788)
        _n_(632789, "self", lambda: self).body = _c_(632803, _a_(632792, _a_(632791, _n_(632790, "self", lambda: self), "world"), "CreateDynamicBody"), position=(_a_(632794, _n_(632793, "self", lambda: self), "x"), _a_(632796, _n_(632795, "self", lambda: self), "y")),
            fixtures=_c_(632802, _n_(632797, "b2FixtureDef", lambda: b2FixtureDef), shape=_c_(632801, _n_(632798, "b2CircleShape", lambda: b2CircleShape), radius = _a_(632800, _n_(632799, "self", lambda: self), "r")), density=2.0, friction = 0.5))
        _l_(632804)