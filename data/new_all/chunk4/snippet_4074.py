# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63224642/while-predicting-the-test-result-the-reshape-function-is-causing-an-error-attri
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
dataset = _c_(595764, _a_(595763, _n_(595762, "pd", lambda: pd), "read_csv"), "50_Startups.csv")
_l_(595765)

x = _a_(595767, _n_(595766, "dataset", lambda: dataset), "iloc")[:, :-1]
_l_(595768)
y = _a_(595770, _n_(595769, "dataset", lambda: dataset), "iloc")[:, -1]
_l_(595771)

_c_(595774, _n_(595772, "print", lambda: print), _n_(595773, "x", lambda: x))
_l_(595775)
_c_(595778, _n_(595776, "print", lambda: print), _n_(595777, "y", lambda: y))
_l_(595779)