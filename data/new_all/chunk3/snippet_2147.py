# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61205314/nameerror-name-os-pathlike-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(571379)

except ImportError:
    pass
try:
    import os
    _l_(571381)

except ImportError:
    pass

a = _c_(571387, _a_(571383, _n_(571382, "np", lambda: np), "loadtxt"), _c_(571386, _a_(571385, _n_(571384, "os", lambda: os), "getcwd"))+'abc.txt')
_l_(571388)