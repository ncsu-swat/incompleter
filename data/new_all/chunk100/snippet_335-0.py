# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import platform as pl
    _l_(110900)

except ImportError:
    pass
for key in _n_(110901, "os_profile", lambda: os_profile):
    _l_(110918)

    if _c_(110905, _n_(110902, "hasattr", lambda: hasattr), _n_(110903, "pl", lambda: pl), _n_(110904, "key", lambda: key)):
        _l_(110917)

        _c_(110915, _n_(110906, "print", lambda: print), _n_(110907, "key", lambda: key) + ': ' + _c_(110914, _n_(110908, "str", lambda: str), _c_(110913, _c_(110912, _n_(110909, "getattr", lambda: getattr), _n_(110910, "pl", lambda: pl), _n_(110911, "key", lambda: key)))))
        _l_(110916)