# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(108678)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(108680)

except ImportError:
    pass
char_list = _c_(108682, _n_(108681, "list", lambda: list), 'ABCDEFGHIJKLMNOP')
_l_(108683)
num_arra = _c_(108686, _a_(108685, _n_(108684, "np", lambda: np), "arange"), 8)
_l_(108687)
num_dict = _c_(108693, _n_(108688, "dict", lambda: dict), _c_(108692, _n_(108689, "zip", lambda: zip), _n_(108690, "char_list", lambda: char_list), _n_(108691, "num_arra", lambda: num_arra)))
_l_(108694)
num_ser = _c_(108698, _a_(108696, _n_(108695, "pd", lambda: pd), "Series"), _n_(108697, "num_dict", lambda: num_dict))
_l_(108699)
_c_(108704, _n_(108700, "print", lambda: print), _c_(108703, _a_(108702, _n_(108701, "df", lambda: df), "head")))
_l_(108705)