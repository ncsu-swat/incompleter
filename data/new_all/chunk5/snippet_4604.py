# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54445088/nameerror-class-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Position:
    _l_(660212)


    def __init__(self, x: _n_(660189, "int", lambda: int), y: _n_(660190, "int", lambda: int)):
        _l_(660197)

        _n_(660191, "self", lambda: self).x = _n_(660192, "x", lambda: x)
        _l_(660193)
        _n_(660194, "self", lambda: self).y = _n_(660195, "y", lambda: y)
        _l_(660196)

    def __add__(self, other: _n_(660198, "Position", lambda: Position)) -> _n_(660199, "Position", lambda: Position):
        _l_(660211)

        aux = _c_(660209, _n_(660200, "Position", lambda: Position), _a_(660202, _n_(660201, "self", lambda: self), "x") + _a_(660204, _n_(660203, "other", lambda: other), "x"), _a_(660206, _n_(660205, "self", lambda: self), "y") + _a_(660208, _n_(660207, "other", lambda: other), "y"))
        _l_(660210)
        return aux