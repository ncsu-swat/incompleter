# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61272588/typeerror-init-missing-2-required-positional-arguments-x-and-y-in-li
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class base:
    _l_(353838)

    def __init__(self,width,length,x,y):
        _l_(353817)

        _n_(353805, "self", lambda: self).__width=_n_(353806, "width", lambda: width)
        _l_(353807)
        _n_(353808, "self", lambda: self).__length=_n_(353809, "length", lambda: length)
        _l_(353810)
        _n_(353811, "self", lambda: self).__x=_n_(353812, "x", lambda: x)
        _l_(353813)
        _n_(353814, "self", lambda: self).__y=_n_(353815, "y", lambda: y)
        _l_(353816)

    def area(self):
        _l_(353823)

        aux = _a_(353819, _n_(353818, "self", lambda: self), "__width")*_a_(353821, _n_(353820, "self", lambda: self), "__length")
        _l_(353822)
        return aux

    def perimeter(self):
        _l_(353829)

        aux = 2*(_a_(353825, _n_(353824, "self", lambda: self), "__width")+_a_(353827, _n_(353826, "self", lambda: self), "__length"))
        _l_(353828)
        return aux

    def x(self):
        _l_(353833)

        aux = _a_(353831, _n_(353830, "self", lambda: self), "__x")
        _l_(353832)
        return aux

    def y(self):
        _l_(353837)

        aux = _a_(353835, _n_(353834, "self", lambda: self), "__y")
        _l_(353836)
        return aux

class circle(_n_(353839, "base", lambda: base)):
    _l_(353866)

    def __init__(self,radius,x,y):
        _l_(353851)

        _c_(353846, _a_(353843, _n_(353840, "super", lambda: super)(_n_(353841, "circle", lambda: circle),_n_(353842, "self", lambda: self)), "__init__"), _n_(353844, "x", lambda: x),_n_(353845, "y", lambda: y))
        _l_(353847)
        _n_(353848, "self", lambda: self).radius=_n_(353849, "radius", lambda: radius)
        _l_(353850)

    def area(self):
        _l_(353859)

        aux = _a_(353853, _n_(353852, "math", lambda: math), "pi")*_c_(353857, _n_(353854, "pow", lambda: pow), _a_(353856, _n_(353855, "self", lambda: self), "radius"),2)
        _l_(353858)
        return aux

    def perimeter(self):
        _l_(353865)

        aux = 2*_a_(353861, _n_(353860, "math", lambda: math), "pi")*_a_(353863, _n_(353862, "self", lambda: self), "radius")
        _l_(353864)
        return aux

class rectangle(_n_(353867, "base", lambda: base)):
    _l_(353879)

    def __init__(self,width,length,x,y):
        _l_(353878)

        _c_(353876, _a_(353871, _n_(353868, "super", lambda: super)(_n_(353869, "rectangle", lambda: rectangle),_n_(353870, "self", lambda: self)), "__init__"), _n_(353872, "width", lambda: width),_n_(353873, "length", lambda: length),_n_(353874, "x", lambda: x),_n_(353875, "y", lambda: y))
        _l_(353877)

# Test function: 

cir=_c_(353881, _n_(353880, "circle", lambda: circle), 3,1,2)
_l_(353882)
_c_(353885, _a_(353884, _n_(353883, "cir", lambda: cir), "area"))
_l_(353886)