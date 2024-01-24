# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58208539/get-methods-name-using-getattribute-without-type-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Person(_n_(428483, "object", lambda: object)):
    _l_(428496)

    def __init__(self):
        _l_(428486)

        _n_(428484, "super", lambda: super)()
        _l_(428485)

    def test(self):
        _l_(428490)

        _c_(428488, _n_(428487, "print", lambda: print), 1)
        _l_(428489)

    def __getattribute__(self, attr):
        _l_(428495)

        _c_(428493, _n_(428491, "print", lambda: print), _n_(428492, "attr", lambda: attr))
        _l_(428494)



p = _c_(428498, _n_(428497, "Person", lambda: Person))
_l_(428499)

_c_(428502, _a_(428501, _n_(428500, "p", lambda: p), "test"))
_l_(428503)