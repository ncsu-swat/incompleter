# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75650571/nameerror-name-df-is-not-definedpython
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(369041)

except ImportError:
    pass
# Using DataFrame.astype() function
_n_(369042, "df", lambda: df)["Date"] = _c_(369045, _a_(369044, _n_(369043, "df", lambda: df)["Date"], "astype"), 'datetime64[ns]')
_l_(369046)
_c_(369050, _n_(369047, "print", lambda: print), _a_(369049, _n_(369048, "df", lambda: df), "dtypes"))
_l_(369051)