# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58480212/attributeerror-python-crash-course
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pygame
    _l_(469404)

except ImportError:
    pass
try:
    from pygame.sprite import Sprite
    _l_(469406)

except ImportError:
    pass

class Bullet(_n_(469407, "Sprite", lambda: Sprite)):
    _l_(469473)


    def __init__(self, ai_game):
        _l_(469450)

        _c_(469410, _a_(469409, _n_(469408, "super", lambda: super)(), "__init__"))
        _l_(469411)
        _n_(469412, "self", lambda: self).screen = _a_(469414, _n_(469413, "ai_game", lambda: ai_game), "screen")
        _l_(469415)
        _n_(469416, "self", lambda: self).settings = _a_(469418, _n_(469417, "ai_game", lambda: ai_game), "settings")
        _l_(469419)
        _n_(469420, "self", lambda: self).color = _a_(469423, _a_(469422, _n_(469421, "self", lambda: self), "settings"), "bullet_color")
        _l_(469424)

        # Create a bullet rect at (0,0) and then set correct position
        _n_(469425, "self", lambda: self).rect = _c_(469434, _a_(469427, _n_(469426, "pygame", lambda: pygame), "Rect"), 0, 0, _a_(469430, _a_(469429, _n_(469428, "self", lambda: self), "settings"), "bullet_width"),
            _a_(469433, _a_(469432, _n_(469431, "self", lambda: self), "settings"), "bullet_height"))
        _l_(469435)
        _a_(469437, _n_(469436, "self", lambda: self), "rect").midtop = _a_(469441, _a_(469440, _a_(469439, _n_(469438, "ai_game", lambda: ai_game), "ship"), "rect"), "midtop")
        _l_(469442)

        # Store the bullet's position as a decimal value
        _n_(469443, "self", lambda: self).y = _c_(469448, _n_(469444, "float", lambda: float), _a_(469447, _a_(469446, _n_(469445, "self", lambda: self), "rect"), "y"))
        _l_(469449)

    def update(self):
        _l_(469460)

        _n_(469451, "self", lambda: self).y -= _a_(469453, _n_(469452, "self", lambda: self), "settings").bullet_speed
        _l_(469454)
        _a_(469456, _n_(469455, "self", lambda: self), "rect").y = _a_(469458, _n_(469457, "self", lambda: self), "y")
        _l_(469459)

    def draw_bullet(self):
        _l_(469472)

        _c_(469470, _a_(469463, _a_(469462, _n_(469461, "pygame", lambda: pygame), "draw"), "rect"), _a_(469465, _n_(469464, "self", lambda: self), "screen"), _a_(469467, _n_(469466, "self", lambda: self), "color"), _a_(469469, _n_(469468, "self", lambda: self), "rect"))
        _l_(469471)