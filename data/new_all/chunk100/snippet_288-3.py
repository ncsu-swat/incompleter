# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(108737)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(108739)

except ImportError:
    pass
char_list = _c_(108741, _n_(108740, "list", lambda: list), 'ABCDEFGHIJKLMNOP')
_l_(108742)
num_dict = _c_(108748, _n_(108743, "dict", lambda: dict), _c_(108747, _n_(108744, "zip", lambda: zip), _n_(108745, "char_list", lambda: char_list), _n_(108746, "num_arra", lambda: num_arra)))
_l_(108749)
num_ser = _c_(108753, _a_(108751, _n_(108750, "pd", lambda: pd), "Series"), _n_(108752, "num_dict", lambda: num_dict))
_l_(108754)
df = _c_(108759, _a_(108758, _c_(108757, _a_(108756, _n_(108755, "num_ser", lambda: num_ser), "to_frame")), "reset_index"))
_l_(108760)
_c_(108765, _n_(108761, "print", lambda: print), _c_(108764, _a_(108763, _n_(108762, "df", lambda: df), "head")))
_l_(108766)