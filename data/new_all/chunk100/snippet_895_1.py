# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(87956)

except ImportError:
    pass
try:
    import numpy as np
    _l_(87958)

except ImportError:
    pass
_c_(87962, _a_(87961, _a_(87960, _n_(87959, "np", lambda: np), "random"), "seed"), 24)
_l_(87963)
df = _c_(87969, _a_(87965, _n_(87964, "pd", lambda: pd), "DataFrame"), {'A': _c_(87968, _a_(87967, _n_(87966, "np", lambda: np), "linspace"), 1, 10, 10)})
_l_(87970)
_a_(87972, _n_(87971, "df", lambda: df), "iloc")[0, 2] = _a_(87974, _n_(87973, "np", lambda: np), "nan")
_l_(87975)
_a_(87977, _n_(87976, "df", lambda: df), "iloc")[3, 3] = _a_(87979, _n_(87978, "np", lambda: np), "nan")
_l_(87980)
_a_(87982, _n_(87981, "df", lambda: df), "iloc")[4, 1] = _a_(87984, _n_(87983, "np", lambda: np), "nan")
_l_(87985)
_a_(87987, _n_(87986, "df", lambda: df), "iloc")[9, 4] = _a_(87989, _n_(87988, "np", lambda: np), "nan")
_l_(87990)
_c_(87992, _n_(87991, "print", lambda: print), 'Original array:')
_l_(87993)
_c_(87996, _n_(87994, "print", lambda: print), _n_(87995, "df", lambda: df))
_l_(87997)

def highlight_min(s):
    _l_(88006)

    """
    highlight the minimum in a Series red.
    """
    is_max = _n_(87998, "s", lambda: s) == _c_(88001, _a_(88000, _n_(87999, "s", lambda: s), "min"))
    _l_(88002)
    aux = ['background-color: red' if _n_(88003, "v", lambda: v) else '' for v in _n_(88004, "is_max", lambda: is_max)]
    _l_(88005)
    return aux
_c_(88008, _n_(88007, "print", lambda: print), '\nHighlight the minimum value in each column:')
_l_(88009)
_c_(88016, _a_(88012, _a_(88011, _n_(88010, "df", lambda: df), "style"), "apply"), _n_(88013, "highlight_min", lambda: highlight_min), subset=_a_(88015, _n_(88014, "pd", lambda: pd), "IndexSlice")[:, ['B', 'C', 'D', 'E']])
_l_(88017)