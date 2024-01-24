# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76667512/attributeerror-settings-object-has-no-attribute-rect
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pygame
    _l_(621422)

except ImportError:
    pass
try:
    from pygame.sprite import Sprite
    _l_(621424)

except ImportError:
    pass
try:
    from settings import Settings
    _l_(621426)

except ImportError:
    pass

class Bullet(_n_(621427, "Sprite", lambda: Sprite)):
    _l_(621496)

    def __init__(self, ai_settings, screen, ship):
        _l_(621474)

        _c_(621430, _a_(621429, _n_(621428, "super", lambda: super)(), "__init__"))
        _l_(621431)
        _n_(621432, "self", lambda: self).screen = _n_(621433, "screen", lambda: screen)
        _l_(621434)
        ai_settings = _c_(621436, _n_(621435, "Settings", lambda: Settings))
        _l_(621437)

        _n_(621438, "self", lambda: self).rect = _c_(621445, _a_(621440, _n_(621439, "pygame", lambda: pygame), "Rect"), 0, 0, _a_(621442, _n_(621441, "ai_settings", lambda: ai_settings), "bullet_width"), _a_(621444, _n_(621443, "ai_settings", lambda: ai_settings), "bullet_height"))
        _l_(621446)
        _a_(621448, _n_(621447, "self", lambda: self), "rect").centerx = _a_(621451, _a_(621450, _n_(621449, "ship", lambda: ship), "rect"), "centerx")
        _l_(621452)
        _a_(621454, _n_(621453, "self", lambda: self), "rect").bottom = _a_(621457, _a_(621456, _n_(621455, "ship", lambda: ship), "rect"), "bottom")
        _l_(621458)

        _n_(621459, "self", lambda: self).y = _c_(621464, _n_(621460, "float", lambda: float), _a_(621463, _a_(621462, _n_(621461, "self", lambda: self), "rect"), "y"))
        _l_(621465)

        _n_(621466, "self", lambda: self).color = _a_(621468, _n_(621467, "ai_settings", lambda: ai_settings), "bullet_color")
        _l_(621469)
        _n_(621470, "self", lambda: self).speed_factor = _a_(621472, _n_(621471, "ai_settings", lambda: ai_settings), "bullet_speed_factor")
        _l_(621473)

    def update(self):
        _l_(621483)

        _n_(621475, "self", lambda: self).y -= _n_(621476, "self", lambda: self).speed_factor
        _l_(621477)
        _a_(621479, _n_(621478, "self", lambda: self), "rect").y = _a_(621481, _n_(621480, "self", lambda: self), "y")
        _l_(621482)

    def draw_bullet(self):
        _l_(621495)

        _c_(621493, _a_(621486, _a_(621485, _n_(621484, "pygame", lambda: pygame), "draw"), "rect"), _a_(621488, _n_(621487, "self", lambda: self), "screen"), _a_(621490, _n_(621489, "self", lambda: self), "color"), _a_(621492, _n_(621491, "self", lambda: self), "rect"))
        _l_(621494)