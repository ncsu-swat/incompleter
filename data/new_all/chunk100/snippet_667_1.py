# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import defaultdict
    _l_(68684)

except ImportError:
    pass

def test(students):
    _l_(68703)

    obj = _c_(68687, _n_(68685, "defaultdict", lambda: defaultdict), _n_(68686, "list", lambda: list))
    _l_(68688)
    for (key, value) in _c_(68691, _a_(68690, _n_(68689, "students", lambda: students), "items")):
        _l_(68698)

        _c_(68696, _a_(68694, _n_(68692, "obj", lambda: obj)[_n_(68693, "value", lambda: value)], "append"), _n_(68695, "key", lambda: key))
        _l_(68697)
    aux = _c_(68701, _n_(68699, "dict", lambda: dict), _n_(68700, "obj", lambda: obj))
    _l_(68702)
    return aux
_c_(68708, _n_(68704, "print", lambda: print), _c_(68707, _n_(68705, "test", lambda: test), _n_(68706, "students", lambda: students)))
_l_(68709)