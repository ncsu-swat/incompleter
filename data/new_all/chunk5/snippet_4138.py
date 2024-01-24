# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62503772/attributeerror-after-getting-hit-in-alien-invasion-game
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pygame
    _l_(697096)

except ImportError:
    pass
try:
    from pygame.sprite import Sprite
    _l_(697098)

except ImportError:
    pass

class Alien(_n_(697099, "Sprite", lambda: Sprite)):
    _l_(697100)

    """A class to represent a single alien in the fleet."""

def __init__(self, ai_settings, screen):
    _l_(697144)

    """Intialize the alien and set its starting position."""
    _c_(697105, _a_(697104, _n_(697101, "super", lambda: super)(_n_(697102, "Alien", lambda: Alien), _n_(697103, "self", lambda: self)), "__init__"))
    _l_(697106)
    _n_(697107, "self", lambda: self).screen = _n_(697108, "screen", lambda: screen)
    _l_(697109)
    _n_(697110, "self", lambda: self).ai_settings = _n_(697111, "ai_settings", lambda: ai_settings)
    _l_(697112)
    
    # Load the alien image and set its rect attribute.
    _n_(697113, "self", lambda: self).image = _c_(697117, _a_(697116, _a_(697115, _n_(697114, "pygame", lambda: pygame), "image"), "load"), 'images/alien.bmp')
    _l_(697118)
    _n_(697119, "self", lambda: self).rect = _c_(697123, _a_(697122, _a_(697121, _n_(697120, "self", lambda: self), "image"), "get_rect"))
    _l_(697124)
    
    # Start each new alien near the top left of the screen.
    _a_(697126, _n_(697125, "self", lambda: self), "rect").x = _a_(697129, _a_(697128, _n_(697127, "self", lambda: self), "rect"), "width")
    _l_(697130)
    _a_(697132, _n_(697131, "self", lambda: self), "rect").y = _a_(697135, _a_(697134, _n_(697133, "self", lambda: self), "rect"), "height")
    _l_(697136)
    
    # Store the alien's exact position.
    _n_(697137, "self", lambda: self).x = _c_(697142, _n_(697138, "float", lambda: float), _a_(697141, _a_(697140, _n_(697139, "self", lambda: self), "rect"), "x"))
    _l_(697143)
def blitme(self):
    _l_(697154)

    """Draw the alien at its current position."""
    _c_(697152, _a_(697147, _a_(697146, _n_(697145, "self", lambda: self), "screen"), "blit"), _a_(697149, _n_(697148, "self", lambda: self), "image"), _a_(697151, _n_(697150, "self", lambda: self), "rect"))
    _l_(697153)
def check_edges(self):
    _l_(697172)

    """Return True if alien is at edge of screen."""
    screen_rect = _c_(697158, _a_(697157, _a_(697156, _n_(697155, "self", lambda: self), "screen"), "get_rect"))
    _l_(697159)
    if _a_(697162, _a_(697161, _n_(697160, "self", lambda: self), "rect"), "right") >= _a_(697164, _n_(697163, "screen_rect", lambda: screen_rect), "right"):
        _l_(697171)

        aux = True
        _l_(697165)
        return aux
    elif _a_(697168, _a_(697167, _n_(697166, "self", lambda: self), "rect"), "left") <= 0:
        _l_(697170)

        aux = True
        _l_(697169)
        return aux
def update(self):
    _l_(697186)

    """Move the alien right or left."""
    _n_(697173, "self", lambda: self).x += (_a_(697176, _a_(697175, _n_(697174, "self", lambda: self), "ai_settings"), "alien_speed_factor") * 
                    _a_(697179, _a_(697178, _n_(697177, "self", lambda: self), "ai_settings"), "fleet_direction"))
    _l_(697180)
    _a_(697182, _n_(697181, "self", lambda: self), "rect").x = _a_(697184, _n_(697183, "self", lambda: self), "x")
    _l_(697185)