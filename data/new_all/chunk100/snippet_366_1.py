# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(35990)

except ImportError:
    pass
try:
    import numpy as np
    _l_(35992)

except ImportError:
    pass
_c_(35996, _a_(35995, _a_(35994, _n_(35993, "np", lambda: np), "random"), "seed"), 24)
_l_(35997)
df = _c_(36003, _a_(35999, _n_(35998, "pd", lambda: pd), "DataFrame"), {'A': _c_(36002, _a_(36001, _n_(36000, "np", lambda: np), "linspace"), 1, 10, 10)})
_l_(36004)
_c_(36006, _n_(36005, "print", lambda: print), 'Original array:')
_l_(36007)
_c_(36010, _n_(36008, "print", lambda: print), _n_(36009, "df", lambda: df))
_l_(36011)
_c_(36013, _n_(36012, "print", lambda: print), '\nDataframe - table style:')
_l_(36014)

def highlight_greaterthan(x):
    _l_(36020)

    if _a_(36016, _n_(36015, "x", lambda: x), "C") > 0.5:
        _l_(36019)

        aux = ['background-color: yellow'] * 5
        _l_(36017)
        return aux
    else:
        aux = ['background-color: white'] * 5
        _l_(36018)
        return aux
_c_(36025, _a_(36023, _a_(36022, _n_(36021, "df", lambda: df), "style"), "apply"), _n_(36024, "highlight_greaterthan", lambda: highlight_greaterthan), axis=1)
_l_(36026)