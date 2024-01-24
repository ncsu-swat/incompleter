# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76667512/attributeerror-settings-object-has-no-attribute-rect
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pygame
    _l_(599846)

except ImportError:
    pass

class Ship:
    _l_(599916)

    def __init__(self, screen):
        _l_(599883)

        _n_(599847, "self", lambda: self).screen = _n_(599848, "screen", lambda: screen)
        _l_(599849)

        _n_(599850, "self", lambda: self).image = _c_(599854, _a_(599853, _a_(599852, _n_(599851, "pygame", lambda: pygame), "image"), "load"), 'images/ship.png')
        _l_(599855)
        _n_(599856, "self", lambda: self).rect = _c_(599860, _a_(599859, _a_(599858, _n_(599857, "self", lambda: self), "image"), "get_rect"))
        _l_(599861)
        _n_(599862, "self", lambda: self).screen_rect = _c_(599865, _a_(599864, _n_(599863, "screen", lambda: screen), "get_rect"))
        _l_(599866)

        _a_(599868, _n_(599867, "self", lambda: self), "rect").centerx = _a_(599871, _a_(599870, _n_(599869, "self", lambda: self), "screen_rect"), "centerx")
        _l_(599872)
        _a_(599874, _n_(599873, "self", lambda: self), "rect").bottom = _a_(599877, _a_(599876, _n_(599875, "self", lambda: self), "screen_rect"), "bottom")
        _l_(599878)

        _n_(599879, "self", lambda: self).moving_right = False
        _l_(599880)
        _n_(599881, "self", lambda: self).moving_left = False
        _l_(599882)

    def update(self):
        _l_(599905)

        if _a_(599885, _n_(599884, "self", lambda: self), "moving_right") and _a_(599888, _a_(599887, _n_(599886, "self", lambda: self), "rect"), "right") < _a_(599891, _a_(599890, _n_(599889, "self", lambda: self), "screen_rect"), "right"):
            _l_(599895)

            _a_(599893, _n_(599892, "self", lambda: self), "rect").centerx += 2
            _l_(599894)

        if _a_(599897, _n_(599896, "self", lambda: self), "moving_left") and _a_(599900, _a_(599899, _n_(599898, "self", lambda: self), "rect"), "left") > 0:
            _l_(599904)

            _a_(599902, _n_(599901, "self", lambda: self), "rect").centerx -= 2
            _l_(599903)

    def blitme(self):
        _l_(599915)

        _c_(599913, _a_(599908, _a_(599907, _n_(599906, "self", lambda: self), "screen"), "blit"), _a_(599910, _n_(599909, "self", lambda: self), "image"), _a_(599912, _n_(599911, "self", lambda: self), "rect"))
        _l_(599914)