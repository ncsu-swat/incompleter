# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67344205/pybacktest-library-hello-world-error-builtins-attributeerror-series-object-h
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import matplotlib
    _l_(568998)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(569000)

except ImportError:
    pass
try:
    import pybacktest
    _l_(569002)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(569004)

except ImportError:
    pass

short_ma = 50
_l_(569005)
long_ma = 200
_l_(569006)

ohlc = _c_(569009, _a_(569008, _n_(569007, "pybacktest", lambda: pybacktest), "load_from_yahoo"), 'AAPL', start=2000)
_l_(569010)
_c_(569013, _a_(569012, _n_(569011, "ohlc", lambda: ohlc), "tail"))
_l_(569014)

ms = _c_(569021, _a_(569020, _c_(569019, _a_(569017, _a_(569016, _n_(569015, "ohlc", lambda: ohlc), "C"), "rolling"), _n_(569018, "short_ma", lambda: short_ma)), "mean"))
_l_(569022)
ml = _c_(569029, _a_(569028, _c_(569027, _a_(569025, _a_(569024, _n_(569023, "ohlc", lambda: ohlc), "C"), "rolling"), _n_(569026, "long_ma", lambda: long_ma)), "mean"))
_l_(569030)

buy = cover = (_n_(569031, "ms", lambda: ms) > _n_(569032, "ml", lambda: ml)) & (_c_(569035, _a_(569034, _n_(569033, "ms", lambda: ms), "shift")) < _c_(569038, _a_(569037, _n_(569036, "ml", lambda: ml), "shift")))  # ma cross up
_l_(569039)  # ma cross up
sell = short = (_n_(569040, "ms", lambda: ms) < _n_(569041, "ml", lambda: ml)) & (_c_(569044, _a_(569043, _n_(569042, "ms", lambda: ms), "shift")) > _c_(569047, _a_(569046, _n_(569045, "ml", lambda: ml), "shift")))  # ma cross down
_l_(569048)  # ma cross down

bt = _c_(569053, _a_(569050, _n_(569049, "pybacktest", lambda: pybacktest), "Backtest"), _c_(569052, _n_(569051, "locals", lambda: locals)), 'ma_cross')
_l_(569054)

_c_(569059, _n_(569055, "print", lambda: print), _c_(569058, _a_(569057, _n_(569056, "bt", lambda: bt), "summary")))
_l_(569060)

_c_(569063, _a_(569062, _n_(569061, "bt", lambda: bt), "plot_equity"))
_l_(569064)