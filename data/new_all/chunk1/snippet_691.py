# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56850716/typeerror-when-extending-a-class-with-additional-attributes
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class inheritest(_n_(392094, "bytes", lambda: bytes)):
    _l_(392109)

    def __init__(self, bs: _n_(392095, "bytes", lambda: bytes), x: _n_(392096, "int", lambda: int) = 0):
        _l_(392108)

        _c_(392098, _n_(392097, "print", lambda: print), "child class init")
        _l_(392099)
        _n_(392100, "self", lambda: self).x = _n_(392101, "x", lambda: x)
        _l_(392102)
        _c_(392106, _a_(392104, _n_(392103, "super", lambda: super)(), "__init__"), _n_(392105, "bs", lambda: bs))
        _l_(392107)


_c_(392113, _n_(392110, "print", lambda: print), _c_(392112, _n_(392111, "inheritest", lambda: inheritest), b'foobar', 3))
_l_(392114)