# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64795214/why-am-i-getting-nameerror-wolf-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
        import pygame
        _l_(468964)

except ImportError:
        pass
try:
        import random
        _l_(468966)

except ImportError:
        pass
try:
        import Colors
        _l_(468968)

except ImportError:
        pass

    
class Wolf(_a_(468971, _a_(468970, _n_(468969, "pygame", lambda: pygame), "sprite"), "Sprite")):
        _l_(468996)

        def __init__(self, color, width, height):
                _l_(468995)

                _c_(468974, _a_(468973, _n_(468972, "super", lambda: super)(), "__init__"))
                _l_(468975)
                _n_(468976, "self", lambda: self).image = _c_(468981, _a_(468978, _n_(468977, "pygame", lambda: pygame), "Surface"), [_n_(468979, "width", lambda: width), _n_(468980, "height", lambda: height)])
                _l_(468982)
                _c_(468987, _a_(468985, _a_(468984, _n_(468983, "self", lambda: self), "image"), "fill"), _n_(468986, "color", lambda: color))
                _l_(468988)
                _n_(468989, "self", lambda: self).rect = _c_(468993, _a_(468992, _a_(468991, _n_(468990, "self", lambda: self), "image"), "get_rect"))
                _l_(468994)