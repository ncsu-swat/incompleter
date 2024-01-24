# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62825992/python-file-not-found-error-using-pd-read
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(687644)

except ImportError:
    pass
try:
    import numpy as np
    _l_(687646)

except ImportError:
    pass
try:
    from sklearn.impute import SimpleImputer
    _l_(687648)

except ImportError:
    pass

df=_c_(687651, _a_(687650, _n_(687649, "pd", lambda: pd), "read_csv"), r'C:\Users\sergi\Downloads\covid_19_data.cvs')
_l_(687652)