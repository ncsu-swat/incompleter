# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/34500737/typeerror-object-takes-no-parameters-with-python2-metaclass-converted-to-py
#!/usr/bin/env python2
# test2.py

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Meta(_n_(418509, "type", lambda: type)):
    _l_(418521)

    def __new__(mcs, name, bases, clsdict):
        _l_(418520)

        new_class = _c_(418516, _a_(418511, _n_(418510, "type", lambda: type), "__new__"), _n_(418512, "mcs", lambda: mcs), _n_(418513, "name", lambda: name), _n_(418514, "bases", lambda: bases), _n_(418515, "clsdict", lambda: clsdict))
        _l_(418517)
        aux = _n_(418518, "new_class", lambda: new_class)
        _l_(418519)
        return aux

class Root(_n_(418522, "object", lambda: object)):
    _l_(418535)

    __metaclass__ = _n_(418523, "Meta", lambda: Meta)
    _l_(418524)

    def __init__(self, value=None):
        _l_(418534)

        _n_(418525, "self", lambda: self).value = _n_(418526, "value", lambda: value)
        _l_(418527)
        _c_(418532, _a_(418531, _n_(418528, "super", lambda: super)(_n_(418529, "Root", lambda: Root), _n_(418530, "self", lambda: self)), "__init__"))
        _l_(418533)

class Sub(_n_(418536, "Root", lambda: Root)):
    _l_(418554)

    def __init__(self, value=None):
        _l_(418544)

        _c_(418542, _a_(418540, _n_(418537, "super", lambda: super)(_n_(418538, "Sub", lambda: Sub), _n_(418539, "self", lambda: self)), "__init__"), value=_n_(418541, "value", lambda: value))
        _l_(418543)

    def __new__(cls, value=None):
        _l_(418553)

        _c_(418551, _a_(418548, _n_(418545, "super", lambda: super)(_n_(418546, "Sub", lambda: Sub), _n_(418547, "cls", lambda: cls)), "__new__"), _n_(418549, "cls", lambda: cls), _n_(418550, "value", lambda: value))
        _l_(418552)

if _n_(418555, "__name__", lambda: __name__) == '__main__':
    _l_(418559)

    sub = _c_(418557, _n_(418556, "Sub", lambda: Sub), 1)
    _l_(418558)