# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55324792/nameerror-name-dates-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(362062)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(362064)

except ImportError:
    pass

df1 = _c_(362067, _a_(362066, _n_(362065, "pd", lambda: pd), "read_csv"), 'tcs.csv', index_col = 'Date', parse_dates = True)
_l_(362068)

idx = _a_(362071, _a_(362070, _n_(362069, "df1", lambda: df1), "loc")['2019-01-01':'2019-02-01'], "index")
_l_(362072)
stk = _a_(362074, _n_(362073, "df1", lambda: df1), "loc")['2019-01-01':'2019-02-01']['Close Price']
_l_(362075)

fig,ax =_c_(362078, _a_(362077, _n_(362076, "plt", lambda: plt), "subplots"))
_l_(362079)
_c_(362084, _a_(362081, _n_(362080, "ax", lambda: ax), "plot_date"), _n_(362082, "idx", lambda: idx),_n_(362083, "stk", lambda: stk),'-')
_l_(362085)

# ax.xaxis.grid(True)
# ax.yaxis.grid(True)

_c_(362092, _a_(362088, _a_(362087, _n_(362086, "ax", lambda: ax), "xaxis"), "set_major_locator"), _c_(362091, _a_(362090, _n_(362089, "dates", lambda: dates), "MonthLocator")))
_l_(362093)
_c_(362100, _a_(362096, _a_(362095, _n_(362094, "ax", lambda: ax), "xaxis"), "set_major_formatter"), _c_(362099, _a_(362098, _n_(362097, "dates", lambda: dates), "DateFormatter"), "%b-%y"))
_l_(362101)

_c_(362104, _a_(362103, _n_(362102, "fig", lambda: fig), "autofmt_xdate"))
_l_(362105)
_c_(362108, _a_(362107, _n_(362106, "plt", lambda: plt), "tight_layout"))
_l_(362109)