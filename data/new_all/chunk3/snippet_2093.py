# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64738269/attributeerror-pygame-rect-object-has-no-attribute-up
#! python3

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pygame
    _l_(522864)

except ImportError:
    pass

class Ship():
    _l_(522987)

    """A class intended for the management of a spacecraft"""

    def __init__(self, ai_game):
        _l_(522919)

        """Spaceship initialization and its initial position."""

        _n_(522865, "self", lambda: self).screen = _a_(522867, _n_(522866, "ai_game", lambda: ai_game), "screen")
        _l_(522868)
        _n_(522869, "self", lambda: self).settings = _a_(522871, _n_(522870, "ai_game", lambda: ai_game), "settings")
        _l_(522872)
        _n_(522873, "self", lambda: self).screen_rect = _c_(522877, _a_(522876, _a_(522875, _n_(522874, "ai_game", lambda: ai_game), "screen"), "get_rect"))
        _l_(522878)

        #Load a spaceship image and retrieve its rectangle.
        _n_(522879, "self", lambda: self).image = _c_(522883, _a_(522882, _a_(522881, _n_(522880, "pygame", lambda: pygame), "image"), "load"), 'images/ship.bmp')
        _l_(522884)
        _n_(522885, "self", lambda: self).rect = _c_(522889, _a_(522888, _a_(522887, _n_(522886, "self", lambda: self), "image"), "get_rect"))
        _l_(522890)

        #Each new ship appears in the bottom center of the screen.
        _a_(522892, _n_(522891, "self", lambda: self), "rect").midbottom = _a_(522895, _a_(522894, _n_(522893, "self", lambda: self), "screen_rect"), "midbottom")
        _l_(522896)

        #The ship's horizontal position is stored as a floating point number.
        _n_(522897, "self", lambda: self).x = _c_(522902, _n_(522898, "float", lambda: float), _a_(522901, _a_(522900, _n_(522899, "self", lambda: self), "rect"), "x"))
        _l_(522903)
        _n_(522904, "self", lambda: self).y = _c_(522909, _n_(522905, "float", lambda: float), _a_(522908, _a_(522907, _n_(522906, "self", lambda: self), "rect"), "y"))
        _l_(522910)

        #Options that indicate the movement of the ship
        _n_(522911, "self", lambda: self).moving_right = False
        _l_(522912)
        _n_(522913, "self", lambda: self).moving_left = False
        _l_(522914)
        _n_(522915, "self", lambda: self).moving_up = False
        _l_(522916)
        _n_(522917, "self", lambda: self).moving_down = False
        _l_(522918)

    def update(self):
        _l_(522976)

        """Update the ship's position based on the option that indicates its movement."""

        #Updating the X coordinate of the ship, not its rectangle
        if _a_(522921, _n_(522920, "self", lambda: self), "moving_right") and _a_(522924, _a_(522923, _n_(522922, "self", lambda: self), "rect"), "right") < _a_(522927, _a_(522926, _n_(522925, "self", lambda: self), "screen_rect"), "right"):
            _l_(522932)

            _n_(522928, "self", lambda: self).x += _a_(522930, _n_(522929, "self", lambda: self), "settings").ship_speed
            _l_(522931)
        if _a_(522934, _n_(522933, "self", lambda: self), "moving_left") and _a_(522937, _a_(522936, _n_(522935, "self", lambda: self), "rect"), "left") > 0:
            _l_(522942)

            _n_(522938, "self", lambda: self).x -= _a_(522940, _n_(522939, "self", lambda: self), "settings").ship_speed
            _l_(522941)

       
        if _a_(522944, _n_(522943, "self", lambda: self), "moving_up") and _a_(522947, _a_(522946, _n_(522945, "self", lambda: self), "rect"), "up") > 0:
            _l_(522952)

            _n_(522948, "self", lambda: self).y += _a_(522950, _n_(522949, "self", lambda: self), "settings").ship_speed
            _l_(522951)
        if _a_(522954, _n_(522953, "self", lambda: self), "moving_down") and _a_(522957, _a_(522956, _n_(522955, "self", lambda: self), "rect"), "down") > _a_(522960, _a_(522959, _n_(522958, "self", lambda: self), "screen_rect"), "down"):
            _l_(522965)

            _n_(522961, "self", lambda: self).y -= _a_(522963, _n_(522962, "self", lambda: self), "settings").ship_speed
            _l_(522964)

        
        #Updating rect based on self.x
        _a_(522967, _n_(522966, "self", lambda: self), "rect").x = _a_(522969, _n_(522968, "self", lambda: self), "x")
        _l_(522970)
        _a_(522972, _n_(522971, "self", lambda: self), "rect").y = _a_(522974, _n_(522973, "self", lambda: self), "y")
        _l_(522975)

    def blitme(self):
        _l_(522986)

        """Displaying a spaceship in its current position."""
        _c_(522984, _a_(522979, _a_(522978, _n_(522977, "self", lambda: self), "screen"), "blit"), _a_(522981, _n_(522980, "self", lambda: self), "image"), _a_(522983, _n_(522982, "self", lambda: self), "rect"))
        _l_(522985)