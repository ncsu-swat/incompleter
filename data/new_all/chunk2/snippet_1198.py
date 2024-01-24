# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51846824/using-unittest-mock-patch-dict-on-os-environ-is-resulting-in-a-typeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(421020)

except ImportError:
    pass
try:
    from unittest.mock import patch
    _l_(421022)

except ImportError:
    pass
with _c_(421025, _a_(421024, _n_(421023, "patch", lambda: patch), "dict"), 'os.environ', values={"foo": 3, "bar": "hello"}, clear=True):
    _l_(421036)

    _c_(421029, _n_(421026, "print", lambda: print), _a_(421028, _n_(421027, "os", lambda: os), "environ")["foo"])
    _l_(421030)
    _c_(421034, _n_(421031, "print", lambda: print), _a_(421033, _n_(421032, "os", lambda: os), "environ")["bar"])
    _l_(421035)