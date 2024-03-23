# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(35945)

except ImportError:
    pass
try:
    import numpy as np
    _l_(35947)

except ImportError:
    pass
_c_(35951, _a_(35950, _a_(35949, _n_(35948, "np", lambda: np), "random"), "seed"), 24)
_l_(35952)
df = _c_(35965, _a_(35954, _n_(35953, "pd", lambda: pd), "concat"), [_n_(35955, "df", lambda: df), _c_(35964, _a_(35957, _n_(35956, "pd", lambda: pd), "DataFrame"), _c_(35961, _a_(35960, _a_(35959, _n_(35958, "np", lambda: np), "random"), "randn"), 10, 4), columns=_c_(35963, _n_(35962, "list", lambda: list), 'BCDE'))], axis=1)
_l_(35966)
_c_(35968, _n_(35967, "print", lambda: print), 'Original array:')
_l_(35969)
_c_(35972, _n_(35970, "print", lambda: print), _n_(35971, "df", lambda: df))
_l_(35973)
_c_(35975, _n_(35974, "print", lambda: print), '\nDataframe - table style:')
_l_(35976)

def highlight_greaterthan(x):
    _l_(35982)

    if _a_(35978, _n_(35977, "x", lambda: x), "C") > 0.5:
        _l_(35981)

        aux = ['background-color: yellow'] * 5
        _l_(35979)
        return aux
    else:
        aux = ['background-color: white'] * 5
        _l_(35980)
        return aux
_c_(35987, _a_(35985, _a_(35984, _n_(35983, "df", lambda: df), "style"), "apply"), _n_(35986, "highlight_greaterthan", lambda: highlight_greaterthan), axis=1)
_l_(35988)