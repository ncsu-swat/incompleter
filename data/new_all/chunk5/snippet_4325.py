# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59652669/attributeerror-module-pandas-compat-has-no-attribute-binary-type
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas_datareader as web
    _l_(698407)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(698409)

except ImportError:
    pass

df = _c_(698412, _a_(698411, _n_(698410, "web", lambda: web), "DataReader"), 'RTSI', 'moex', start='2015-01-01', end='2019-12-30')
_l_(698413)
_n_(698414, "df", lambda: df)
_l_(698415)