# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/22848621/how-do-i-solve-nameerror-name-threading-is-not-defined-in-python-3-3
#!/usr/bin/python

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import Utilities
    _l_(387265)

except ImportError:
    pass
try:
    import os
    _l_(387267)

except ImportError:
    pass
try:
    import sys
    _l_(387269)

except ImportError:
    pass
try:
    import getopt
    _l_(387271)

except ImportError:
    pass
try:
    import time
    _l_(387273)

except ImportError:
    pass
try:
    from queue import Queue
    _l_(387275)

except ImportError:
    pass
try:
    from threading import Thread
    _l_(387277)

except ImportError:
    pass

_db_lock=_c_(387280, _a_(387279, _n_(387278, "threading", lambda: threading), "Lock"))
_l_(387281)