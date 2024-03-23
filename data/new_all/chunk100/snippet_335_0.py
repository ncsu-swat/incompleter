# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import platform as pl
    _l_(33398)

except ImportError:
    pass
for key in _n_(33399, "os_profile", lambda: os_profile):
    _l_(33416)

    if _c_(33403, _n_(33400, "hasattr", lambda: hasattr), _n_(33401, "pl", lambda: pl), _n_(33402, "key", lambda: key)):
        _l_(33415)

        _c_(33413, _n_(33404, "print", lambda: print), _n_(33405, "key", lambda: key) + ': ' + _c_(33412, _n_(33406, "str", lambda: str), _c_(33411, _c_(33410, _n_(33407, "getattr", lambda: getattr), _n_(33408, "pl", lambda: pl), _n_(33409, "key", lambda: key)))))
        _l_(33414)