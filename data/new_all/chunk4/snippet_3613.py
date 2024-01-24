# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71296396/why-is-this-showing-type-error-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import math
    _l_(631533)

except ImportError:
    pass
try:
    import os
    _l_(631535)

except ImportError:
    pass
try:
    import random
    _l_(631537)

except ImportError:
    pass
try:
    import re
    _l_(631539)

except ImportError:
    pass
try:
    import sys
    _l_(631541)

except ImportError:
    pass



def timeConversion(s):
    _l_(631581)

    if "P" in _n_(631542, "s", lambda: s):
        _l_(631580)

        x = _c_(631546, _a_(631544, _n_(631543, "re", lambda: re), "split"), "\W", _n_(631545, "s", lambda: s))
        _l_(631547)
        y = _c_(631550, _n_(631548, "int", lambda: int), _n_(631549, "x", lambda: x)[0]) + 12
        _l_(631551)
        z = _c_(631554, _n_(631552, "str", lambda: str), _n_(631553, "y", lambda: y))
        _l_(631555)
        a = _c_(631560, _a_(631557, _n_(631556, "re", lambda: re), "sub"), "^\d\d", _n_(631558, "z", lambda: z), _n_(631559, "s", lambda: s))
        _l_(631561)
        b = _c_(631565, _a_(631563, _n_(631562, "re", lambda: re), "sub"), "[a-zA-Z]", "", _n_(631564, "a", lambda: a))
        _l_(631566)
        _c_(631569, _n_(631567, "print", lambda: print), _n_(631568, "b", lambda: b))
        _l_(631570)
    else:
        b = _c_(631574, _a_(631572, _n_(631571, "re", lambda: re), "sub"), "[a-zA-z]", "", _n_(631573, "s", lambda: s))
        _l_(631575)
        _c_(631578, _n_(631576, "print", lambda: print), _n_(631577, "b", lambda: b))
        _l_(631579)

if _n_(631582, "_name_", lambda: _name_) == '_main_':
    _l_(631604)

    fptr = _c_(631586, _n_(631583, "open", lambda: open), _a_(631585, _n_(631584, "os", lambda: os), "environ")['OUTPUT_PATH'], 'w')
    _l_(631587)

    s = _c_(631589, _n_(631588, "raw_input", lambda: raw_input))
    _l_(631590)

    result = _c_(631593, _n_(631591, "timeConversion", lambda: timeConversion), _n_(631592, "s", lambda: s))
    _l_(631594)

    _c_(631598, _a_(631596, _n_(631595, "fptr", lambda: fptr), "write"), _n_(631597, "result", lambda: result), + '\n')
    _l_(631599)

    _c_(631602, _a_(631601, _n_(631600, "fptr", lambda: fptr), "close"))
    _l_(631603)