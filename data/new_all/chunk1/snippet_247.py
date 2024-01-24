# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/34500737/typeerror-object-takes-no-parameters-with-python2-metaclass-converted-to-py
#!/usr/bin/env python3
# test3.py

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Meta(_n_(410591, "type", lambda: type)):
    _l_(410603)

    def __new__(mcs, name, bases, clsdict):
        _l_(410602)

        new_class = _c_(410598, _a_(410593, _n_(410592, "type", lambda: type), "__new__"), _n_(410594, "mcs", lambda: mcs), _n_(410595, "name", lambda: name), _n_(410596, "bases", lambda: bases), _n_(410597, "clsdict", lambda: clsdict))
        _l_(410599)
        aux = _n_(410600, "new_class", lambda: new_class)
        _l_(410601)
        return aux

class Root(_n_(410604, "object", lambda: object), metaclass=_n_(410605, "Meta", lambda: Meta)):
    _l_(410616)

    def __init__(self, value=None):
        _l_(410615)

        _n_(410606, "self", lambda: self).value = _n_(410607, "value", lambda: value)
        _l_(410608)
        _c_(410613, _a_(410612, _n_(410609, "super", lambda: super)(_n_(410610, "Root", lambda: Root), _n_(410611, "self", lambda: self)), "__init__"))
        _l_(410614)

class Sub(_n_(410617, "Root", lambda: Root)):
    _l_(410635)

    def __init__(self, value=None):
        _l_(410625)

        _c_(410623, _a_(410621, _n_(410618, "super", lambda: super)(_n_(410619, "Sub", lambda: Sub), _n_(410620, "self", lambda: self)), "__init__"), value=_n_(410622, "value", lambda: value))
        _l_(410624)

    def __new__(cls, value=None):
        _l_(410634)

        _c_(410632, _a_(410629, _n_(410626, "super", lambda: super)(_n_(410627, "Sub", lambda: Sub), _n_(410628, "cls", lambda: cls)), "__new__"), _n_(410630, "cls", lambda: cls), _n_(410631, "value", lambda: value))
        _l_(410633)

if _n_(410636, "__name__", lambda: __name__) == '__main__':
    _l_(410640)

    sub = _c_(410638, _n_(410637, "Sub", lambda: Sub), 1)
    _l_(410639)