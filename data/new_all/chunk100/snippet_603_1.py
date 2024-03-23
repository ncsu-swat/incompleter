# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(63270)

except ImportError:
    pass
try:
    import sys
    _l_(63272)

except ImportError:
    pass
arguments = ['hello.py']
_l_(63273)
_c_(63283, _n_(63274, "print", lambda: print), _c_(63282, _a_(63276, _n_(63275, "os", lambda: os), "execvp"), _n_(63277, "program", lambda: program), (_n_(63278, "program", lambda: program),) + _c_(63281, _n_(63279, "tuple", lambda: tuple), _n_(63280, "arguments", lambda: arguments))))
_l_(63284)
_c_(63286, _n_(63285, "print", lambda: print), 'Goodbye')
_l_(63287)