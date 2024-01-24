# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72495771/attributeerror-module-wsgi-has-no-attribute-application
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import imp
    _l_(543036)

except ImportError:
    pass
try:
    import os
    _l_(543038)

except ImportError:
    pass
try:
    import sys
    _l_(543040)

except ImportError:
    pass


_c_(543049, _a_(543043, _a_(543042, _n_(543041, "sys", lambda: sys), "path"), "insert"), 0, _c_(543048, _a_(543046, _a_(543045, _n_(543044, "os", lambda: os), "path"), "dirname"), _n_(543047, "__file__", lambda: __file__)))
_l_(543050)

wsgi = _c_(543053, _a_(543052, _n_(543051, "imp", lambda: imp), "load_source"), 'wsgi', 'app.py')
_l_(543054)
application = _a_(543056, _n_(543055, "wsgi", lambda: wsgi), "application")
_l_(543057)