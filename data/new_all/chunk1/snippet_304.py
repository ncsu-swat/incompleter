# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/47999393/typeerror-init-got-an-unexpected-keyword-argument-encoding
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(380797)

except ImportError:
    pass
...
_l_(380798)

url = "https://coinmarketcap.com/currencies/bitcoin/historical-data/?start=20130428&end="+_c_(380801, _a_(380800, _n_(380799, "time", lambda: time), "strftime"), "%Y%m%d")
_l_(380802)

# CODE FAILS HERE
bitcoin_market_info = _c_(380806, _a_(380804, _n_(380803, "pd", lambda: pd), "read_html"), _n_(380805, "url", lambda: url))[0]
_l_(380807)