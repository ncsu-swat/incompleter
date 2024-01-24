# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50060699/matplotlib-typeerror-unsupported-operand-types-for-datetime-date-and-fl
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import matplotlib.pyplot as plt
    _l_(379048)

except ImportError:
    pass
try:
    from pylab import rcParams
    _l_(379050)

except ImportError:
    pass
try:
    import matplotlib.ticker as mtick
    _l_(379052)

except ImportError:
    pass
try:
    import matplotlib.dates as mdates
    _l_(379054)

except ImportError:
    pass
try:
    import numpy as np
    _l_(379056)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(379058)

except ImportError:
    pass
try:
    from datetime import datetime, timedelta
    _l_(379060)

except ImportError:
    pass

DF = _c_(379076, _a_(379062, _n_(379061, "pd", lambda: pd), "DataFrame"), {
    'day':     [_c_(379066, _a_(379065, _c_(379064, _n_(379063, "datetime", lambda: datetime), 2018,1,1), "date"))+_c_(379069, _n_(379067, "timedelta", lambda: timedelta), _n_(379068, "x", lambda: x)+1) for x in _c_(379071, _n_(379070, "range", lambda: range), 100)],
    'balance': _c_(379075, _a_(379074, _a_(379073, _n_(379072, "np", lambda: np), "random"), "normal"), 100,100,100)
})
_l_(379077)
_n_(379078, "rcParams", lambda: rcParams)['figure.figsize'] = 20, 10
_l_(379079)
fig, ax = _c_(379082, _a_(379081, _n_(379080, "plt", lambda: plt), "subplots"))
_l_(379083)
_c_(379088, _a_(379085, _n_(379084, "ax", lambda: ax), "bar"), _n_(379086, "DF", lambda: DF)['day'], _n_(379087, "DF", lambda: DF)['balance'], color='lightblue')
_l_(379089)
_c_(379092, _a_(379091, _n_(379090, "plt", lambda: plt), "xlabel"), 'day', fontsize=20)
_l_(379093)
myFmt = _c_(379096, _a_(379095, _n_(379094, "mdates", lambda: mdates), "DateFormatter"), '%Y-%m')
_l_(379097)
_c_(379102, _a_(379100, _a_(379099, _n_(379098, "ax", lambda: ax), "xaxis"), "set_major_formatter"), _n_(379101, "myFmt", lambda: myFmt))
_l_(379103)
_c_(379106, _a_(379105, _n_(379104, "plt", lambda: plt), "show"))
_l_(379107)