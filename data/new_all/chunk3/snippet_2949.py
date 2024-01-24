# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57298549/how-do-i-debug-this-attributeerror-int-object-has-no-attribute-increase
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Employee:
    _l_(523872)

    """Sort of simulates an employee."""

    def __init__(self, first, last, salary):
        _l_(523861)

        """Initialize attributes."""
        _n_(523852, "self", lambda: self).first = _n_(523853, "first", lambda: first)
        _l_(523854)
        _n_(523855, "self", lambda: self).last = _n_(523856, "last", lambda: last)
        _l_(523857)
        _n_(523858, "self", lambda: self).salary = _n_(523859, "salary", lambda: salary)
        _l_(523860)

    def give_raise(self, increase = 5000):
        _l_(523871)

        """gives raise"""
        _n_(523862, "self", lambda: self).increase = _n_(523863, "increase", lambda: increase)
        _l_(523864)
        _n_(523865, "self", lambda: self).salary = _a_(523867, _n_(523866, "self", lambda: self), "salary") + _a_(523869, _n_(523868, "self", lambda: self), "increase")
        _l_(523870)

_c_(523874, _n_(523873, "Employee", lambda: Employee), "first", "last", 30000)
_l_(523875)
_c_(523878, _a_(523877, _n_(523876, "Employee", lambda: Employee), "give_raise"), 890)
_l_(523879)
_c_(523883, _n_(523880, "print", lambda: print), _a_(523882, _n_(523881, "Employee", lambda: Employee), "salary"))
_l_(523884)