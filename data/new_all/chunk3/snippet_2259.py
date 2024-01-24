# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55318044/patching-an-object-in-a-factory-class-yields-typeerror-super-argument-1-must
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from unittest.mock import patch
    _l_(548499)

except ImportError:
    pass

class B():
    _l_(548501)

    pass
    _l_(548500)

class A(_n_(548502, "B", lambda: B)):
    _l_(548504)

    pass
    _l_(548503)


class AFactory:
    _l_(548515)


    def create(self):
        _l_(548514)

        a = _c_(548506, _n_(548505, "A", lambda: A))
        _l_(548507)
        _c_(548512, _a_(548511, _n_(548508, "super", lambda: super)(_n_(548509, "A", lambda: A), _n_(548510, "a", lambda: a)), "__init__"))
        _l_(548513)

with _c_(548517, _n_(548516, "patch", lambda: patch), 'mymain.A'):
    _l_(548523)

    _c_(548521, _a_(548520, _c_(548519, _n_(548518, "AFactory", lambda: AFactory)), "create"))
    _l_(548522)