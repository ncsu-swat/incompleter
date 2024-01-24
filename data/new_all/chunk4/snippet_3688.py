# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69791420/i-am-getting-an-attribute-error-message-when-i-want-to-make-my-sprite-character
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pygame
    _l_(611215)

except ImportError:
    pass
try:
    from autopilot import debris, bullet_group
    _l_(611217)

except ImportError:
    pass

#screen settings
WIDTH = 1000
_l_(611218)
HEIGHT = 400
_l_(611219)

screen = _c_(611225, _a_(611222, _a_(611221, _n_(611220, "pygame", lambda: pygame), "display"), "set_mode"), (_n_(611223, "WIDTH", lambda: WIDTH), _n_(611224, "HEIGHT", lambda: HEIGHT)))
_l_(611226)
_c_(611230, _a_(611229, _a_(611228, _n_(611227, "pygame", lambda: pygame), "display"), "set_caption"), "AutoPilot")
_l_(611231)
_c_(611234, _a_(611233, _n_(611232, "screen", lambda: screen), "fill"), (255, 255, 255))
_l_(611235)

#load bullets
bullets = _c_(611241, _a_(611240, _c_(611239, _a_(611238, _a_(611237, _n_(611236, "pygame", lambda: pygame), "image"), "load"), 'car/bullet.png'), "convert_alpha"))
_l_(611242)

#bullet class
class Bullet(_a_(611245, _a_(611244, _n_(611243, "pygame", lambda: pygame), "sprite"), "Sprite")):
    _l_(611298)

    def __init__(self, x, y, direction):
        _l_(611272)

        _c_(611251, _a_(611249, _a_(611248, _a_(611247, _n_(611246, "pygame", lambda: pygame), "sprite"), "Sprite"), "__init__"), _n_(611250, "self", lambda: self))
        _l_(611252)

        _n_(611253, "self", lambda: self).speed = 5
        _l_(611254)
        _n_(611255, "self", lambda: self).image = _n_(611256, "bullets", lambda: bullets)
        _l_(611257)
        _n_(611258, "self", lambda: self).rect = _c_(611262, _a_(611261, _a_(611260, _n_(611259, "self", lambda: self), "image"), "get_rect"))
        _l_(611263)
        _a_(611265, _n_(611264, "self", lambda: self), "rect").center = (_n_(611266, "x", lambda: x),_n_(611267, "y", lambda: y))
        _l_(611268)
        _n_(611269, "self", lambda: self).direction = _n_(611270, "direction", lambda: direction)
        _l_(611271)

    def update(self):
        _l_(611297)

        _a_(611274, _n_(611273, "self", lambda: self), "rect").centery -= _n_(611275, "self", lambda: self).speed
        _l_(611276)
        #check if bullet has gone off screen
        if _a_(611279, _a_(611278, _n_(611277, "self", lambda: self), "rect"), "top") < 1:
            _l_(611284)

            _c_(611282, _a_(611281, _n_(611280, "self", lambda: self), "kill"))
            _l_(611283)
        #check collision with cement block
        if _c_(611290, _a_(611287, _a_(611286, _n_(611285, "pygame", lambda: pygame), "sprite"), "spritecollide"), _n_(611288, "debris", lambda: debris), _n_(611289, "bullet_group", lambda: bullet_group), False):
            _l_(611296)

            if _a_(611292, _n_(611291, "debris", lambda: debris), "alive"):
                _l_(611295)

                _n_(611293, "debris", lambda: debris).health -= 25
                _l_(611294)