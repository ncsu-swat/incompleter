# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65795814/dask-series-mean-compute-results-in-typeerror-sum-got-an-unexpected-ke
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(568390)

except ImportError:
    pass
try:
    import numpy as np
    _l_(568392)

except ImportError:
    pass
try:
    from dask import dataframe as dd
    _l_(568394)

except ImportError:
    pass

df = _c_(568397, _a_(568396, _n_(568395, "pd", lambda: pd), "DataFrame"), {'foo': [[1,2,3], [4,5,6]]})
_l_(568398)
ddf = _c_(568402, _a_(568400, _n_(568399, "dd", lambda: dd), "from_pandas"), _n_(568401, "df", lambda: df), npartitions=2) 
_l_(568403) 