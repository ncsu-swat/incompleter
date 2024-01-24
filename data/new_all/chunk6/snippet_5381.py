# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60326330/need-help-resolving-attribute-error-within-pygameinheritance
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class projectile(_n_(350685, "player", lambda: player)):
    _l_(350731)

    def __init__(self,bulletx, bullety):
        _l_(350696)

        _n_(350686, "self", lambda: self).bulletx = _n_(350687, "bulletx", lambda: bulletx)
        _l_(350688)
        _n_(350689, "self", lambda: self).bullety = _n_(350690, "bullety", lambda: bullety)
        _l_(350691)
        _n_(350692, "self", lambda: self).facing = 1
        _l_(350693)
        _n_(350694, "self", lambda: self).shooting = False
        _l_(350695)
    def shoot(self):
        _l_(350717)

        _n_(350697, "self", lambda: self).vel = 30 * _a_(350699, _n_(350698, "self", lambda: self), "facing")
        _l_(350700)
        if _a_(350702, _n_(350701, "self", lambda: self), "left"):
            _l_(350707)

            _n_(350703, "self", lambda: self).facing = -1
            _l_(350704)
        else:
            _n_(350705, "self", lambda: self).facing = 1
            _l_(350706)
        _n_(350708, "self", lambda: self).bulletx += _n_(350709, "self", lambda: self).vel
        _l_(350710)
        if _n_(350711, "self", lambda: self) < 0 or _a_(350713, _n_(350712, "bullet", lambda: bullet), "x") > 500:
            _l_(350716)

            _n_(350714, "self", lambda: self).shooting = True
            _l_(350715)
    def draw(self):
        _l_(350730)

        if _a_(350719, _n_(350718, "self", lambda: self), "shooting") == True:
            _l_(350729)

            _c_(350727, _a_(350721, _n_(350720, "win", lambda: win), "blit"), _n_(350722, "thunderball", lambda: thunderball),(_a_(350724, _n_(350723, "self", lambda: self), "bulletx"),_a_(350726, _n_(350725, "self", lambda: self), "bullety")))
            _l_(350728)