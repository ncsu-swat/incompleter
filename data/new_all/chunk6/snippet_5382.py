# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60326330/need-help-resolving-attribute-error-within-pygameinheritance
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class projectile(_n_(365874, "player", lambda: player)):
    _l_(365920)

    def __init__(self,bulletx, bullety):
        _l_(365885)

        _n_(365875, "self", lambda: self).bulletx = _n_(365876, "bulletx", lambda: bulletx)
        _l_(365877)
        _n_(365878, "self", lambda: self).bullety = _n_(365879, "bullety", lambda: bullety)
        _l_(365880)
        _n_(365881, "self", lambda: self).facing = 1
        _l_(365882)
        _n_(365883, "self", lambda: self).shooting = False
        _l_(365884)
    def shoot(self):
        _l_(365906)

        _n_(365886, "self", lambda: self).vel = 30 * _a_(365888, _n_(365887, "self", lambda: self), "facing")
        _l_(365889)
        if _a_(365891, _n_(365890, "self", lambda: self), "left"):
            _l_(365896)

            _n_(365892, "self", lambda: self).facing = -1
            _l_(365893)
        else:
            _n_(365894, "self", lambda: self).facing = 1
            _l_(365895)
        _n_(365897, "self", lambda: self).bulletx += _n_(365898, "self", lambda: self).vel
        _l_(365899)
        if _n_(365900, "self", lambda: self) < 0 or _a_(365902, _n_(365901, "bullet", lambda: bullet), "x") > 500:
            _l_(365905)

            _n_(365903, "self", lambda: self).shooting = True
            _l_(365904)
    def draw(self):
        _l_(365919)

        if _a_(365908, _n_(365907, "self", lambda: self), "shooting") == True:
            _l_(365918)

            _c_(365916, _a_(365910, _n_(365909, "win", lambda: win), "blit"), _n_(365911, "thunderball", lambda: thunderball),(_a_(365913, _n_(365912, "self", lambda: self), "bulletx"),_a_(365915, _n_(365914, "self", lambda: self), "bullety")))
            _l_(365917)