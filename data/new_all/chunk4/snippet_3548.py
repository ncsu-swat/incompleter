# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73698056/i-am-new-to-pandas-data-frame-i-am-getting-this-error-typeerror-can-only-conca
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(611519)

except ImportError:
    pass
try:
    import numpy as np
    _l_(611521)

except ImportError:
    pass
df = _c_(611524, _a_(611523, _n_(611522, "pd", lambda: pd), "read_excel"), "test123.xlsx")
_l_(611525)
_c_(611528, _n_(611526, "print", lambda: print), _n_(611527, "df", lambda: df))
_l_(611529)
subone = _n_(611530, "df", lambda: df)["F1"] + _n_(611531, "df", lambda: df)["I1"]
_l_(611532)
_c_(611535, _n_(611533, "print", lambda: print), _n_(611534, "subone", lambda: subone))
_l_(611536)