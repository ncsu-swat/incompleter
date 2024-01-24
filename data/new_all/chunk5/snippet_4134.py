# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62480756/nameerror-name-bullets-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pygame
    _l_(656845)

except ImportError:
    pass
try:
    from pygame.sprite import Sprite
    _l_(656847)

except ImportError:
    pass

class Bullet(_n_(656848, "Sprite", lambda: Sprite)):
    _l_(656849)

    """A class to manage bullets fired from the ship"""

def __init__(self, ai_settings, screen, ship):
    _l_(656893)

    """Create a bullet object at the ship's current position."""
    _c_(656852, _a_(656851, _n_(656850, "super", lambda: super)(), "__init__"))
    _l_(656853)
    _n_(656854, "self", lambda: self).screen = _n_(656855, "screen", lambda: screen)
    _l_(656856)

    # Create a bullet rect at (0, 0) and then set the correct position.
    _n_(656857, "self", lambda: self).rect = _c_(656864, _a_(656859, _n_(656858, "pygame", lambda: pygame), "Rect"), 0, 0, _a_(656861, _n_(656860, "ai_settings", lambda: ai_settings), "bullet_width"), 
        _a_(656863, _n_(656862, "ai_settings", lambda: ai_settings), "bullet_height"))
    _l_(656865)
    _a_(656867, _n_(656866, "self", lambda: self), "rect").centerx = _a_(656870, _a_(656869, _n_(656868, "ship", lambda: ship), "rect"), "centerx")
    _l_(656871)
    _a_(656873, _n_(656872, "self", lambda: self), "rect").top = _a_(656876, _a_(656875, _n_(656874, "ship", lambda: ship), "rect"), "top")
    _l_(656877)

    # Store the bullet's position as a decimal value.
    _n_(656878, "self", lambda: self).y = _c_(656883, _n_(656879, "float", lambda: float), _a_(656882, _a_(656881, _n_(656880, "self", lambda: self), "rect"), "y"))
    _l_(656884)

    _n_(656885, "self", lambda: self).color = _a_(656887, _n_(656886, "ai_settings", lambda: ai_settings), "bullet_color")
    _l_(656888)
    _n_(656889, "self", lambda: self).speed_factor = _a_(656891, _n_(656890, "ai_settings", lambda: ai_settings), "bullet_speed_factor")
    _l_(656892)

def update(self):
    _l_(656902)

    """Move the bullet up the screen."""
    # Update the decimal position of the bullet.
    _n_(656894, "self", lambda: self).y -= _n_(656895, "self", lambda: self).speed_factor
    _l_(656896)
    # Update the rect position.
    _a_(656898, _n_(656897, "self", lambda: self), "rect").y = _a_(656900, _n_(656899, "self", lambda: self), "y")
    _l_(656901)

def draw_bullet(self):
    _l_(656914)

    """Draw the bullet to the screen."""
    _c_(656912, _a_(656905, _a_(656904, _n_(656903, "pygame", lambda: pygame), "draw"), "rect"), _a_(656907, _n_(656906, "self", lambda: self), "screen"), _a_(656909, _n_(656908, "self", lambda: self), "color"), _a_(656911, _n_(656910, "self", lambda: self), "rect"))
    _l_(656913)