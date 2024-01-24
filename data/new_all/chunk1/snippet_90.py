# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59132467/concat-2-columns-in-pandas-attributeerror-dataframe-object-has-no-attribute
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(411360)

except ImportError:
    pass
try:
    import numpy as np
    _l_(411362)

except ImportError:
    pass
try:
    from statsmodels import api as sm
    _l_(411364)

except ImportError:
    pass
try:
    import pandas_datareader.data as web
    _l_(411366)

except ImportError:
    pass
try:
    import datetime
    _l_(411368)

except ImportError:
    pass

start = _c_(411371, _a_(411370, _n_(411369, "datetime", lambda: datetime), "datetime"), 2015,2,12)
_l_(411372)
end = _c_(411376, _a_(411375, _a_(411374, _n_(411373, "datetime", lambda: datetime), "datetime"), "today"))
_l_(411377)
df = _c_(411382, _a_(411379, _n_(411378, "web", lambda: web), "get_data_yahoo"), ['F', '^GSPC'], _n_(411380, "start", lambda: start), _n_(411381, "end", lambda: end))
_l_(411383)

df1 = _c_(411388, _a_(411385, _n_(411384, "df", lambda: df), "concat"), columns=[_n_(411386, "F", lambda: F)['Close'], _n_(411387, "gspc", lambda: gspc)['Close']], axis=1)
_l_(411389)