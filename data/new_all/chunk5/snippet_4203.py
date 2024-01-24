# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61772088/ipython-name-error-name-x-is-not-defined
from __future__ import print_function
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_l_(654947)
try:
    import sys
    _l_(654949)

except ImportError:
    pass
try:
    from IPython.utils._tokenize_py2 import String
    _l_(654951)

except ImportError:
    pass
_c_(654955, _a_(654954, _a_(654953, _n_(654952, "sys", lambda: sys), "path"), "append"), '.')
_l_(654956)
try:
    import numpy, ctypes
    _l_(654958)

except ImportError:
    pass
Pylonlib = "/opt/pylon5/lib64/libpylonc.so"
_l_(654959)
try:
    from ctypes import cdll
    _l_(654961)

except ImportError:
    pass
libc = _c_(654965, _a_(654963, _n_(654962, "cdll", lambda: cdll), "LoadLibrary"), _n_(654964, "Pylonlib", lambda: Pylonlib))
_l_(654966)
_c_(654969, _a_(654968, _n_(654967, "libc", lambda: libc), "PylonInitialize"))
_l_(654970)
#### call any plyon function after you have initialized
_c_(654973, _a_(654972, _n_(654971, "libc", lambda: libc), "PylonTerminate"))
_l_(654974)