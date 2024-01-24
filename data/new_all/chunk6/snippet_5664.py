# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75650571/nameerror-name-df-is-not-definedpython
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(344212)

except ImportError:
    pass
# Using DataFrame.astype() function
_n_(344213, "df", lambda: df)["Date"] = _c_(344216, _a_(344215, _n_(344214, "df", lambda: df)["Date"], "astype"), 'datetime64[ns]')
_l_(344217)
_c_(344221, _n_(344218, "print", lambda: print), _a_(344220, _n_(344219, "df", lambda: df), "dtypes"))
_l_(344222)