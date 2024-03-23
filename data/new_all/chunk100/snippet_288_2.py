# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(24604)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(24606)

except ImportError:
    pass
num_arra = _c_(24609, _a_(24608, _n_(24607, "np", lambda: np), "arange"), 8)
_l_(24610)
num_dict = _c_(24616, _n_(24611, "dict", lambda: dict), _c_(24615, _n_(24612, "zip", lambda: zip), _n_(24613, "char_list", lambda: char_list), _n_(24614, "num_arra", lambda: num_arra)))
_l_(24617)
num_ser = _c_(24621, _a_(24619, _n_(24618, "pd", lambda: pd), "Series"), _n_(24620, "num_dict", lambda: num_dict))
_l_(24622)
df = _c_(24627, _a_(24626, _c_(24625, _a_(24624, _n_(24623, "num_ser", lambda: num_ser), "to_frame")), "reset_index"))
_l_(24628)
_c_(24633, _n_(24629, "print", lambda: print), _c_(24632, _a_(24631, _n_(24630, "df", lambda: df), "head")))
_l_(24634)