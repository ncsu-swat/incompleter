# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61272588/typeerror-init-missing-2-required-positional-arguments-x-and-y-in-li
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class base:
    _l_(361631)

    def __init__(self,width,length,x,y):
        _l_(361610)

        _n_(361598, "self", lambda: self).__width=_n_(361599, "width", lambda: width)
        _l_(361600)
        _n_(361601, "self", lambda: self).__length=_n_(361602, "length", lambda: length)
        _l_(361603)
        _n_(361604, "self", lambda: self).__x=_n_(361605, "x", lambda: x)
        _l_(361606)
        _n_(361607, "self", lambda: self).__y=_n_(361608, "y", lambda: y)
        _l_(361609)

    def area(self):
        _l_(361616)

        aux = _a_(361612, _n_(361611, "self", lambda: self), "__width")*_a_(361614, _n_(361613, "self", lambda: self), "__length")
        _l_(361615)
        return aux

    def perimeter(self):
        _l_(361622)

        aux = 2*(_a_(361618, _n_(361617, "self", lambda: self), "__width")+_a_(361620, _n_(361619, "self", lambda: self), "__length"))
        _l_(361621)
        return aux

    def x(self):
        _l_(361626)

        aux = _a_(361624, _n_(361623, "self", lambda: self), "__x")
        _l_(361625)
        return aux

    def y(self):
        _l_(361630)

        aux = _a_(361628, _n_(361627, "self", lambda: self), "__y")
        _l_(361629)
        return aux

class circle(_n_(361632, "base", lambda: base)):
    _l_(361659)

    def __init__(self,radius,x,y):
        _l_(361644)

        _c_(361639, _a_(361636, _n_(361633, "super", lambda: super)(_n_(361634, "circle", lambda: circle),_n_(361635, "self", lambda: self)), "__init__"), _n_(361637, "x", lambda: x),_n_(361638, "y", lambda: y))
        _l_(361640)
        _n_(361641, "self", lambda: self).radius=_n_(361642, "radius", lambda: radius)
        _l_(361643)

    def area(self):
        _l_(361652)

        aux = _a_(361646, _n_(361645, "math", lambda: math), "pi")*_c_(361650, _n_(361647, "pow", lambda: pow), _a_(361649, _n_(361648, "self", lambda: self), "radius"),2)
        _l_(361651)
        return aux

    def perimeter(self):
        _l_(361658)

        aux = 2*_a_(361654, _n_(361653, "math", lambda: math), "pi")*_a_(361656, _n_(361655, "self", lambda: self), "radius")
        _l_(361657)
        return aux

class rectangle(_n_(361660, "base", lambda: base)):
    _l_(361672)

    def __init__(self,width,length,x,y):
        _l_(361671)

        _c_(361669, _a_(361664, _n_(361661, "super", lambda: super)(_n_(361662, "rectangle", lambda: rectangle),_n_(361663, "self", lambda: self)), "__init__"), _n_(361665, "width", lambda: width),_n_(361666, "length", lambda: length),_n_(361667, "x", lambda: x),_n_(361668, "y", lambda: y))
        _l_(361670)

# Test function: 

cir=_c_(361674, _n_(361673, "circle", lambda: circle), 3,1,2)
_l_(361675)
_c_(361678, _a_(361677, _n_(361676, "cir", lambda: cir), "area"))
_l_(361679)