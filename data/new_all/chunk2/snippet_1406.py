# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64795214/why-am-i-getting-nameerror-wolf-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pygame
    _l_(432993)

except ImportError:
    pass
try:
    import random
    _l_(432995)

except ImportError:
    pass
try:
    import Colors
    _l_(432997)

except ImportError:
    pass

class Player(_a_(433000, _a_(432999, _n_(432998, "pygame", lambda: pygame), "sprite"), "Sprite")):
    _l_(433052)

    """ The class is the player-controlled sprite. """
 
    # -- Methods
    def __init__(self, x, y):
        _l_(433035)

        """Constructor function"""
        # Call the parent's constructor
        _c_(433003, _a_(433002, _n_(433001, "super", lambda: super)(), "__init__"))
        _l_(433004)
 
        # Set height, width
        _n_(433005, "self", lambda: self).image = _c_(433008, _a_(433007, _n_(433006, "pygame", lambda: pygame), "Surface"), [15, 15])
        _l_(433009)
        _c_(433015, _a_(433012, _a_(433011, _n_(433010, "self", lambda: self), "image"), "fill"), _a_(433014, _n_(433013, "Colors", lambda: Colors), "BLUE"))
        _l_(433016)
 
        # Make our top-left corner the passed-in location.
        _n_(433017, "self", lambda: self).rect = _c_(433021, _a_(433020, _a_(433019, _n_(433018, "self", lambda: self), "image"), "get_rect"))
        _l_(433022)
        _a_(433024, _n_(433023, "self", lambda: self), "rect").x = _n_(433025, "x", lambda: x)
        _l_(433026)
        _a_(433028, _n_(433027, "self", lambda: self), "rect").y = _n_(433029, "y", lambda: y)
        _l_(433030)
 
        # -- Attributes
        # Set speed vector
        _n_(433031, "self", lambda: self).change_x = 0
        _l_(433032)
        _n_(433033, "self", lambda: self).change_y = 0
        _l_(433034)
 
    def changespeed(self, x, y):
        _l_(433042)

        """ Change the speed of the player"""
        _n_(433036, "self", lambda: self).change_x += _n_(433037, "x", lambda: x)
        _l_(433038)
        _n_(433039, "self", lambda: self).change_y += _n_(433040, "y", lambda: y)
        _l_(433041)
 
    def update(self):
        _l_(433051)

        """ Find a new position for the player"""
        _a_(433044, _n_(433043, "self", lambda: self), "rect").x += _n_(433045, "self", lambda: self).change_x
        _l_(433046)
        _a_(433048, _n_(433047, "self", lambda: self), "rect").y += _n_(433049, "self", lambda: self).change_y
        _l_(433050)