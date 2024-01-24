# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76940145/using-multiple-inheritance-getting-typeerror-init-missing-1-required-po
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Employee:
    _l_(417814)

    def __init__(self, id, ename):
        _l_(417805)

        _n_(417799, "self", lambda: self).id = _n_(417800, "id", lambda: id)
        _l_(417801)
        _n_(417802, "self", lambda: self).ename = _n_(417803, "ename", lambda: ename)
        _l_(417804)

    def showInfo(self):
        _l_(417813)

        _c_(417811, _n_(417806, "print", lambda: print), "ID=", _a_(417808, _n_(417807, "self", lambda: self), "id"), "Name of employee=", _a_(417810, _n_(417809, "self", lambda: self), "ename"))
        _l_(417812)

class Programmer(_n_(417815, "Employee", lambda: Employee)):
    _l_(417836)

    def __init__(self, id, ename, language):
        _l_(417825)

        _c_(417820, _a_(417817, _n_(417816, "super", lambda: super)(), "__init__"), _n_(417818, "id", lambda: id), _n_(417819, "ename", lambda: ename))
        _l_(417821)
        _n_(417822, "self", lambda: self).language = _n_(417823, "language", lambda: language)
        _l_(417824)

    def showInfo(self):
        _l_(417835)

        _c_(417828, _a_(417827, _n_(417826, "super", lambda: super)(), "showInfo"))
        _l_(417829)
        _c_(417833, _n_(417830, "print", lambda: print), "Development Language=", _a_(417832, _n_(417831, "self", lambda: self), "language"))
        _l_(417834)

class Manager(_n_(417837, "Employee", lambda: Employee)):
    _l_(417858)

    def __init__(self, id, ename, department):
        _l_(417847)

        _c_(417842, _a_(417839, _n_(417838, "super", lambda: super)(), "__init__"), _n_(417840, "id", lambda: id), _n_(417841, "ename", lambda: ename))
        _l_(417843)
        _n_(417844, "self", lambda: self).department = _n_(417845, "department", lambda: department)
        _l_(417846)

    def showInfo(self):
        _l_(417857)

        _c_(417850, _a_(417849, _n_(417848, "super", lambda: super)(), "showInfo"))
        _l_(417851)
        _c_(417855, _n_(417852, "print", lambda: print), "Department=", _a_(417854, _n_(417853, "self", lambda: self), "department"))
        _l_(417856)

# Define Development Manager class using Multiple inheritances
class DevManager(_n_(417859, "Programmer", lambda: Programmer), _n_(417860, "Manager", lambda: Manager)):
    _l_(417883)

    def __init__(self, id, ename, language, department):
        _l_(417877)

        _c_(417867, _a_(417862, _n_(417861, "Programmer", lambda: Programmer), "__init__"), _n_(417863, "self", lambda: self), _n_(417864, "id", lambda: id), _n_(417865, "ename", lambda: ename), _n_(417866, "language", lambda: language))
        _l_(417868)
        _c_(417875, _a_(417870, _n_(417869, "Manager", lambda: Manager), "__init__"), _n_(417871, "self", lambda: self), _n_(417872, "id", lambda: id), _n_(417873, "ename", lambda: ename), _n_(417874, "department", lambda: department))
        _l_(417876)

    def showInfo(self):
        _l_(417882)

        _c_(417880, _a_(417879, _n_(417878, "super", lambda: super)(), "showInfo"))
        _l_(417881)

# Main
obj = _c_(417885, _n_(417884, "DevManager", lambda: DevManager), "A101", "Rajib Menon", "Python", "Engineering")
_l_(417886)
_c_(417889, _a_(417888, _n_(417887, "obj", lambda: obj), "showInfo"))
_l_(417890)