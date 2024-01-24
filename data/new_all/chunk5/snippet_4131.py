# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62503772/attributeerror-after-getting-hit-in-alien-invasion-game
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pygame
    _l_(652026)

except ImportError:
    pass
try:
    from pygame.sprite import Sprite
    _l_(652028)

except ImportError:
    pass

class Bullet(_n_(652029, "Sprite", lambda: Sprite)):
    _l_(652030)

    """A class to manage bullets fired from the ship"""

def __init__(self, ai_settings, screen, ship):
    _l_(652074)

    """Create a bullet object at the ship's current position."""
    _c_(652033, _a_(652032, _n_(652031, "super", lambda: super)(), "__init__"))
    _l_(652034)
    _n_(652035, "self", lambda: self).screen = _n_(652036, "screen", lambda: screen)
    _l_(652037)
    
    # Create a bullet rect at (0, 0) and then set the correct position.
    _n_(652038, "self", lambda: self).rect = _c_(652045, _a_(652040, _n_(652039, "pygame", lambda: pygame), "Rect"), 0, 0, _a_(652042, _n_(652041, "ai_settings", lambda: ai_settings), "bullet_width"), 
        _a_(652044, _n_(652043, "ai_settings", lambda: ai_settings), "bullet_height"))
    _l_(652046)
    _a_(652048, _n_(652047, "self", lambda: self), "rect").centerx = _a_(652051, _a_(652050, _n_(652049, "ship", lambda: ship), "rect"), "centerx")
    _l_(652052)
    _a_(652054, _n_(652053, "self", lambda: self), "rect").top = _a_(652057, _a_(652056, _n_(652055, "ship", lambda: ship), "rect"), "top")
    _l_(652058)
    
    # Store the bullet's position as a decimal value.
    _n_(652059, "self", lambda: self).y = _c_(652064, _n_(652060, "float", lambda: float), _a_(652063, _a_(652062, _n_(652061, "self", lambda: self), "rect"), "y"))
    _l_(652065)
    
    _n_(652066, "self", lambda: self).color = _a_(652068, _n_(652067, "ai_settings", lambda: ai_settings), "bullet_color")
    _l_(652069)
    _n_(652070, "self", lambda: self).speed_factor = _a_(652072, _n_(652071, "ai_settings", lambda: ai_settings), "bullet_speed_factor")
    _l_(652073)

def update(self):
    _l_(652083)

    """Move the bullet up the screen."""
    # Update the decimal position of the bullet.
    _n_(652075, "self", lambda: self).y -= _n_(652076, "self", lambda: self).speed_factor
    _l_(652077)
    # Update the rect position.
    _a_(652079, _n_(652078, "self", lambda: self), "rect").y = _a_(652081, _n_(652080, "self", lambda: self), "y")
    _l_(652082)
def draw_bullet(self):
    _l_(652095)

    """Draw the bullet to the screen."""
    _c_(652093, _a_(652086, _a_(652085, _n_(652084, "pygame", lambda: pygame), "draw"), "rect"), _a_(652088, _n_(652087, "self", lambda: self), "screen"), _a_(652090, _n_(652089, "self", lambda: self), "color"), _a_(652092, _n_(652091, "self", lambda: self), "rect"))
    _l_(652094)