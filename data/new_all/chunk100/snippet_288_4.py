# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(24666)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(24668)

except ImportError:
    pass
char_list = _c_(24670, _n_(24669, "list", lambda: list), 'ABCDEFGHIJKLMNOP')
_l_(24671)
num_arra = _c_(24674, _a_(24673, _n_(24672, "np", lambda: np), "arange"), 8)
_l_(24675)
num_dict = _c_(24681, _n_(24676, "dict", lambda: dict), _c_(24680, _n_(24677, "zip", lambda: zip), _n_(24678, "char_list", lambda: char_list), _n_(24679, "num_arra", lambda: num_arra)))
_l_(24682)
num_ser = _c_(24686, _a_(24684, _n_(24683, "pd", lambda: pd), "Series"), _n_(24685, "num_dict", lambda: num_dict))
_l_(24687)
_c_(24692, _n_(24688, "print", lambda: print), _c_(24691, _a_(24690, _n_(24689, "df", lambda: df), "head")))
_l_(24693)