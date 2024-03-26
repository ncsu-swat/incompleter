# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(112436)

except ImportError:
    pass
try:
    import numpy as np
    _l_(112438)

except ImportError:
    pass
_c_(112442, _a_(112441, _a_(112440, _n_(112439, "np", lambda: np), "random"), "seed"), 24)
_l_(112443)
df = _c_(112456, _a_(112445, _n_(112444, "pd", lambda: pd), "concat"), [_n_(112446, "df", lambda: df), _c_(112455, _a_(112448, _n_(112447, "pd", lambda: pd), "DataFrame"), _c_(112452, _a_(112451, _a_(112450, _n_(112449, "np", lambda: np), "random"), "randn"), 10, 4), columns=_c_(112454, _n_(112453, "list", lambda: list), 'BCDE'))], axis=1)
_l_(112457)
_c_(112459, _n_(112458, "print", lambda: print), 'Original array:')
_l_(112460)
_c_(112463, _n_(112461, "print", lambda: print), _n_(112462, "df", lambda: df))
_l_(112464)
_c_(112466, _n_(112465, "print", lambda: print), '\nDataframe - table style:')
_l_(112467)

def highlight_greaterthan(x):
    _l_(112473)

    if _a_(112469, _n_(112468, "x", lambda: x), "C") > 0.5:
        _l_(112472)

        aux = ['background-color: yellow'] * 5
        _l_(112470)
        return aux
    else:
        aux = ['background-color: white'] * 5
        _l_(112471)
        return aux
_c_(112478, _a_(112476, _a_(112475, _n_(112474, "df", lambda: df), "style"), "apply"), _n_(112477, "highlight_greaterthan", lambda: highlight_greaterthan), axis=1)
_l_(112479)