# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/37557411/why-does-defining-the-argument-types-for-eq-throw-a-mypy-type-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class MyObject(_n_(411040, "object", lambda: object)):
    _l_(411054)

    def __init__(self, value: _n_(411041, "int", lambda: int)=5) -> None:
        _l_(411045)

        _n_(411042, "self", lambda: self).value = _n_(411043, "value", lambda: value)
        _l_(411044)

    def __eq__(self, other: _n_(411046, "MyObject", lambda: MyObject)) -> _n_(411047, "bool", lambda: bool):
        _l_(411053)

        aux = _a_(411049, _n_(411048, "self", lambda: self), "value") == _a_(411051, _n_(411050, "other", lambda: other), "value")
        _l_(411052)
        return aux