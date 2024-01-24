# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55324792/nameerror-name-dates-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(357727)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(357729)

except ImportError:
    pass

df1 = _c_(357732, _a_(357731, _n_(357730, "pd", lambda: pd), "read_csv"), 'tcs.csv', index_col = 'Date', parse_dates = True)
_l_(357733)

idx = _a_(357736, _a_(357735, _n_(357734, "df1", lambda: df1), "loc")['2019-01-01':'2019-02-01'], "index")
_l_(357737)
stk = _a_(357739, _n_(357738, "df1", lambda: df1), "loc")['2019-01-01':'2019-02-01']['Close Price']
_l_(357740)

fig,ax =_c_(357743, _a_(357742, _n_(357741, "plt", lambda: plt), "subplots"))
_l_(357744)
_c_(357749, _a_(357746, _n_(357745, "ax", lambda: ax), "plot_date"), _n_(357747, "idx", lambda: idx),_n_(357748, "stk", lambda: stk),'-')
_l_(357750)

# ax.xaxis.grid(True)
# ax.yaxis.grid(True)

_c_(357757, _a_(357753, _a_(357752, _n_(357751, "ax", lambda: ax), "xaxis"), "set_major_locator"), _c_(357756, _a_(357755, _n_(357754, "dates", lambda: dates), "MonthLocator")))
_l_(357758)
_c_(357765, _a_(357761, _a_(357760, _n_(357759, "ax", lambda: ax), "xaxis"), "set_major_formatter"), _c_(357764, _a_(357763, _n_(357762, "dates", lambda: dates), "DateFormatter"), "%b-%y"))
_l_(357766)

_c_(357769, _a_(357768, _n_(357767, "fig", lambda: fig), "autofmt_xdate"))
_l_(357770)
_c_(357773, _a_(357772, _n_(357771, "plt", lambda: plt), "tight_layout"))
_l_(357774)