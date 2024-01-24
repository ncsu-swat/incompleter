# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57275824/matplotlib-error-attributeerror-int-object-has-no-attribute-toordinal
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from pandas_datareader import data
    _l_(681703)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(681705)

except ImportError:
    pass
try:
    from mpl_finance import candlestick2_ohlc
    _l_(681707)

except ImportError:
    pass
try:
    import matplotlib.dates as mdates
    _l_(681709)

except ImportError:
    pass
try:
    import fix_yahoo_finance as yf
    _l_(681711)

except ImportError:
    pass
try:
    import datetime
    _l_(681713)

except ImportError:
    pass

start = _c_(681716, _a_(681715, _n_(681714, "datetime", lambda: datetime), "date"), 2018, 1, 1)
_l_(681717)
end = _c_(681721, _a_(681720, _a_(681719, _n_(681718, "datetime", lambda: datetime), "date"), "today"))
_l_(681722)

aapl = _c_(681727, _a_(681724, _n_(681723, "yf", lambda: yf), "download"), "AAPL",_n_(681725, "start", lambda: start),_n_(681726, "end", lambda: end)) 
_l_(681728) 
_c_(681731, _a_(681730, _n_(681729, "aapl", lambda: aapl), "reset_index"), inplace=True)
_l_(681732)

_n_(681733, "aapl", lambda: aapl)['Date'] = _c_(681739, _a_(681736, _a_(681735, _n_(681734, "aapl", lambda: aapl), "index"), "map"), _a_(681738, _n_(681737, "mdates", lambda: mdates), "date2num"))
_l_(681740)

fig, ax = _c_(681743, _a_(681742, _n_(681741, "plt", lambda: plt), "subplots"))
_l_(681744)
_c_(681747, _a_(681746, _n_(681745, "plt", lambda: plt), "xlabel"), "Date")
_l_(681748)
_c_(681751, _a_(681750, _n_(681749, "plt", lambda: plt), "ylabel"), "Price")
_l_(681752)

_c_(681763, _n_(681753, "candlestick2_ohlc", lambda: candlestick2_ohlc), _n_(681754, "ax", lambda: ax), _a_(681756, _n_(681755, "aapl", lambda: aapl), "Open"), _a_(681758, _n_(681757, "aapl", lambda: aapl), "High"), _a_(681760, _n_(681759, "aapl", lambda: aapl), "Low"), _a_(681762, _n_(681761, "aapl", lambda: aapl), "Close"), width=1, colorup='g')
_l_(681764)
_c_(681767, _a_(681766, _n_(681765, "plt", lambda: plt), "savefig"), 'my_figure.png')
_l_(681768)
_c_(681771, _a_(681770, _n_(681769, "plt", lambda: plt), "show")) 
_l_(681772) 