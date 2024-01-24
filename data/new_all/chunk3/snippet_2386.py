# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/47103106/python3-subclass-is-being-instantiated-as-superclass-subclass-method-not-found
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from player import Player
    _l_(573288)

except ImportError:
    pass
try:
    from hand import Hand
    _l_(573290)

except ImportError:
    pass

class Dealer(_n_(573291, "Player", lambda: Player)):
    _l_(573310)


    def __init__(self):
        _l_(573296)

        _c_(573294, _a_(573293, _n_(573292, "super", lambda: super)(), "__init__"))
        _l_(573295)

    def deal(self, twocards):
        _l_(573309)

        _n_(573297, "self", lambda: self).hands = [_c_(573299, _n_(573298, "Hand", lambda: Hand), showfirst=False)]
        _l_(573300)
        _a_(573302, _n_(573301, "self", lambda: self), "hands")[0] += _n_(573303, "twocards", lambda: twocards)
        _l_(573304)
        _c_(573307, _a_(573306, _n_(573305, "self", lambda: self), "seecards"), 0)
        _l_(573308)