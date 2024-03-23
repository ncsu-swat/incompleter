# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(24636)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(24638)

except ImportError:
    pass
char_list = _c_(24640, _n_(24639, "list", lambda: list), 'ABCDEFGHIJKLMNOP')
_l_(24641)
num_arra = _c_(24644, _a_(24643, _n_(24642, "np", lambda: np), "arange"), 8)
_l_(24645)
num_dict = _c_(24651, _n_(24646, "dict", lambda: dict), _c_(24650, _n_(24647, "zip", lambda: zip), _n_(24648, "char_list", lambda: char_list), _n_(24649, "num_arra", lambda: num_arra)))
_l_(24652)
df = _c_(24657, _a_(24656, _c_(24655, _a_(24654, _n_(24653, "num_ser", lambda: num_ser), "to_frame")), "reset_index"))
_l_(24658)
_c_(24663, _n_(24659, "print", lambda: print), _c_(24662, _a_(24661, _n_(24660, "df", lambda: df), "head")))
_l_(24664)