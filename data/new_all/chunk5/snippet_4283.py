# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60262615/how-to-fix-a-nameerror-name-color-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
size = (1280, 850)
_l_(702664)
Win = _c_(702669, _a_(702667, _a_(702666, _n_(702665, "pygame", lambda: pygame), "display"), "set_mode"), _n_(702668, "size", lambda: size))
_l_(702670)
class Particle:
    _l_(702712)

    color = (255, 255, 0)
    _l_(702671)
    ID = 0
    _l_(702672)

    def __init__(self, rect):
        _l_(702685)

        _n_(702673, "Particle", lambda: Particle).ID += 1
        _l_(702674)
        _n_(702675, "self", lambda: self).color = _n_(702676, "color", lambda: (color))
        _l_(702677)
        _n_(702678, "self", lambda: self).ID = _a_(702680, _n_(702679, "Particle", lambda: Particle), "ID")
        _l_(702681)
        _n_(702682, "self", lambda: self).rect = _n_(702683, "rect", lambda: rect)
        _l_(702684)

    def move(self, x, y):
        _l_(702693)

        _c_(702691, _a_(702688, _a_(702687, _n_(702686, "self", lambda: self), "rect"), "move"), _n_(702689, "x", lambda: x), _n_(702690, "y", lambda: y))
        _l_(702692)

    def draw(self):
        _l_(702704)

        _c_(702702, _a_(702696, _a_(702695, _n_(702694, "pygame", lambda: pygame), "draw"), "rect"), _n_(702697, "Win", lambda: Win), _a_(702699, _n_(702698, "self", lambda: self), "color"), _a_(702701, _n_(702700, "self", lambda: self), "rect"))
        _l_(702703)

    def collide(self, rect1):
        _l_(702711)

        aux = _c_(702709, _a_(702707, _a_(702706, _n_(702705, "self", lambda: self), "rect"), "colliderect"), _n_(702708, "rect1", lambda: rect1))
        _l_(702710)
        return aux