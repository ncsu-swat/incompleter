# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57357818/how-can-i-fix-the-typeerror-of-my-dataclass-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from dataclasses import dataclass
    _l_(377617)

except ImportError:
    pass

@_n_(377618, "dataclass", lambda: dataclass)
class Employee(_n_(377619, "object", lambda: object)):
    _l_(377657)

    name: _n_(377620, "str", lambda: str)
    _l_(377621)
    lastname: _n_(377622, "str", lambda: str)
    _l_(377623)
    age: _n_(377624, "int", lambda: int) or None
    _l_(377625)
    salary: _n_(377626, "int", lambda: int)
    _l_(377627)
    department: _n_(377628, "str", lambda: str)
    _l_(377629)

    def __new__(cls, name, lastname, age, salary, department):
        _l_(377635)

        aux = _c_(377633, _a_(377631, _n_(377630, "object", lambda: object), "__new__"), _n_(377632, "cls", lambda: cls))
        _l_(377634)
        return aux

    def __post_init__(self):
        _l_(377648)

        if _c_(377639, _n_(377636, "type", lambda: type), _a_(377638, _n_(377637, "self", lambda: self), "age")) == _n_(377640, "str", lambda: str):
            _l_(377647)

            _n_(377641, "self", lambda: self).age = _c_(377645, _n_(377642, "int", lambda: int), _a_(377644, _n_(377643, "self", lambda: self), "age")) or None
            _l_(377646)

    def __str__(self):
        _l_(377656)

        aux = f'{_a_(377650, _n_(377649, "self", lambda: self), "name")}, {_a_(377652, _n_(377651, "self", lambda: self), "lastname")}, {_a_(377654, _n_(377653, "self", lambda: self), "age")}' 
        _l_(377655) 
        return aux 

dic = {"name":"abdülmutallip", 
"lastname":"uzunkavakağacıaltındauzanıroğlu", 
"age":"24", "salary":2000, "department":"İK", 
"city":"istanbul", "country":"tr", "adres":"yok", "phone":"0033333"}
_l_(377658)

a = _c_(377661, _n_(377659, 'Employee', lambda: Employee), **_n_(377660, 'dic', lambda: dic))
_l_(377662)
_c_(377665, _n_(377663, 'print', lambda: print), _n_(377664, 'a', lambda: a))
_l_(377666)