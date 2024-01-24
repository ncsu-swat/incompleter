# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60326330/need-help-resolving-attribute-error-within-pygameinheritance
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class projectile(_n_(358977, "player", lambda: player)):
    _l_(359023)

    def __init__(self,bulletx, bullety):
        _l_(358988)

        _n_(358978, "self", lambda: self).bulletx = _n_(358979, "bulletx", lambda: bulletx)
        _l_(358980)
        _n_(358981, "self", lambda: self).bullety = _n_(358982, "bullety", lambda: bullety)
        _l_(358983)
        _n_(358984, "self", lambda: self).facing = 1
        _l_(358985)
        _n_(358986, "self", lambda: self).shooting = False
        _l_(358987)
    def shoot(self):
        _l_(359009)

        _n_(358989, "self", lambda: self).vel = 30 * _a_(358991, _n_(358990, "self", lambda: self), "facing")
        _l_(358992)
        if _a_(358994, _n_(358993, "self", lambda: self), "left"):
            _l_(358999)

            _n_(358995, "self", lambda: self).facing = -1
            _l_(358996)
        else:
            _n_(358997, "self", lambda: self).facing = 1
            _l_(358998)
        _n_(359000, "self", lambda: self).bulletx += _n_(359001, "self", lambda: self).vel
        _l_(359002)
        if _n_(359003, "self", lambda: self) < 0 or _a_(359005, _n_(359004, "bullet", lambda: bullet), "x") > 500:
            _l_(359008)

            _n_(359006, "self", lambda: self).shooting = True
            _l_(359007)
    def draw(self):
        _l_(359022)

        if _a_(359011, _n_(359010, "self", lambda: self), "shooting") == True:
            _l_(359021)

            _c_(359019, _a_(359013, _n_(359012, "win", lambda: win), "blit"), _n_(359014, "thunderball", lambda: thunderball),(_a_(359016, _n_(359015, "self", lambda: self), "bulletx"),_a_(359018, _n_(359017, "self", lambda: self), "bullety")))
            _l_(359020)