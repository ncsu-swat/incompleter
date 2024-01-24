# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70590761/get-attribute-error-while-calling-a-attribute-of-specific-class-in-another-class
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Class1:
    _l_(422519)

    def __init__(self,a ,b) -> None:
        _l_(422518)

        _n_(422512, "self", lambda: self).a = _n_(422513, "a", lambda: a)
        _l_(422514)
        _n_(422515, "self", lambda: self).b = _n_(422516, "b", lambda: b)
        _l_(422517)


class Class2:
    _l_(422540)

    def __init__(self, myobject) -> None:
        _l_(422523)

        _n_(422520, "self", lambda: self).myobject = _n_(422521, "myobject", lambda: myobject)
        _l_(422522)

    def __eq__(self, other: _n_(422524, "object", lambda: object)) -> _n_(422525, "bool", lambda: bool):
        _l_(422532)

        aux = _a_(422528, _a_(422527, _n_(422526, "self", lambda: self), "myobject"), "a") == _a_(422530, _n_(422529, "other", lambda: other), "a")
        _l_(422531)
        return aux

    def __str__(self) -> _n_(422533, "str", lambda: str):
        _l_(422539)

        aux = _c_(422537, _n_(422534, "str", lambda: str), _a_(422536, _n_(422535, "self", lambda: self), "myobject"))
        _l_(422538)
        return aux

variable1=_c_(422544, _n_(422541, "Class2", lambda: Class2), _c_(422543, _n_(422542, "Class1", lambda: Class1), 1,2))
_l_(422545)
variable2=_c_(422549, _n_(422546, "Class2", lambda: Class2), _c_(422548, _n_(422547, "Class1", lambda: Class1), 1,3))
_l_(422550)

_c_(422554, _n_(422551, "print", lambda: print), _n_(422552, "variable1", lambda: variable1)==_n_(422553, "variable2", lambda: variable2))
_l_(422555)