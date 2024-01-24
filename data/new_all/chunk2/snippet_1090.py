# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/33684848/typeerror-strptime-argument-0-must-be-str-not-class-bytes
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(454660)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(454662)

except ImportError:
    pass
try:
    import matplotlib.dates as mdates
    _l_(454664)

except ImportError:
    pass
try:
    from datetime import datetime
    _l_(454666)

except ImportError:
    pass

days, impressions = _c_(454672, _a_(454668, _n_(454667, "np", lambda: np), "loadtxt"), "page-impressions.csv", unpack=True,
        converters={ 0: _c_(454671, _a_(454670, _n_(454669, "mdates", lambda: mdates), "strpdate2num"), '%Y-%m-%d')})
_l_(454673)

_c_(454678, _a_(454675, _n_(454674, "plt", lambda: plt), "plot_date"), x=_n_(454676, "days", lambda: days), y=_n_(454677, "impressions", lambda: impressions), fmt="r-")
_l_(454679)
_c_(454682, _a_(454681, _n_(454680, "plt", lambda: plt), "title"), "Pageessions on example.com")
_l_(454683)
_c_(454686, _a_(454685, _n_(454684, "plt", lambda: plt), "ylabel"), "Page impressions")
_l_(454687)
_c_(454690, _a_(454689, _n_(454688, "plt", lambda: plt), "grid"), True)
_l_(454691)

_c_(454694, _a_(454693, _n_(454692, "plt", lambda: plt), "savefig"), 'test.pdf', format='pdf')
_l_(454695)