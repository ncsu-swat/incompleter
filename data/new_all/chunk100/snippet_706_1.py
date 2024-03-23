# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Rectangle:
    _l_(72212)


    def __init__(self, l, w):
        _l_(72205)

        _n_(72202, "self", lambda: self).width = _n_(72203, "w", lambda: w)
        _l_(72204)

    def rectangle_area(self):
        _l_(72211)

        aux = _a_(72207, _n_(72206, "self", lambda: self), "length") * _a_(72209, _n_(72208, "self", lambda: self), "width")
        _l_(72210)
        return aux
newRectangle = _c_(72214, _n_(72213, "Rectangle", lambda: Rectangle), 12, 10)
_l_(72215)
_c_(72220, _n_(72216, "print", lambda: print), _c_(72219, _a_(72218, _n_(72217, "newRectangle", lambda: newRectangle), "rectangle_area")))
_l_(72221)