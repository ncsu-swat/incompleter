# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
result = {}
_l_(64824)
for (key, value) in _c_(64827, _a_(64826, _n_(64825, "student_data", lambda: student_data), "items")):
    _l_(64837)

    if _n_(64828, "value", lambda: value) not in _c_(64831, _a_(64830, _n_(64829, "result", lambda: result), "values")):
        _l_(64836)

        _n_(64832, "result", lambda: result)[_n_(64833, "key", lambda: key)] = _n_(64834, "value", lambda: value)
        _l_(64835)
_c_(64840, _n_(64838, "print", lambda: print), _n_(64839, "result", lambda: result))
_l_(64841)