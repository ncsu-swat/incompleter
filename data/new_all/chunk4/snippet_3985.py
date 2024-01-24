# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64683421/how-to-adjust-a-dict-of-one-class-so-it-works-in-another-when-using-type
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class A(_n_(591739, "object", lambda: object)):
    _l_(591746)

    def __init__(self):
        _l_(591745)

        _c_(591743, _n_(591740, "print", lambda: print), 'A', _a_(591742, _n_(591741, "self", lambda: self), "__dict__"))
        _l_(591744)


class B(_n_(591747, "object", lambda: object)):
    _l_(591754)

    def __init__(self):
        _l_(591753)

        _c_(591751, _n_(591748, "print", lambda: print), 'B', _a_(591750, _n_(591749, "self", lambda: self), "__dict__"))
        _l_(591752)

F = _c_(591761, _n_(591755, "type", lambda: type), 'C', (_n_(591756, "B", lambda: B),), _c_(591760, _a_(591759, _a_(591758, _n_(591757, "A", lambda: A), "__dict__"), "copy")))
_l_(591762)
_c_(591764, _n_(591763, "F", lambda: F))
_l_(591765)