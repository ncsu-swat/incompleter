# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62365323/williams-r-ta-lib-getting-typeerror-with-look-back-period
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(467070)

except ImportError:
    pass
try:
    from pandas_datareader import data as web
    _l_(467072)

except ImportError:
    pass
try:
    import ta
    _l_(467074)

except ImportError:
    pass


df = _c_(467077, _a_(467076, _n_(467075, "web", lambda: web), "DataReader"), 'F', 'yahoo')
_l_(467078)

williams1 = _c_(467085, _a_(467081, _a_(467080, _n_(467079, "ta", lambda: ta), "momentum"), "WilliamsRIndicator"), high = _n_(467082, "df", lambda: df)['High'], 
        low = _n_(467083, "df", lambda: df)['Low'], 
        close = _n_(467084, "df", lambda: df)['Close'], 
        fillna = False
        )
_l_(467086)

_c_(467089, _a_(467088, _n_(467087, "williams1", lambda: williams1), "wr"))
_l_(467090)