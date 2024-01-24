# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60473871/typeerror-init-got-multiple-values-for-argument-with-python-3-using-sup
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Parent:
    _l_(408067)

    def __init__(self, var1, var2):
        _l_(408066)

        _n_(408060, "self", lambda: self).var1 = _n_(408061, "var1", lambda: var1)
        _l_(408062)
        _n_(408063, "self", lambda: self).var2 = _n_(408064, "var2", lambda: var2)
        _l_(408065)

class Child(_n_(408068, "Parent", lambda: Parent)):
    _l_(408080)

    a = 1 #a and b are class attributes
    _l_(408069) #a and b are class attributes
    b = 2
    _l_(408070)

    def __init__(self, var1 = 1, var2 = 2, var3 = None):
        _l_(408079)

        _c_(408074, _a_(408072, _n_(408071, "super", lambda: super)(), "__init__"), _n_(408073, "self", lambda: self), var1 = 1, var2 = 2) #error shows up for this line
        _l_(408075) #error shows up for this line
        _n_(408076, "self", lambda: self).var3 = _n_(408077, "var3", lambda: var3)
        _l_(408078)

child_obj = _c_(408082, _n_(408081, "Child", lambda: Child), var3 = 3)
_l_(408083)