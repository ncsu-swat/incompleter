# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1987694/how-do-i-print-the-full-numpy-array-without-truncation
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(1542940)

except ImportError:
    pass
_c_(1542951, _n_(1542941, "print", lambda: print), _c_(1542950, _n_(1542942, "str", lambda: str), _c_(1542949, _a_(1542948, _c_(1542947, _a_(1542946, _c_(1542945, _a_(1542944, _n_(1542943, "np", lambda: np), "arange"), 10000), "reshape"), 250,40), "tolist"))))
_l_(1542952)

