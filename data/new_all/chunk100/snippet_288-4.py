# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(108768)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(108770)

except ImportError:
    pass
num_arra = _c_(108773, _a_(108772, _n_(108771, "np", lambda: np), "arange"), 8)
_l_(108774)
num_dict = _c_(108780, _n_(108775, "dict", lambda: dict), _c_(108779, _n_(108776, "zip", lambda: zip), _n_(108777, "char_list", lambda: char_list), _n_(108778, "num_arra", lambda: num_arra)))
_l_(108781)
num_ser = _c_(108785, _a_(108783, _n_(108782, "pd", lambda: pd), "Series"), _n_(108784, "num_dict", lambda: num_dict))
_l_(108786)
df = _c_(108791, _a_(108790, _c_(108789, _a_(108788, _n_(108787, "num_ser", lambda: num_ser), "to_frame")), "reset_index"))
_l_(108792)
_c_(108797, _n_(108793, "print", lambda: print), _c_(108796, _a_(108795, _n_(108794, "df", lambda: df), "head")))
_l_(108798)