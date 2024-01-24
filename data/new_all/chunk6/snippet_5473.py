# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/26673926/attributeerror-object-has-no-attribute-velx
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pygame
    _l_(335052)

except ImportError:
    pass

class BaseClass(_a_(335055, _a_(335054, _n_(335053, "pygame", lambda: pygame), "sprite"), "Sprite")):
    _l_(335102)


    allsprites = _c_(335059, _a_(335058, _a_(335057, _n_(335056, "pygame", lambda: pygame), "sprite"), "Group"))
    _l_(335060)
    def __init__(self, x, y, width, height, image_string):
        _l_(335101)


        _c_(335066, _a_(335064, _a_(335063, _a_(335062, _n_(335061, "pygame", lambda: pygame), "sprite"), "Sprite"), "__init__"), _n_(335065, "self", lambda: self))
        _l_(335067)
        _c_(335072, _a_(335070, _a_(335069, _n_(335068, "BaseClass", lambda: BaseClass), "allsprites"), "add"), _n_(335071, "self", lambda: self))
        _l_(335073)

        _n_(335074, "self", lambda: self).image = _c_(335079, _a_(335077, _a_(335076, _n_(335075, "pygame", lambda: pygame), "image"), "load"), _n_(335078, "image_string", lambda: image_string))
        _l_(335080)
        _n_(335081, "self", lambda: self).rect = _c_(335085, _a_(335084, _a_(335083, _n_(335082, "self", lambda: self), "image"), "get_rect"))
        _l_(335086)
        _a_(335088, _n_(335087, "self", lambda: self), "rect").x = _n_(335089, "x", lambda: x)
        _l_(335090)
        _a_(335092, _n_(335091, "self", lambda: self), "rect").y = _n_(335093, "y", lambda: y)
        _l_(335094)

        _n_(335095, "self", lambda: self).width = _n_(335096, "width", lambda: width)
        _l_(335097)
        _n_(335098, "self", lambda: self).height = _n_(335099, "height", lambda: height)
        _l_(335100)



class Pokemon(_n_(335103, "BaseClass", lambda: BaseClass)):
    _l_(335133)

    List = _c_(335107, _a_(335106, _a_(335105, _n_(335104, "pygame", lambda: pygame), "sprite"), "Group"))
    _l_(335108)
    def __init___(self, x, y, width, height, image_string):
        _l_(335127)


        _c_(335117, _a_(335110, _n_(335109, "BaseClass", lambda: BaseClass), "__init__"), _n_(335111, "self", lambda: self), _n_(335112, "x", lambda: x), _n_(335113, "y", lambda: y), _n_(335114, "width", lambda: width), _n_(335115, "height", lambda: height), _n_(335116, "image_string", lambda: image_string))
        _l_(335118)
        _c_(335123, _a_(335121, _a_(335120, _n_(335119, "Pokemon", lambda: Pokemon), "List"), "add"), _n_(335122, "self", lambda: self))
        _l_(335124)
        _n_(335125, "self", lambda: self).velx = 3
        _l_(335126)

    def motion(self):
        _l_(335132)


        _a_(335129, _n_(335128, "self", lambda: self), "rect").x += _n_(335130, "self", lambda: self).velx
        _l_(335131)