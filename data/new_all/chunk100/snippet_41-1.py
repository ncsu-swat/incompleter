# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(114885)

except ImportError:
    pass
_c_(114887, _n_(114886, "print", lambda: print), 'Original Series:')
_l_(114888)
_c_(114891, _n_(114889, "print", lambda: print), _n_(114890, "series1", lambda: series1))
_l_(114892)
result = _c_(114898, _a_(114894, _n_(114893, "series1", lambda: series1), "map"), lambda x: _c_(114897, _n_(114895, "len", lambda: len), _n_(114896, "x", lambda: x)))
_l_(114899)
_c_(114901, _n_(114900, "print", lambda: print), '\nNumber of characters in each word in the said series:')
_l_(114902)
_c_(114905, _n_(114903, "print", lambda: print), _n_(114904, "result", lambda: result))
_l_(114906)