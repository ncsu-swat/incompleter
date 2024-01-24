# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/26673926/attributeerror-object-has-no-attribute-velx
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pygame
    _l_(347944)

except ImportError:
    pass

class BaseClass(_a_(347947, _a_(347946, _n_(347945, "pygame", lambda: pygame), "sprite"), "Sprite")):
    _l_(347994)


    allsprites = _c_(347951, _a_(347950, _a_(347949, _n_(347948, "pygame", lambda: pygame), "sprite"), "Group"))
    _l_(347952)
    def __init__(self, x, y, width, height, image_string):
        _l_(347993)


        _c_(347958, _a_(347956, _a_(347955, _a_(347954, _n_(347953, "pygame", lambda: pygame), "sprite"), "Sprite"), "__init__"), _n_(347957, "self", lambda: self))
        _l_(347959)
        _c_(347964, _a_(347962, _a_(347961, _n_(347960, "BaseClass", lambda: BaseClass), "allsprites"), "add"), _n_(347963, "self", lambda: self))
        _l_(347965)

        _n_(347966, "self", lambda: self).image = _c_(347971, _a_(347969, _a_(347968, _n_(347967, "pygame", lambda: pygame), "image"), "load"), _n_(347970, "image_string", lambda: image_string))
        _l_(347972)
        _n_(347973, "self", lambda: self).rect = _c_(347977, _a_(347976, _a_(347975, _n_(347974, "self", lambda: self), "image"), "get_rect"))
        _l_(347978)
        _a_(347980, _n_(347979, "self", lambda: self), "rect").x = _n_(347981, "x", lambda: x)
        _l_(347982)
        _a_(347984, _n_(347983, "self", lambda: self), "rect").y = _n_(347985, "y", lambda: y)
        _l_(347986)

        _n_(347987, "self", lambda: self).width = _n_(347988, "width", lambda: width)
        _l_(347989)
        _n_(347990, "self", lambda: self).height = _n_(347991, "height", lambda: height)
        _l_(347992)



class Pokemon(_n_(347995, "BaseClass", lambda: BaseClass)):
    _l_(348025)

    List = _c_(347999, _a_(347998, _a_(347997, _n_(347996, "pygame", lambda: pygame), "sprite"), "Group"))
    _l_(348000)
    def __init___(self, x, y, width, height, image_string):
        _l_(348019)


        _c_(348009, _a_(348002, _n_(348001, "BaseClass", lambda: BaseClass), "__init__"), _n_(348003, "self", lambda: self), _n_(348004, "x", lambda: x), _n_(348005, "y", lambda: y), _n_(348006, "width", lambda: width), _n_(348007, "height", lambda: height), _n_(348008, "image_string", lambda: image_string))
        _l_(348010)
        _c_(348015, _a_(348013, _a_(348012, _n_(348011, "Pokemon", lambda: Pokemon), "List"), "add"), _n_(348014, "self", lambda: self))
        _l_(348016)
        _n_(348017, "self", lambda: self).velx = 3
        _l_(348018)

    def motion(self):
        _l_(348024)


        _a_(348021, _n_(348020, "self", lambda: self), "rect").x += _n_(348022, "self", lambda: self).velx
        _l_(348023)