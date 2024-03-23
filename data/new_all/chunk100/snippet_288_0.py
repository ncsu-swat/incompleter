# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(24545)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(24547)

except ImportError:
    pass
char_list = _c_(24549, _n_(24548, "list", lambda: list), 'ABCDEFGHIJKLMNOP')
_l_(24550)
num_dict = _c_(24556, _n_(24551, "dict", lambda: dict), _c_(24555, _n_(24552, "zip", lambda: zip), _n_(24553, "char_list", lambda: char_list), _n_(24554, "num_arra", lambda: num_arra)))
_l_(24557)
num_ser = _c_(24561, _a_(24559, _n_(24558, "pd", lambda: pd), "Series"), _n_(24560, "num_dict", lambda: num_dict))
_l_(24562)
df = _c_(24567, _a_(24566, _c_(24565, _a_(24564, _n_(24563, "num_ser", lambda: num_ser), "to_frame")), "reset_index"))
_l_(24568)
_c_(24573, _n_(24569, "print", lambda: print), _c_(24572, _a_(24571, _n_(24570, "df", lambda: df), "head")))
_l_(24574)