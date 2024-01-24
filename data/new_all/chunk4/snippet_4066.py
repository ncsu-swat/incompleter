# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63224642/while-predicting-the-test-result-the-reshape-function-is-causing-an-error-attri
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
dataset = _c_(639213, _a_(639212, _n_(639211, "pd", lambda: pd), "read_csv"), "50_Startups.csv")
_l_(639214)

x = _a_(639216, _n_(639215, "dataset", lambda: dataset), "iloc")[:, :-1]
_l_(639217)
y = _a_(639219, _n_(639218, "dataset", lambda: dataset), "iloc")[:, -1]
_l_(639220)

_c_(639223, _n_(639221, "print", lambda: print), _n_(639222, "x", lambda: x))
_l_(639224)
_c_(639227, _n_(639225, "print", lambda: print), _n_(639226, "y", lambda: y))
_l_(639228)