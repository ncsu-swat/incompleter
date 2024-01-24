# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70735803/why-am-i-getting-an-attributeerror-alien-object-has-no-attribute-draw-bullet
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pygame
    _l_(467788)

except ImportError:
    pass
try:
    from pygame.sprite import Sprite
    _l_(467790)

except ImportError:
    pass

class Alien(_n_(467791, "Sprite", lambda: Sprite)):
    _l_(467878)

    """A class to represent a single alien in the fleet."""
    
    def __init__(self, ai_settings, screen):
        _l_(467835)

        """Initialize the alien and its starting position."""
        _c_(467796, _a_(467795, _n_(467792, "super", lambda: super)(_n_(467793, "Alien", lambda: Alien), _n_(467794, "self", lambda: self)), "__init__"))
        _l_(467797)
        _n_(467798, "self", lambda: self).screen = _n_(467799, "screen", lambda: screen)
        _l_(467800)
        _n_(467801, "self", lambda: self).ai_settings = _n_(467802, "ai_settings", lambda: ai_settings)
        _l_(467803)
        
        # Load the alien image and set its rect attribute.
        _n_(467804, "self", lambda: self).image = _c_(467808, _a_(467807, _a_(467806, _n_(467805, "pygame", lambda: pygame), "image"), "load"), 'images/alien.bmp')
        _l_(467809)
        _n_(467810, "self", lambda: self).rect = _c_(467814, _a_(467813, _a_(467812, _n_(467811, "self", lambda: self), "image"), "get_rect"))
        _l_(467815)
        
        # Start each new alien near the top left of the screen.
        _a_(467817, _n_(467816, "self", lambda: self), "rect").x = _a_(467820, _a_(467819, _n_(467818, "self", lambda: self), "rect"), "width")
        _l_(467821)
        _a_(467823, _n_(467822, "self", lambda: self), "rect").y = _a_(467826, _a_(467825, _n_(467824, "self", lambda: self), "rect"), "height")
        _l_(467827)
        
        # Store the alien's exact position.
        _n_(467828, "self", lambda: self).x = _c_(467833, _n_(467829, "float", lambda: float), _a_(467832, _a_(467831, _n_(467830, "self", lambda: self), "rect"), "x"))
        _l_(467834)
    def blitme(self):
        _l_(467845)

        """Draw the alien at its current location."""
        _c_(467843, _a_(467838, _a_(467837, _n_(467836, "self", lambda: self), "screen"), "blit"), _a_(467840, _n_(467839, "self", lambda: self), "image"), _a_(467842, _n_(467841, "self", lambda: self), "rect"))
        _l_(467844)
    
    def check_edges(self):
        _l_(467863)

        """Return true if alien is at edge of screen."""
        screen_rect = _c_(467849, _a_(467848, _a_(467847, _n_(467846, "self", lambda: self), "screen"), "get_rect"))
        _l_(467850)
        if _a_(467853, _a_(467852, _n_(467851, "self", lambda: self), "rect"), "right") >= _a_(467855, _n_(467854, "screen_rect", lambda: screen_rect), "right"):
            _l_(467862)

            aux = True
            _l_(467856)
            return aux
        elif _a_(467859, _a_(467858, _n_(467857, "self", lambda: self), "rect"), "left") <= 0:
            _l_(467861)

            aux = True
            _l_(467860)
            return aux
    def update(self):
        _l_(467877)

        """Move the alien right of left."""
        _n_(467864, "self", lambda: self).x += (_a_(467867, _a_(467866, _n_(467865, "self", lambda: self), "ai_settings"), "alien_speed_factor") * _a_(467870, _a_(467869, _n_(467868, "self", lambda: self), "ai_settings"), "fleet_direction"))
        _l_(467871)
        _a_(467873, _n_(467872, "self", lambda: self), "rect").x = _a_(467875, _n_(467874, "self", lambda: self), "x")
        _l_(467876)