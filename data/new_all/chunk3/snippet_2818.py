# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62120840/why-am-i-getting-an-error-typeerror-system-takes-at-most-1-argument-3-given
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(533601)

except ImportError:
    pass

currentinfo = _c_(533603, _n_(533602, "input", lambda: input), "Enter username: ")
_l_(533604)

_c_(533608, _a_(533606, _n_(533605, "os", lambda: os), "system"), 'echo', "Username:", _n_(533607, "currentinfo", lambda: currentinfo), ">> info.txt")
_l_(533609)