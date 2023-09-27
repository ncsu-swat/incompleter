# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/247770/how-to-retrieve-a-modules-path
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(1541938)

except ImportError:
    pass
try:
    import inspect
    _l_(1541940)

except ImportError:
    pass
_c_(1541944, _a_(1541942, _n_(1541941, "inspect", lambda: inspect), "getfile"), _n_(1541943, "os", lambda: os))
_l_(1541945)
'/usr/lib64/python2.7/os.pyc'
_l_(1541946)
_c_(1541950, _a_(1541948, _n_(1541947, "inspect", lambda: inspect), "getfile"), _n_(1541949, "inspect", lambda: inspect))
_l_(1541951)
'/usr/lib64/python2.7/inspect.pyc'
_l_(1541952)
_c_(1541960, _a_(1541955, _a_(1541954, _n_(1541953, "os", lambda: os), "path"), "dirname"), _c_(1541959, _a_(1541957, _n_(1541956, "inspect", lambda: inspect), "getfile"), _n_(1541958, "inspect", lambda: inspect)))
_l_(1541961)
'/usr/lib64/python2.7'
_l_(1541962)

