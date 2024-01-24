# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61772088/ipython-name-error-name-x-is-not-defined
from __future__ import print_function
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_l_(698893)
try:
    import sys
    _l_(698895)

except ImportError:
    pass
try:
    from IPython.utils._tokenize_py2 import String
    _l_(698897)

except ImportError:
    pass
_c_(698901, _a_(698900, _a_(698899, _n_(698898, "sys", lambda: sys), "path"), "append"), '.')
_l_(698902)
try:
    import numpy, ctypes
    _l_(698904)

except ImportError:
    pass
Pylonlib = "/opt/pylon5/lib64/libpylonc.so"
_l_(698905)
try:
    from ctypes import cdll
    _l_(698907)

except ImportError:
    pass
libc = _c_(698911, _a_(698909, _n_(698908, "cdll", lambda: cdll), "LoadLibrary"), _n_(698910, "Pylonlib", lambda: Pylonlib))
_l_(698912)
_c_(698915, _a_(698914, _n_(698913, "libc", lambda: libc), "PylonInitialize"))
_l_(698916)
#### call any plyon function after you have initialized
_c_(698919, _a_(698918, _n_(698917, "libc", lambda: libc), "PylonTerminate"))
_l_(698920)