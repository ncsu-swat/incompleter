# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62503772/attributeerror-after-getting-hit-in-alien-invasion-game
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pygame
    _l_(701017)

except ImportError:
    pass
try:
    from pygame.sprite import Sprite
    _l_(701019)

except ImportError:
    pass

class Bullet(_n_(701020, "Sprite", lambda: Sprite)):
    _l_(701021)

    """A class to manage bullets fired from the ship"""

def __init__(self, ai_settings, screen, ship):
    _l_(701065)

    """Create a bullet object at the ship's current position."""
    _c_(701024, _a_(701023, _n_(701022, "super", lambda: super)(), "__init__"))
    _l_(701025)
    _n_(701026, "self", lambda: self).screen = _n_(701027, "screen", lambda: screen)
    _l_(701028)
    
    # Create a bullet rect at (0, 0) and then set the correct position.
    _n_(701029, "self", lambda: self).rect = _c_(701036, _a_(701031, _n_(701030, "pygame", lambda: pygame), "Rect"), 0, 0, _a_(701033, _n_(701032, "ai_settings", lambda: ai_settings), "bullet_width"), 
        _a_(701035, _n_(701034, "ai_settings", lambda: ai_settings), "bullet_height"))
    _l_(701037)
    _a_(701039, _n_(701038, "self", lambda: self), "rect").centerx = _a_(701042, _a_(701041, _n_(701040, "ship", lambda: ship), "rect"), "centerx")
    _l_(701043)
    _a_(701045, _n_(701044, "self", lambda: self), "rect").top = _a_(701048, _a_(701047, _n_(701046, "ship", lambda: ship), "rect"), "top")
    _l_(701049)
    
    # Store the bullet's position as a decimal value.
    _n_(701050, "self", lambda: self).y = _c_(701055, _n_(701051, "float", lambda: float), _a_(701054, _a_(701053, _n_(701052, "self", lambda: self), "rect"), "y"))
    _l_(701056)
    
    _n_(701057, "self", lambda: self).color = _a_(701059, _n_(701058, "ai_settings", lambda: ai_settings), "bullet_color")
    _l_(701060)
    _n_(701061, "self", lambda: self).speed_factor = _a_(701063, _n_(701062, "ai_settings", lambda: ai_settings), "bullet_speed_factor")
    _l_(701064)

def update(self):
    _l_(701074)

    """Move the bullet up the screen."""
    # Update the decimal position of the bullet.
    _n_(701066, "self", lambda: self).y -= _n_(701067, "self", lambda: self).speed_factor
    _l_(701068)
    # Update the rect position.
    _a_(701070, _n_(701069, "self", lambda: self), "rect").y = _a_(701072, _n_(701071, "self", lambda: self), "y")
    _l_(701073)
def draw_bullet(self):
    _l_(701086)

    """Draw the bullet to the screen."""
    _c_(701084, _a_(701077, _a_(701076, _n_(701075, "pygame", lambda: pygame), "draw"), "rect"), _a_(701079, _n_(701078, "self", lambda: self), "screen"), _a_(701081, _n_(701080, "self", lambda: self), "color"), _a_(701083, _n_(701082, "self", lambda: self), "rect"))
    _l_(701085)