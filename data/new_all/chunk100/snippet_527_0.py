# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(53364)

except ImportError:
    pass
_c_(53366, _n_(53365, "print", lambda: print), 'Original Series:')
_l_(53367)
_c_(53370, _n_(53368, "print", lambda: print), _n_(53369, "series1", lambda: series1))
_l_(53371)
result = _c_(53381, _a_(53373, _n_(53372, "series1", lambda: series1), "map"), lambda x: _c_(53376, _a_(53375, _n_(53374, "x", lambda: x)[0], "upper")) + _n_(53377, "x", lambda: x)[1:-1] + _c_(53380, _a_(53379, _n_(53378, "x", lambda: x)[-1], "upper")))
_l_(53382)
_c_(53384, _n_(53383, "print", lambda: print), '\nFirst and last character of each word to upper case:')
_l_(53385)
_c_(53388, _n_(53386, "print", lambda: print), _n_(53387, "result", lambda: result))
_l_(53389)