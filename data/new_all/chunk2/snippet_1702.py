# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62187152/python3-attributeerror-int-object-has-no-attribute-length
#!/bin/python3
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(465628)

except ImportError:
    pass
try:
    import sys
    _l_(465630)

except ImportError:
    pass
try:
    import numpy
    _l_(465632)

except ImportError:
    pass
try:
    import office2john
    _l_(465634)

except ImportError:
    pass

def passwordVerifier(password):
    _l_(465671)

    password = _c_(465637, _n_(465635, "str", lambda: str), _n_(465636, "password", lambda: password))
    _l_(465638)
    verifier = [_c_(465641, _a_(465640, _n_(465639, "numpy", lambda: numpy), "uint16"), 1)] 
    _l_(465642) 
    passwordArray = [_c_(465645, _a_(465644, _n_(465643, "numpy", lambda: numpy), "uint8"), 1)]
    _l_(465646)
    verifier = 0x0000
    _l_(465647)

    passwordArray = [0]
    _l_(465648)
    passwordArray = _c_(465650, _n_(465649, "bytes", lambda: bytes), [])                           
    _l_(465651)                           
    passwordArray = _c_(465654, _a_(465653, _n_(465652, "password", lambda: password), "length"))
    _l_(465655)


    for password in _n_(465656, "passwordArray", lambda: passwordArray):
        _l_(465670)

        intermediate1 = 0 
        _l_(465657) 
        if _n_(465658, "password", lambda: password) in _n_(465659, "passwordArray", lambda: passwordArray):
            _l_(465667)

            intermediate1 = 1 
            _l_(465660) 
        else: 
            intermediate2 = _n_(465661, "verifier", lambda: verifier) * 2 
            _l_(465662) 
            intermediate3 = _n_(465663, "intermediate1", lambda: intermediate1) 
            _l_(465664) 
            verifier = _n_(465665, "intermediate3", lambda: intermediate3)
            _l_(465666)
        aux = _n_(465668, "verifier", lambda: verifier)
        _l_(465669)
        return aux