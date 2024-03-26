# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(108650)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(108652)

except ImportError:
    pass
char_list = _c_(108654, _n_(108653, "list", lambda: list), 'ABCDEFGHIJKLMNOP')
_l_(108655)
num_arra = _c_(108658, _a_(108657, _n_(108656, "np", lambda: np), "arange"), 8)
_l_(108659)
num_ser = _c_(108663, _a_(108661, _n_(108660, "pd", lambda: pd), "Series"), _n_(108662, "num_dict", lambda: num_dict))
_l_(108664)
df = _c_(108669, _a_(108668, _c_(108667, _a_(108666, _n_(108665, "num_ser", lambda: num_ser), "to_frame")), "reset_index"))
_l_(108670)
_c_(108675, _n_(108671, "print", lambda: print), _c_(108674, _a_(108673, _n_(108672, "df", lambda: df), "head")))
_l_(108676)