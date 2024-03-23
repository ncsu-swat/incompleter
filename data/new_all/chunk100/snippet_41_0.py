# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(41205)

except ImportError:
    pass
_c_(41207, _n_(41206, "print", lambda: print), 'Original Series:')
_l_(41208)
_c_(41211, _n_(41209, "print", lambda: print), _n_(41210, "series1", lambda: series1))
_l_(41212)
result = _c_(41218, _a_(41214, _n_(41213, "series1", lambda: series1), "map"), lambda x: _c_(41217, _n_(41215, "len", lambda: len), _n_(41216, "x", lambda: x)))
_l_(41219)
_c_(41221, _n_(41220, "print", lambda: print), '\nNumber of characters in each word in the said series:')
_l_(41222)
_c_(41225, _n_(41223, "print", lambda: print), _n_(41224, "result", lambda: result))
_l_(41226)