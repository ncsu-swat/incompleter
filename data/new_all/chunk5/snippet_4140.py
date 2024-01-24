# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62480756/nameerror-name-bullets-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pygame
    _l_(647403)

except ImportError:
    pass
try:
    from pygame.sprite import Sprite
    _l_(647405)

except ImportError:
    pass

class Bullet(_n_(647406, "Sprite", lambda: Sprite)):
    _l_(647407)

    """A class to manage bullets fired from the ship"""

def __init__(self, ai_settings, screen, ship):
    _l_(647451)

    """Create a bullet object at the ship's current position."""
    _c_(647410, _a_(647409, _n_(647408, "super", lambda: super)(), "__init__"))
    _l_(647411)
    _n_(647412, "self", lambda: self).screen = _n_(647413, "screen", lambda: screen)
    _l_(647414)

    # Create a bullet rect at (0, 0) and then set the correct position.
    _n_(647415, "self", lambda: self).rect = _c_(647422, _a_(647417, _n_(647416, "pygame", lambda: pygame), "Rect"), 0, 0, _a_(647419, _n_(647418, "ai_settings", lambda: ai_settings), "bullet_width"), 
        _a_(647421, _n_(647420, "ai_settings", lambda: ai_settings), "bullet_height"))
    _l_(647423)
    _a_(647425, _n_(647424, "self", lambda: self), "rect").centerx = _a_(647428, _a_(647427, _n_(647426, "ship", lambda: ship), "rect"), "centerx")
    _l_(647429)
    _a_(647431, _n_(647430, "self", lambda: self), "rect").top = _a_(647434, _a_(647433, _n_(647432, "ship", lambda: ship), "rect"), "top")
    _l_(647435)

    # Store the bullet's position as a decimal value.
    _n_(647436, "self", lambda: self).y = _c_(647441, _n_(647437, "float", lambda: float), _a_(647440, _a_(647439, _n_(647438, "self", lambda: self), "rect"), "y"))
    _l_(647442)

    _n_(647443, "self", lambda: self).color = _a_(647445, _n_(647444, "ai_settings", lambda: ai_settings), "bullet_color")
    _l_(647446)
    _n_(647447, "self", lambda: self).speed_factor = _a_(647449, _n_(647448, "ai_settings", lambda: ai_settings), "bullet_speed_factor")
    _l_(647450)

def update(self):
    _l_(647460)

    """Move the bullet up the screen."""
    # Update the decimal position of the bullet.
    _n_(647452, "self", lambda: self).y -= _n_(647453, "self", lambda: self).speed_factor
    _l_(647454)
    # Update the rect position.
    _a_(647456, _n_(647455, "self", lambda: self), "rect").y = _a_(647458, _n_(647457, "self", lambda: self), "y")
    _l_(647459)

def draw_bullet(self):
    _l_(647472)

    """Draw the bullet to the screen."""
    _c_(647470, _a_(647463, _a_(647462, _n_(647461, "pygame", lambda: pygame), "draw"), "rect"), _a_(647465, _n_(647464, "self", lambda: self), "screen"), _a_(647467, _n_(647466, "self", lambda: self), "color"), _a_(647469, _n_(647468, "self", lambda: self), "rect"))
    _l_(647471)