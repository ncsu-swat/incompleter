# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61442914/python-error-using-panda-attributeerror-series-object-has-no-attribute-astyp
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(351281)

except ImportError:
    pass

data = _c_(351284, _a_(351283, _n_(351282, "pd", lambda: pd), "read_csv"), 'artwork_sample.csv')
_l_(351285)

_a_(351287, _n_(351286, "data", lambda: data), "dtypes")
_l_(351288)