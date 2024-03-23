# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(37027)

except ImportError:
    pass
try:
    import numpy as np
    _l_(37029)

except ImportError:
    pass
_c_(37033, _a_(37032, _a_(37031, _n_(37030, "np", lambda: np), "random"), "seed"), 24)
_l_(37034)
df = _c_(37040, _a_(37036, _n_(37035, "pd", lambda: pd), "DataFrame"), {'A': _c_(37039, _a_(37038, _n_(37037, "np", lambda: np), "linspace"), 1, 10, 10)})
_l_(37041)
_a_(37043, _n_(37042, "df", lambda: df), "iloc")[0, 2] = _a_(37045, _n_(37044, "np", lambda: np), "nan")
_l_(37046)
_a_(37048, _n_(37047, "df", lambda: df), "iloc")[3, 3] = _a_(37050, _n_(37049, "np", lambda: np), "nan")
_l_(37051)
_a_(37053, _n_(37052, "df", lambda: df), "iloc")[4, 1] = _a_(37055, _n_(37054, "np", lambda: np), "nan")
_l_(37056)
_a_(37058, _n_(37057, "df", lambda: df), "iloc")[9, 4] = _a_(37060, _n_(37059, "np", lambda: np), "nan")
_l_(37061)
_c_(37063, _n_(37062, "print", lambda: print), 'Original array:')
_l_(37064)
_c_(37067, _n_(37065, "print", lambda: print), _n_(37066, "df", lambda: df))
_l_(37068)
_c_(37070, _n_(37069, "print", lambda: print), '\nBackground:black - fontcolor:yelow')
_l_(37071)
_c_(37075, _a_(37074, _a_(37073, _n_(37072, "df", lambda: df), "style"), "set_properties"), **{'background-color': 'black', 'color': 'yellow'})
_l_(37076)