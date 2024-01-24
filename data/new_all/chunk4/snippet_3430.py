# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74460778/how-do-i-fix-typeerror-must-be-a-real-number-not-a-tuple-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Vehicle:
    _l_(645674)

    name = ""
    _l_(645658)
    kind = "car"
    _l_(645659)
    color = ""
    _l_(645660)
    value = 100.00
    _l_(645661)
    def description(self):
        _l_(645673)

        desc_str = "%s is a %s %s worth $%.2f." % (_a_(645663, _n_(645662, "self", lambda: self), "name"), _a_(645665, _n_(645664, "self", lambda: self), "color"), _a_(645667, _n_(645666, "self", lambda: self), "kind"), _a_(645669, _n_(645668, "self", lambda: self), "value"))
        _l_(645670)
        aux = _n_(645671, "desc_str", lambda: desc_str)
        _l_(645672)
        return aux

car1 = _c_(645676, _n_(645675, "Vehicle", lambda: Vehicle))
_l_(645677)
_n_(645678, "car1", lambda: car1).name = "Fer"
_l_(645679)
_n_(645680, "car1", lambda: car1).color = "Red"
_l_(645681)
_n_(645682, "car1", lambda: car1).kind = "Convertible"
_l_(645683)
_n_(645684, "car1", lambda: car1).value = 60,000.00
_l_(645685)

car2 = _c_(645687, _n_(645686, "Vehicle", lambda: Vehicle))
_l_(645688)
_n_(645689, "car2", lambda: car2).name = "Jump"
_l_(645690)
_n_(645691, "car2", lambda: car2).color = "Blue"
_l_(645692)
_n_(645693, "car2", lambda: car2).kind = "Van"
_l_(645694)
_n_(645695, "car2", lambda: car2).value = 10,000.00
_l_(645696)

_c_(645701, _n_(645697, "print", lambda: print), _c_(645700, _a_(645699, _n_(645698, "car1", lambda: car1), "description")))
_l_(645702)
_c_(645707, _n_(645703, "print", lambda: print), _c_(645706, _a_(645705, _n_(645704, "car2", lambda: car2), "description")))
_l_(645708)