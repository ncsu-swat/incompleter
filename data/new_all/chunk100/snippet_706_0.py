# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Rectangle:
    _l_(72195)


    def __init__(self, l, w):
        _l_(72188)

        _n_(72182, "self", lambda: self).length = _n_(72183, "l", lambda: l)
        _l_(72184)
        _n_(72185, "self", lambda: self).width = _n_(72186, "w", lambda: w)
        _l_(72187)

    def rectangle_area(self):
        _l_(72194)

        aux = _a_(72190, _n_(72189, "self", lambda: self), "length") * _a_(72192, _n_(72191, "self", lambda: self), "width")
        _l_(72193)
        return aux
_c_(72200, _n_(72196, "print", lambda: print), _c_(72199, _a_(72198, _n_(72197, "newRectangle", lambda: newRectangle), "rectangle_area")))
_l_(72201)