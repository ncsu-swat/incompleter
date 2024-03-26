# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(104003)

except ImportError:
    pass
try:
    import numpy as np
    _l_(104005)

except ImportError:
    pass
_c_(104009, _a_(104008, _a_(104007, _n_(104006, "np", lambda: np), "random"), "seed"), 24)
_l_(104010)
df = _c_(104023, _a_(104012, _n_(104011, "pd", lambda: pd), "concat"), [_n_(104013, "df", lambda: df), _c_(104022, _a_(104015, _n_(104014, "pd", lambda: pd), "DataFrame"), _c_(104019, _a_(104018, _a_(104017, _n_(104016, "np", lambda: np), "random"), "randn"), 10, 4), columns=_c_(104021, _n_(104020, "list", lambda: list), 'BCDE'))], axis=1)
_l_(104024)
_a_(104026, _n_(104025, "df", lambda: df), "iloc")[0, 2] = _a_(104028, _n_(104027, "np", lambda: np), "nan")
_l_(104029)
_a_(104031, _n_(104030, "df", lambda: df), "iloc")[3, 3] = _a_(104033, _n_(104032, "np", lambda: np), "nan")
_l_(104034)
_a_(104036, _n_(104035, "df", lambda: df), "iloc")[4, 1] = _a_(104038, _n_(104037, "np", lambda: np), "nan")
_l_(104039)
_a_(104041, _n_(104040, "df", lambda: df), "iloc")[9, 4] = _a_(104043, _n_(104042, "np", lambda: np), "nan")
_l_(104044)
_c_(104046, _n_(104045, "print", lambda: print), 'Original array:')
_l_(104047)
_c_(104050, _n_(104048, "print", lambda: print), _n_(104049, "df", lambda: df))
_l_(104051)

def color_negative_red(val):
    _l_(104056)

    color = 'red' if _n_(104052, "val", lambda: val) < 0 else 'black'
    _l_(104053)
    aux = 'color: %s' % _n_(104054, "color", lambda: color)
    _l_(104055)
    return aux
_c_(104058, _n_(104057, "print", lambda: print), '\nNegative numbers red and positive numbers black:')
_l_(104059)
_c_(104063, _a_(104062, _a_(104061, _n_(104060, "df", lambda: df), "style"), "highlight_null"), null_color='red')
_l_(104064)