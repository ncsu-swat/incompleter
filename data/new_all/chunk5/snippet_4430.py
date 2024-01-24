# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57908392/typeerror-init-takes-4-positional-arguments-but-5-were-given-added-all-e
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Employee:
    _l_(681809)

    def __init__(self,first,last,salary):
        _l_(681808)

        _n_(681793, "self", lambda: self).first=_n_(681794, "first", lambda: first)
        _l_(681795)
        _n_(681796, "self", lambda: self).last=_n_(681797, "last", lambda: last)
        _l_(681798)
        _n_(681799, "self", lambda: self).salary=_n_(681800, "salary", lambda: salary)
        _l_(681801)
        _n_(681802, "self", lambda: self).email=_c_(681806, _a_(681803, "{}{}@company.com", "format"), _n_(681804, "first", lambda: first),_n_(681805, "last", lambda: last))
        _l_(681807)


class administrator:
    _l_(681814)

    def __init__(self,age):
        _l_(681813)

        _n_(681810, "self", lambda: self).age=_n_(681811, "age", lambda: age)
        _l_(681812)

class Manager(_n_(681815, "Employee", lambda: Employee),_n_(681816, "administrator", lambda: administrator)):
    _l_(681829)

    def __init__(self,first,last,salary,age,gender):
        _l_(681828)


        _c_(681823, _a_(681818, _n_(681817, "super", lambda: super)(), "__init__"), _n_(681819, "first", lambda: first),_n_(681820, "last", lambda: last),_n_(681821, "salary", lambda: salary),_n_(681822, "age", lambda: age))
        _l_(681824)
        _n_(681825, "self", lambda: self).gender=_n_(681826, "gender", lambda: gender)
        _l_(681827)

manager1=_c_(681831, _n_(681830, "Manager", lambda: Manager), "Max","Milan",50000,26,"male")
_l_(681832)

_c_(681836, _n_(681833, "print", lambda: print), _a_(681835, _n_(681834, "manager1", lambda: manager1), "email"))
_l_(681837)
_c_(681841, _n_(681838, "print", lambda: print), _a_(681840, _n_(681839, "manager1", lambda: manager1), "gender"))
_l_(681842)