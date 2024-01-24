# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69791420/i-am-getting-an-attribute-error-message-when-i-want-to-make-my-sprite-character
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pygame
    _l_(600201)

except ImportError:
    pass

#screen settings
WIDTH = 1000
_l_(600202)
HEIGHT = 400
_l_(600203)

screen = _c_(600209, _a_(600206, _a_(600205, _n_(600204, "pygame", lambda: pygame), "display"), "set_mode"), (_n_(600207, "WIDTH", lambda: WIDTH), _n_(600208, "HEIGHT", lambda: HEIGHT)))
_l_(600210)
_c_(600214, _a_(600213, _a_(600212, _n_(600211, "pygame", lambda: pygame), "display"), "set_caption"), "AutoPilot")
_l_(600215)
_c_(600218, _a_(600217, _n_(600216, "screen", lambda: screen), "fill"), (255, 255, 255))
_l_(600219)

#debris class
class Debris(_a_(600222, _a_(600221, _n_(600220, "pygame", lambda: pygame), "sprite"), "Sprite")):
    _l_(600307)

    def __init__(self, scale, speed):
        _l_(600295)

        _c_(600228, _a_(600226, _a_(600225, _a_(600224, _n_(600223, "pygame", lambda: pygame), "sprite"), "Sprite"), "__init__"), _n_(600227, "self", lambda: self))
        _l_(600229)

        _n_(600230, "self", lambda: self).x = 400
        _l_(600231)
        _n_(600232, "self", lambda: self).y = _n_(600233, "HEIGHT", lambda: HEIGHT) / 2 - 200
        _l_(600234)
        _n_(600235, "self", lambda: self).speed = _n_(600236, "speed", lambda: speed)
        _l_(600237)
        _n_(600238, "self", lambda: self).vy = 0
        _l_(600239)
        _n_(600240, "self", lambda: self).on_ground = True
        _l_(600241)
        _n_(600242, "self", lambda: self).move = True
        _l_(600243)
        _n_(600244, "self", lambda: self).health = 100
        _l_(600245)
        _n_(600246, "self", lambda: self).max_health = _a_(600248, _n_(600247, "self", lambda: self), "health")
        _l_(600249)
        _n_(600250, "self", lambda: self).alive = True
        _l_(600251)

        #load debris
        _n_(600252, "self", lambda: self).images = []
        _l_(600253)
        img = _c_(600259, _a_(600258, _c_(600257, _a_(600256, _a_(600255, _n_(600254, "pygame", lambda: pygame), "image"), "load"), 'debris/cement.png'), "convert_alpha"))
        _l_(600260)
        img = _c_(600277, _a_(600263, _a_(600262, _n_(600261, "pygame", lambda: pygame), "transform"), "scale"), _n_(600264, "img", lambda: img), (_c_(600269, _n_(600265, "int", lambda: int), _c_(600268, _a_(600267, _n_(600266, "img", lambda: img), "get_width"))) * _n_(600270, "scale", lambda: scale), (_c_(600275, _n_(600271, "int", lambda: int), _c_(600274, _a_(600273, _n_(600272, "img", lambda: img), "get_height"))) * _n_(600276, "scale", lambda: scale))))
        _l_(600278)
        _c_(600283, _a_(600281, _a_(600280, _n_(600279, "self", lambda: self), "images"), "append"), _n_(600282, "img", lambda: img))
        _l_(600284)
        _n_(600285, "self", lambda: self).image = _a_(600287, _n_(600286, "self", lambda: self), "images")[0]
        _l_(600288)
        _n_(600289, "self", lambda: self).rect = _c_(600293, _a_(600292, _a_(600291, _n_(600290, "self", lambda: self), "image"), "get_rect"))
        _l_(600294)

    #draw debris to screen
    def draw(self):
        _l_(600306)

        _c_(600304, _a_(600297, _n_(600296, "screen", lambda: screen), "blit"), _a_(600299, _n_(600298, "self", lambda: self), "image"),(_a_(600301, _n_(600300, "self", lambda: self), "x"),_a_(600303, _n_(600302, "self", lambda: self), "y")))
        _l_(600305)