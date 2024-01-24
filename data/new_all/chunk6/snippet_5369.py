# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61272588/typeerror-init-missing-2-required-positional-arguments-x-and-y-in-li
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class base:
    _l_(342660)

    def __init__(self,width,length,x,y):
        _l_(342639)

        _n_(342627, "self", lambda: self).__width=_n_(342628, "width", lambda: width)
        _l_(342629)
        _n_(342630, "self", lambda: self).__length=_n_(342631, "length", lambda: length)
        _l_(342632)
        _n_(342633, "self", lambda: self).__x=_n_(342634, "x", lambda: x)
        _l_(342635)
        _n_(342636, "self", lambda: self).__y=_n_(342637, "y", lambda: y)
        _l_(342638)

    def area(self):
        _l_(342645)

        aux = _a_(342641, _n_(342640, "self", lambda: self), "__width")*_a_(342643, _n_(342642, "self", lambda: self), "__length")
        _l_(342644)
        return aux

    def perimeter(self):
        _l_(342651)

        aux = 2*(_a_(342647, _n_(342646, "self", lambda: self), "__width")+_a_(342649, _n_(342648, "self", lambda: self), "__length"))
        _l_(342650)
        return aux

    def x(self):
        _l_(342655)

        aux = _a_(342653, _n_(342652, "self", lambda: self), "__x")
        _l_(342654)
        return aux

    def y(self):
        _l_(342659)

        aux = _a_(342657, _n_(342656, "self", lambda: self), "__y")
        _l_(342658)
        return aux

class circle(_n_(342661, "base", lambda: base)):
    _l_(342688)

    def __init__(self,radius,x,y):
        _l_(342673)

        _c_(342668, _a_(342665, _n_(342662, "super", lambda: super)(_n_(342663, "circle", lambda: circle),_n_(342664, "self", lambda: self)), "__init__"), _n_(342666, "x", lambda: x),_n_(342667, "y", lambda: y))
        _l_(342669)
        _n_(342670, "self", lambda: self).radius=_n_(342671, "radius", lambda: radius)
        _l_(342672)

    def area(self):
        _l_(342681)

        aux = _a_(342675, _n_(342674, "math", lambda: math), "pi")*_c_(342679, _n_(342676, "pow", lambda: pow), _a_(342678, _n_(342677, "self", lambda: self), "radius"),2)
        _l_(342680)
        return aux

    def perimeter(self):
        _l_(342687)

        aux = 2*_a_(342683, _n_(342682, "math", lambda: math), "pi")*_a_(342685, _n_(342684, "self", lambda: self), "radius")
        _l_(342686)
        return aux

class rectangle(_n_(342689, "base", lambda: base)):
    _l_(342701)

    def __init__(self,width,length,x,y):
        _l_(342700)

        _c_(342698, _a_(342693, _n_(342690, "super", lambda: super)(_n_(342691, "rectangle", lambda: rectangle),_n_(342692, "self", lambda: self)), "__init__"), _n_(342694, "width", lambda: width),_n_(342695, "length", lambda: length),_n_(342696, "x", lambda: x),_n_(342697, "y", lambda: y))
        _l_(342699)

# Test function: 

cir=_c_(342703, _n_(342702, "circle", lambda: circle), 3,1,2)
_l_(342704)
_c_(342707, _a_(342706, _n_(342705, "cir", lambda: cir), "area"))
_l_(342708)