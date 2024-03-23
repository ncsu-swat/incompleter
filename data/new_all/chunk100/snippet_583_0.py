# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(60986)

except ImportError:
    pass
if _c_(60991, _a_(60989, _a_(60988, _n_(60987, "os", lambda: os), "path"), "isdir"), _n_(60990, "path", lambda: path)):
    _l_(61007)

    _c_(60993, _n_(60992, "print", lambda: print), '\nIt is a directory')
    _l_(60994)
elif _c_(60999, _a_(60997, _a_(60996, _n_(60995, "os", lambda: os), "path"), "isfile"), _n_(60998, "path", lambda: path)):
    _l_(61006)

    _c_(61001, _n_(61000, "print", lambda: print), '\nIt is a normal file')
    _l_(61002)
else:
    _c_(61004, _n_(61003, "print", lambda: print), 'It is a special file (socket, FIFO, device file)')
    _l_(61005)
_c_(61009, _n_(61008, "print", lambda: print))
_l_(61010)