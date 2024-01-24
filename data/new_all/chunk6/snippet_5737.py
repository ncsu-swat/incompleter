# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59699242/why-does-this-produce-the-error-message-attributeerror-a-object-has-no-attrib
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class A:
    _l_(370691)

    def __init__(self, x, y):
        _l_(370675)

        _n_(370669, "self", lambda: self).x = _n_(370670, "x", lambda: x)
        _l_(370671)
        _n_(370672, "self", lambda: self).y = _n_(370673, "y", lambda: y)
        _l_(370674)

    def method(self):
        _l_(370683)

        aux = _c_(370681, _n_(370676, "A", lambda: A), _a_(370678, _n_(370677, "self", lambda: self), "x") + 1, _a_(370680, _n_(370679, "self", lambda: self), "y") + 1)
        _l_(370682)
        return aux

    def method2(self, f):
        _l_(370690)

        if _a_(370687, _c_(370686, _a_(370685, _n_(370684, "self", lambda: self), "f")), "x") > 3:
            _l_(370689)

            aux = True
            _l_(370688)
            return aux

a = _c_(370693, _n_(370692, "A", lambda: A), 1, 2)
_l_(370694)
y = _c_(370700, _a_(370696, _n_(370695, "a", lambda: a), "method2"), _c_(370699, _a_(370698, _n_(370697, "a", lambda: a), "method")))
_l_(370701)
_c_(370704, _n_(370702, "print", lambda: print), _n_(370703, "y", lambda: y))
_l_(370705)