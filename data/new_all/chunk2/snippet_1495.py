# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50835149/attributeerror-employee-object-has-no-attribute-workinghours
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Employee:
    _l_(426206)

    def numberofWorkingHours(self):
        _l_(426199)

        _n_(426197, "self", lambda: self).WorkingHours = 45
        _l_(426198)

    def printnumberofWorkingHours(self):
        _l_(426205)

        _c_(426203, _n_(426200, "print", lambda: print), _a_(426202, _n_(426201, "self", lambda: self), "WorkingHours"))
        _l_(426204)

class Trainee:
    _l_(426210)

    def numberofWorkingHours(self):
        _l_(426209)

        _n_(426207, "self", lambda: self).WorkingHours = 60
        _l_(426208)

emp = _c_(426212, _n_(426211, "Employee", lambda: Employee))
_l_(426213)
_c_(426216, _a_(426215, _n_(426214, "emp", lambda: emp), "printnumberofWorkingHours"))
_l_(426217)