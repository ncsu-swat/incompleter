# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70735803/why-am-i-getting-an-attributeerror-alien-object-has-no-attribute-draw-bullet
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pygame
    _l_(464220)

except ImportError:
    pass
try:
    from pygame.sprite import Sprite
    _l_(464222)

except ImportError:
    pass

class Bullet(_n_(464223, "Sprite", lambda: Sprite)):
    _l_(464291)

    """A class to manage bullets fired from the ship."""
    
    def __init__(self, ai_settings, screen, ship):
        _l_(464269)

        """Create a bullet object at the ship's current position."""
        _c_(464228, _a_(464227, _n_(464224, "super", lambda: super)(_n_(464225, "Bullet", lambda: Bullet), _n_(464226, "self", lambda: self)), "__init__"))
        _l_(464229)
        _n_(464230, "self", lambda: self).screen = _n_(464231, "screen", lambda: screen)
        _l_(464232)
        
        # Create a bullet rect at (0,0) and then set correct position.
        _n_(464233, "self", lambda: self).rect = _c_(464240, _a_(464235, _n_(464234, "pygame", lambda: pygame), "Rect"), 0, 0, _a_(464237, _n_(464236, "ai_settings", lambda: ai_settings), "bullet_width"), _a_(464239, _n_(464238, "ai_settings", lambda: ai_settings), "bullet_height"))
        _l_(464241)
        _a_(464243, _n_(464242, "self", lambda: self), "rect").centerx = _a_(464246, _a_(464245, _n_(464244, "ship", lambda: ship), "rect"), "centerx")
        _l_(464247)
        _a_(464249, _n_(464248, "self", lambda: self), "rect").top = _a_(464252, _a_(464251, _n_(464250, "ship", lambda: ship), "rect"), "top")
        _l_(464253)
        
        # Store the bullet's position as a decimal value.
        _n_(464254, "self", lambda: self).y = _c_(464259, _n_(464255, "float", lambda: float), _a_(464258, _a_(464257, _n_(464256, "self", lambda: self), "rect"), "y"))
        _l_(464260)
        
        _n_(464261, "self", lambda: self).color = _a_(464263, _n_(464262, "ai_settings", lambda: ai_settings), "bullet_color")
        _l_(464264)
        _n_(464265, "self", lambda: self).speed_factor = _a_(464267, _n_(464266, "ai_settings", lambda: ai_settings), "bullet_speed_factor")
        _l_(464268)
    def update(self):
        _l_(464278)

        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        _n_(464270, "self", lambda: self).y -= _n_(464271, "self", lambda: self).speed_factor
        _l_(464272)
        #Update the rect position.
        _a_(464274, _n_(464273, "self", lambda: self), "rect").y = _a_(464276, _n_(464275, "self", lambda: self), "y")
        _l_(464277)
    def draw_bullet(self):
        _l_(464290)

        """Draw the bullet to the screen."""
        _c_(464288, _a_(464281, _a_(464280, _n_(464279, "pygame", lambda: pygame), "draw"), "rect"), _a_(464283, _n_(464282, "self", lambda: self), "screen"), _a_(464285, _n_(464284, "self", lambda: self), "color"), _a_(464287, _n_(464286, "self", lambda: self), "rect"))
        _l_(464289)