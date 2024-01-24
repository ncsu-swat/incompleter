# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60262615/how-to-fix-a-nameerror-name-color-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
size = (1280, 850)
_l_(697789)
Win = _c_(697794, _a_(697792, _a_(697791, _n_(697790, "pygame", lambda: pygame), "display"), "set_mode"), _n_(697793, "size", lambda: size))
_l_(697795)
class Particle:
    _l_(697837)

    color = (255, 255, 0)
    _l_(697796)
    ID = 0
    _l_(697797)

    def __init__(self, rect):
        _l_(697810)

        _n_(697798, "Particle", lambda: Particle).ID += 1
        _l_(697799)
        _n_(697800, "self", lambda: self).color = _n_(697801, "color", lambda: (color))
        _l_(697802)
        _n_(697803, "self", lambda: self).ID = _a_(697805, _n_(697804, "Particle", lambda: Particle), "ID")
        _l_(697806)
        _n_(697807, "self", lambda: self).rect = _n_(697808, "rect", lambda: rect)
        _l_(697809)

    def move(self, x, y):
        _l_(697818)

        _c_(697816, _a_(697813, _a_(697812, _n_(697811, "self", lambda: self), "rect"), "move"), _n_(697814, "x", lambda: x), _n_(697815, "y", lambda: y))
        _l_(697817)

    def draw(self):
        _l_(697829)

        _c_(697827, _a_(697821, _a_(697820, _n_(697819, "pygame", lambda: pygame), "draw"), "rect"), _n_(697822, "Win", lambda: Win), _a_(697824, _n_(697823, "self", lambda: self), "color"), _a_(697826, _n_(697825, "self", lambda: self), "rect"))
        _l_(697828)

    def collide(self, rect1):
        _l_(697836)

        aux = _c_(697834, _a_(697832, _a_(697831, _n_(697830, "self", lambda: self), "rect"), "colliderect"), _n_(697833, "rect1", lambda: rect1))
        _l_(697835)
        return aux