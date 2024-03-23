# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(24576)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(24578)

except ImportError:
    pass
char_list = _c_(24580, _n_(24579, "list", lambda: list), 'ABCDEFGHIJKLMNOP')
_l_(24581)
num_arra = _c_(24584, _a_(24583, _n_(24582, "np", lambda: np), "arange"), 8)
_l_(24585)
num_ser = _c_(24589, _a_(24587, _n_(24586, "pd", lambda: pd), "Series"), _n_(24588, "num_dict", lambda: num_dict))
_l_(24590)
df = _c_(24595, _a_(24594, _c_(24593, _a_(24592, _n_(24591, "num_ser", lambda: num_ser), "to_frame")), "reset_index"))
_l_(24596)
_c_(24601, _n_(24597, "print", lambda: print), _c_(24600, _a_(24599, _n_(24598, "df", lambda: df), "head")))
_l_(24602)