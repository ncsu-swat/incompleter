# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71296396/why-is-this-showing-type-error-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import math
    _l_(646180)

except ImportError:
    pass
try:
    import os
    _l_(646182)

except ImportError:
    pass
try:
    import random
    _l_(646184)

except ImportError:
    pass
try:
    import re
    _l_(646186)

except ImportError:
    pass
try:
    import sys
    _l_(646188)

except ImportError:
    pass



def timeConversion(s):
    _l_(646228)

    if "P" in _n_(646189, "s", lambda: s):
        _l_(646227)

        x = _c_(646193, _a_(646191, _n_(646190, "re", lambda: re), "split"), "\W", _n_(646192, "s", lambda: s))
        _l_(646194)
        y = _c_(646197, _n_(646195, "int", lambda: int), _n_(646196, "x", lambda: x)[0]) + 12
        _l_(646198)
        z = _c_(646201, _n_(646199, "str", lambda: str), _n_(646200, "y", lambda: y))
        _l_(646202)
        a = _c_(646207, _a_(646204, _n_(646203, "re", lambda: re), "sub"), "^\d\d", _n_(646205, "z", lambda: z), _n_(646206, "s", lambda: s))
        _l_(646208)
        b = _c_(646212, _a_(646210, _n_(646209, "re", lambda: re), "sub"), "[a-zA-Z]", "", _n_(646211, "a", lambda: a))
        _l_(646213)
        _c_(646216, _n_(646214, "print", lambda: print), _n_(646215, "b", lambda: b))
        _l_(646217)
    else:
        b = _c_(646221, _a_(646219, _n_(646218, "re", lambda: re), "sub"), "[a-zA-z]", "", _n_(646220, "s", lambda: s))
        _l_(646222)
        _c_(646225, _n_(646223, "print", lambda: print), _n_(646224, "b", lambda: b))
        _l_(646226)

if _n_(646229, "_name_", lambda: _name_) == '_main_':
    _l_(646251)

    fptr = _c_(646233, _n_(646230, "open", lambda: open), _a_(646232, _n_(646231, "os", lambda: os), "environ")['OUTPUT_PATH'], 'w')
    _l_(646234)

    s = _c_(646236, _n_(646235, "raw_input", lambda: raw_input))
    _l_(646237)

    result = _c_(646240, _n_(646238, "timeConversion", lambda: timeConversion), _n_(646239, "s", lambda: s))
    _l_(646241)

    _c_(646245, _a_(646243, _n_(646242, "fptr", lambda: fptr), "write"), _n_(646244, "result", lambda: result), + '\n')
    _l_(646246)

    _c_(646249, _a_(646248, _n_(646247, "fptr", lambda: fptr), "close"))
    _l_(646250)