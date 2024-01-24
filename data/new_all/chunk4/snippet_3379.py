# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75155197/typeerror-string-indices-must-be-integers-in-the-time-of-downloading-stock-data
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(583612)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(583614)

except ImportError:
    pass
try:
    import seaborn as sns
    _l_(583616)

except ImportError:
    pass
try:
    import pandas_datareader.data as web
    _l_(583618)

except ImportError:
    pass
try:
    import datetime
    _l_(583620)

except ImportError:
    pass

start=_c_(583623, _a_(583622, _n_(583621, "datetime", lambda: datetime), "datetime"), 2015,6,1)
_l_(583624)
end=_c_(583627, _a_(583626, _n_(583625, "datetime", lambda: datetime), "datetime"), 2022,6,30)
_l_(583628)

sbin=_c_(583633, _a_(583630, _n_(583629, "web", lambda: web), "DataReader"), 'SBIN.BO','yahoo',_n_(583631, "start", lambda: start),_n_(583632, "end", lambda: end))
_l_(583634)
tatamotors=_c_(583639, _a_(583636, _n_(583635, "web", lambda: web), "DataReader"), 'TATAMOTORS.BO','yahoo',_n_(583637, "start", lambda: start),_n_(583638, "end", lambda: end))
_l_(583640)
reliance=_c_(583645, _a_(583642, _n_(583641, "web", lambda: web), "DataReader"), 'RELIANCE.BO','yahoo',_n_(583643, "start", lambda: start),_n_(583644, "end", lambda: end))
_l_(583646)