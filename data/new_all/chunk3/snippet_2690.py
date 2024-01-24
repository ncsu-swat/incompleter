# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66610777/typeerror-module-object-is-not-callable-call-to-constructor
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from com.gs.entities import Employee
    _l_(566031)

except ImportError:
    pass
try:
    from _datetime import datetime, timedelta
    _l_(566033)

except ImportError:
    pass


class Branch:
    _l_(566119)


    def __init__(self, branchName):
        _l_(566106)

        _n_(566034, "self", lambda: self).branchName = _n_(566035, "branchName", lambda: branchName)
        _l_(566036)
        _n_(566037, "self", lambda: self).startTime = _c_(566040, _a_(566039, _n_(566038, "datetime", lambda: datetime), "now"))
        _l_(566041)
        _n_(566042, "self", lambda: self).endTime = _c_(566045, _a_(566044, _n_(566043, "datetime", lambda: datetime), "now")) + _c_(566047, _n_(566046, "timedelta", lambda: timedelta), hours = 9)
        _l_(566048)
        _n_(566049, "self", lambda: self).employees = []
        _l_(566050)
        for i in _c_(566052, _n_(566051, "range", lambda: range), 0, 10):
            _l_(566105)

            if(_n_(566053, "i", lambda: i) < 6):
                _l_(566104)

                _c_(566063, _a_(566056, _a_(566055, _n_(566054, "self", lambda: self), "employees"), "append"), _c_(566062, _n_(566057, "Employee", lambda: Employee), _n_(566058, "i", lambda: i), _c_(566061, _n_(566059, "str", lambda: str), _n_(566060, "i", lambda: i)), "Cashier"))
                _l_(566064)
            elif(_n_(566065, "i", lambda: i) < 8):
                _l_(566103)

                _c_(566075, _a_(566068, _a_(566067, _n_(566066, "self", lambda: self), "employees"), "append"), _c_(566074, _n_(566069, "Employee", lambda: Employee), _n_(566070, "i", lambda: i), _c_(566073, _n_(566071, "str", lambda: str), _n_(566072, "i", lambda: i)), "Loan Officers"))
                _l_(566076)
            elif(_n_(566077, "i", lambda: i) == 8):
                _l_(566102)

                _c_(566087, _a_(566080, _a_(566079, _n_(566078, "self", lambda: self), "employees"), "append"), _c_(566086, _n_(566081, "Employee", lambda: Employee), _n_(566082, "i", lambda: i), _c_(566085, _n_(566083, "str", lambda: str), _n_(566084, "i", lambda: i)), "Deputy Manager"))
                _l_(566088)
            elif(_n_(566089, "i", lambda: i) == 9):
                _l_(566101)

                _c_(566099, _a_(566092, _a_(566091, _n_(566090, "self", lambda: self), "employees"), "append"), _c_(566098, _n_(566093, "Employee", lambda: Employee), _n_(566094, "i", lambda: i), _c_(566097, _n_(566095, "str", lambda: str), _n_(566096, "i", lambda: i)), "Manager"))
                _l_(566100)
    def startOperation(self):
        _l_(566112)

        _c_(566110, _n_(566107, "print", lambda: print), "Starting operation at " + _a_(566109, _n_(566108, "self", lambda: self), "startTime"))
        _l_(566111)

    def endOperation(self):
        _l_(566118)

        _c_(566116, _n_(566113, "print", lambda: print), "Starting operation at " + _a_(566115, _n_(566114, "self", lambda: self), "endTime"))
        _l_(566117)


b = _c_(566121, _n_(566120, "Branch", lambda: Branch), "CP")
_l_(566122)
_c_(566126, _n_(566123, "print", lambda: print), _a_(566125, _n_(566124, "b", lambda: b), "employees"))
_l_(566127)