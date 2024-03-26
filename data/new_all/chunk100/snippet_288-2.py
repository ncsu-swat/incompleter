# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(108707)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(108709)

except ImportError:
    pass
char_list = _c_(108711, _n_(108710, "list", lambda: list), 'ABCDEFGHIJKLMNOP')
_l_(108712)
num_arra = _c_(108715, _a_(108714, _n_(108713, "np", lambda: np), "arange"), 8)
_l_(108716)
num_dict = _c_(108722, _n_(108717, "dict", lambda: dict), _c_(108721, _n_(108718, "zip", lambda: zip), _n_(108719, "char_list", lambda: char_list), _n_(108720, "num_arra", lambda: num_arra)))
_l_(108723)
df = _c_(108728, _a_(108727, _c_(108726, _a_(108725, _n_(108724, "num_ser", lambda: num_ser), "to_frame")), "reset_index"))
_l_(108729)
_c_(108734, _n_(108730, "print", lambda: print), _c_(108733, _a_(108732, _n_(108731, "df", lambda: df), "head")))
_l_(108735)