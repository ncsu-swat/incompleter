# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62503772/attributeerror-after-getting-hit-in-alien-invasion-game
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pygame
    _l_(707107)

except ImportError:
    pass
try:
    from pygame.sprite import Sprite
    _l_(707109)

except ImportError:
    pass

class Alien(_n_(707110, "Sprite", lambda: Sprite)):
    _l_(707111)

    """A class to represent a single alien in the fleet."""

def __init__(self, ai_settings, screen):
    _l_(707155)

    """Intialize the alien and set its starting position."""
    _c_(707116, _a_(707115, _n_(707112, "super", lambda: super)(_n_(707113, "Alien", lambda: Alien), _n_(707114, "self", lambda: self)), "__init__"))
    _l_(707117)
    _n_(707118, "self", lambda: self).screen = _n_(707119, "screen", lambda: screen)
    _l_(707120)
    _n_(707121, "self", lambda: self).ai_settings = _n_(707122, "ai_settings", lambda: ai_settings)
    _l_(707123)
    
    # Load the alien image and set its rect attribute.
    _n_(707124, "self", lambda: self).image = _c_(707128, _a_(707127, _a_(707126, _n_(707125, "pygame", lambda: pygame), "image"), "load"), 'images/alien.bmp')
    _l_(707129)
    _n_(707130, "self", lambda: self).rect = _c_(707134, _a_(707133, _a_(707132, _n_(707131, "self", lambda: self), "image"), "get_rect"))
    _l_(707135)
    
    # Start each new alien near the top left of the screen.
    _a_(707137, _n_(707136, "self", lambda: self), "rect").x = _a_(707140, _a_(707139, _n_(707138, "self", lambda: self), "rect"), "width")
    _l_(707141)
    _a_(707143, _n_(707142, "self", lambda: self), "rect").y = _a_(707146, _a_(707145, _n_(707144, "self", lambda: self), "rect"), "height")
    _l_(707147)
    
    # Store the alien's exact position.
    _n_(707148, "self", lambda: self).x = _c_(707153, _n_(707149, "float", lambda: float), _a_(707152, _a_(707151, _n_(707150, "self", lambda: self), "rect"), "x"))
    _l_(707154)
def blitme(self):
    _l_(707165)

    """Draw the alien at its current position."""
    _c_(707163, _a_(707158, _a_(707157, _n_(707156, "self", lambda: self), "screen"), "blit"), _a_(707160, _n_(707159, "self", lambda: self), "image"), _a_(707162, _n_(707161, "self", lambda: self), "rect"))
    _l_(707164)
def check_edges(self):
    _l_(707183)

    """Return True if alien is at edge of screen."""
    screen_rect = _c_(707169, _a_(707168, _a_(707167, _n_(707166, "self", lambda: self), "screen"), "get_rect"))
    _l_(707170)
    if _a_(707173, _a_(707172, _n_(707171, "self", lambda: self), "rect"), "right") >= _a_(707175, _n_(707174, "screen_rect", lambda: screen_rect), "right"):
        _l_(707182)

        aux = True
        _l_(707176)
        return aux
    elif _a_(707179, _a_(707178, _n_(707177, "self", lambda: self), "rect"), "left") <= 0:
        _l_(707181)

        aux = True
        _l_(707180)
        return aux
def update(self):
    _l_(707197)

    """Move the alien right or left."""
    _n_(707184, "self", lambda: self).x += (_a_(707187, _a_(707186, _n_(707185, "self", lambda: self), "ai_settings"), "alien_speed_factor") * 
                    _a_(707190, _a_(707189, _n_(707188, "self", lambda: self), "ai_settings"), "fleet_direction"))
    _l_(707191)
    _a_(707193, _n_(707192, "self", lambda: self), "rect").x = _a_(707195, _n_(707194, "self", lambda: self), "x")
    _l_(707196)