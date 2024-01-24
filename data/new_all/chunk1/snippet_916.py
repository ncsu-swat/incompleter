# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/41606555/typeerror-object-takes-no-parameters
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Person(_n_(408169, "object", lambda: object)):
    _l_(408199)

    def __new__(cls, name, age):
        _l_(408182)

        _c_(408171, _n_(408170, "print", lambda: print), '__new__called')
        _l_(408172)
        aux = _c_(408180, _a_(408176, _n_(408173, "super", lambda: super)(_n_(408174, "Person", lambda: Person), _n_(408175, "cls", lambda: cls)), "__new__"), _n_(408177, "cls", lambda: cls), _n_(408178, "name", lambda: name), _n_(408179, "age", lambda: age))
        _l_(408181)
        return aux
    def __init__(self, name, age):
        _l_(408192)

        _c_(408184, _n_(408183, "print", lambda: print), '__init__called')
        _l_(408185)
        _n_(408186, "self", lambda: self).name = _n_(408187, "name", lambda: name)
        _l_(408188)
        _n_(408189, "self", lambda: self).age = _n_(408190, "age", lambda: age)
        _l_(408191)
    def __str__(self):
        _l_(408198)

        aux = ('<Person:%s(%s)>'%(_a_(408194, _n_(408193, "self", lambda: self), "name"), _a_(408196, _n_(408195, "self", lambda: self), "age")))
        _l_(408197)
        return aux
if _n_(408200, "__name__", lambda: __name__) == '__main__':
    _l_(408208)

    piglei = _c_(408202, _n_(408201, "Person", lambda: Person), "piglei", 24)
    _l_(408203)
    _c_(408206, _n_(408204, "print", lambda: print), _n_(408205, "piglei", lambda: piglei))
    _l_(408207)