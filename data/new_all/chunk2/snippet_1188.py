# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55314830/typeerror-not-supported-between-instances-of-nonetype-and-int
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pickle
    _l_(425496)

except ImportError:
    pass
try:
    import numpy as np
    _l_(425498)

except ImportError:
    pass
with _c_(425500, _n_(425499, "open", lambda: open), 'rf_model_1','rb') as f:
    _l_(425506)

    rf=_c_(425504, _a_(425502, _n_(425501, "pickle", lambda: pickle), "load"), _n_(425503, "f", lambda: f))
    _l_(425505)

xx = _c_(425511, _a_(425510, _c_(425509, _a_(425508, _n_(425507, "np", lambda: np), "array"), [67, 17832, 1, 1, 0, 33, 1941902452, 36, 33011.0, 19, 18, 0, 2, 1]), "reshape"), 1,-1)
_l_(425512)
_c_(425520, _n_(425513, "print", lambda: print), 'Class: ',_c_(425519, _n_(425514, "int", lambda: int), _c_(425518, _a_(425516, _n_(425515, "rf", lambda: rf), "predict"), _n_(425517, "xx", lambda: xx))))
_l_(425521)