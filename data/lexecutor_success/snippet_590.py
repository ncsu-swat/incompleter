# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/390250/elegant-ways-to-support-equivalence-equality-in-python-classes
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Foo:
    _l_(1539302)

    def __eq__(self, other):
        _l_(1539301)

        if _c_(1539293, _n_(1539289, "isinstance", lambda: isinstance), _n_(1539290, "other", lambda: other), _a_(1539292, _n_(1539291, "self", lambda: self), "__class__")):
            _l_(1539300)

            aux = _a_(1539295, _n_(1539294, "self", lambda: self), "__dict__") == _a_(1539297, _n_(1539296, "other", lambda: other), "__dict__")
            _l_(1539298)
            return aux
        else:
            aux = False
            _l_(1539299)
            return aux

class Bar(_n_(1539303, "Foo", lambda: Foo)):
    _l_(1539304)

pass
b = _c_(1539306, _n_(1539305, "Bar", lambda: Bar))
_l_(1539307)
f = _c_(1539309, _n_(1539308, "Foo", lambda: Foo))
_l_(1539310)
_n_(1539311, "f", lambda: f) == _n_(1539312, "b", lambda: b)
_l_(1539313)
True
_l_(1539314)
_n_(1539315, "b", lambda: b) == _n_(1539316, "f", lambda: f)
_l_(1539317)
False
_l_(1539318)

def __eq__(self, other):
    _l_(1539332)

    if _c_(1539321, _n_(1539319, "type", lambda: type), _n_(1539320, "other", lambda: other)) is _c_(1539324, _n_(1539322, "type", lambda: type), _n_(1539323, "self", lambda: self)):
        _l_(1539330)

        aux = _a_(1539326, _n_(1539325, "self", lambda: self), "__dict__") == _a_(1539328, _n_(1539327, "other", lambda: other), "__dict__")
        _l_(1539329)
        return aux
    aux = False
    _l_(1539331)
    return aux

