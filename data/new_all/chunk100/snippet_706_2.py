# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Rectangle:
    _l_(72232)


    def __init__(self, l, w):
        _l_(72225)

        _n_(72222, "self", lambda: self).length = _n_(72223, "l", lambda: l)
        _l_(72224)

    def rectangle_area(self):
        _l_(72231)

        aux = _a_(72227, _n_(72226, "self", lambda: self), "length") * _a_(72229, _n_(72228, "self", lambda: self), "width")
        _l_(72230)
        return aux
newRectangle = _c_(72234, _n_(72233, "Rectangle", lambda: Rectangle), 12, 10)
_l_(72235)
_c_(72240, _n_(72236, "print", lambda: print), _c_(72239, _a_(72238, _n_(72237, "newRectangle", lambda: newRectangle), "rectangle_area")))
_l_(72241)