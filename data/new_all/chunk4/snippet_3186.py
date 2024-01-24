# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/8041625/multithreading-attempt-using-python-3-2-2-attributeerror-str-object-has-no
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import threading
    _l_(599238)

except ImportError:
    pass

class AsyncScript(_a_(599240, _n_(599239, "threading", lambda: threading), "Thread")):
    _l_(599257)

    def __init__(self, s):
        _l_(599250)

        _c_(599245, _a_(599243, _a_(599242, _n_(599241, "threading", lambda: threading), "Thread"), "__init__"), _n_(599244, "self", lambda: self))
        _l_(599246)
        _n_(599247, "self", lambda: self).script = _n_(599248, "s", lambda: s)
        _l_(599249)
    def run(self):
        _l_(599256)

        _c_(599254, _n_(599251, "print", lambda: print), "This would run script " + _a_(599253, _n_(599252, "self", lambda: self), "script"))
        _l_(599255)

_c_(599261, _a_(599260, _c_(599259, _n_(599258, "AsyncScript", lambda: AsyncScript), "sample script path string"), "start"))
_l_(599262)