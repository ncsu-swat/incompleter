# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59915199/error-nameerror-name-json-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from json import *
    _l_(359842)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(359844)

except ImportError:
    pass
try:
    import numpy as np
    _l_(359846)

except ImportError:
    pass
try:
    import os
    _l_(359848)

except ImportError:
    pass

fp=_c_(359850, _n_(359849, "open", lambda: open), "data1.json","r")
_l_(359851)
data=_c_(359855, _a_(359853, _n_(359852, "json", lambda: json), "loads"), _n_(359854, "fp", lambda: fp))
_l_(359856)
_c_(359859, _n_(359857, "print", lambda: print), _n_(359858, "data", lambda: data))
_l_(359860)

s=_c_(359864, _a_(359862, _n_(359861, "pd", lambda: pd), "Series"), _n_(359863, "data", lambda: data),index=[1,2])
_l_(359865)
_c_(359868, _n_(359866, "print", lambda: print), _n_(359867, "s", lambda: s))
_l_(359869)