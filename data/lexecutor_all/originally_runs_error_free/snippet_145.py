# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/3430372/how-do-i-get-the-full-path-of-the-current-files-directory
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(1548841)

except ImportError:
    pass
_c_(1548848, _n_(1548842, "print", lambda: print), _c_(1548847, _a_(1548845, _a_(1548844, _n_(1548843, "os", lambda: os), "path"), "dirname"), _n_(1548846, "__file__", lambda: __file__)))
_l_(1548849)

