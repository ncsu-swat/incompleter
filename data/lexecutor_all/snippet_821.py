# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/918154/relative-paths-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import ntpath
    _l_(1543870)

except ImportError:
    pass
try:
    import os
    _l_(1543872)

except ImportError:
    pass
dirname = _c_(1543876, _a_(1543874, _n_(1543873, "ntpath", lambda: ntpath), "dirname"), _n_(1543875, "__file__", lambda: __file__))
_l_(1543877)
filename = _c_(1543882, _a_(1543880, _a_(1543879, _n_(1543878, "os", lambda: os), "path"), "join"), _n_(1543881, "dirname", lambda: dirname), 'relative/path/to/file/you/want')
_l_(1543883)

