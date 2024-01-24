# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/21609227/python-3-3-3-typeerror-list-indices-must-be-integers-not-float
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Block(_a_(457863, _a_(457862, _n_(457861, "pygame", lambda: pygame), "sprite"), "Sprite")):
    _l_(457901)

    def __init__(self, x, y):
        _l_(457891)

        _c_(457869, _a_(457867, _a_(457866, _a_(457865, _n_(457864, "pygame", lambda: pygame), "sprite"), "Sprite"), "__init__"), _n_(457868, "self", lambda: self))
        _l_(457870)

        _n_(457871, "self", lambda: self).image = _c_(457875, _a_(457874, _a_(457873, _n_(457872, "pygame", lambda: pygame), "image"), "load"), 'data/images/moon.jpg')
        _l_(457876)

        _n_(457877, "self", lambda: self).rect = _c_(457881, _a_(457880, _a_(457879, _n_(457878, "self", lambda: self), "image"), "get_rect"))
        _l_(457882)
        _a_(457884, _n_(457883, "self", lambda: self), "rect").x = _n_(457885, "x", lambda: x)
        _l_(457886)
        _a_(457888, _n_(457887, "self", lambda: self), "rect").y = _n_(457889, "y", lambda: y)
        _l_(457890)

    def render(self, surface):
        _l_(457900)

        _c_(457898, _a_(457893, _n_(457892, "surface", lambda: surface), "blit"), _a_(457895, _n_(457894, "self", lambda: self), "image"), _a_(457897, _n_(457896, "self", lambda: self), "rect"))
        _l_(457899)