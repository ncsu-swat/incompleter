# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(94173)

except ImportError:
    pass
try:
    import numpy as np
    _l_(94175)

except ImportError:
    pass
_c_(94179, _a_(94178, _a_(94177, _n_(94176, "np", lambda: np), "random"), "seed"), 24)
_l_(94180)
df = _c_(94193, _a_(94182, _n_(94181, "pd", lambda: pd), "concat"), [_n_(94183, "df", lambda: df), _c_(94192, _a_(94185, _n_(94184, "pd", lambda: pd), "DataFrame"), _c_(94189, _a_(94188, _a_(94187, _n_(94186, "np", lambda: np), "random"), "randn"), 10, 4), columns=_c_(94191, _n_(94190, "list", lambda: list), 'BCDE'))], axis=1)
_l_(94194)
_c_(94196, _n_(94195, "print", lambda: print), 'Original array:')
_l_(94197)
_c_(94200, _n_(94198, "print", lambda: print), _n_(94199, "df", lambda: df))
_l_(94201)
_c_(94203, _n_(94202, "print", lambda: print), '\nDataframe - Gradient color:')
_l_(94204)
_c_(94208, _a_(94207, _a_(94206, _n_(94205, "df", lambda: df), "style"), "background_gradient"), subset=['C'])
_l_(94209)