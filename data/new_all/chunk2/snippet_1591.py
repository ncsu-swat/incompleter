# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74128016/quantstats-typeerror-invalid-comparison-between-dtype-datetime64ns-america
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import quantstats as qs
    _l_(435086)

except ImportError:
    pass

_c_(435089, _a_(435088, _n_(435087, "qs", lambda: qs), "extend_pandas"))
_l_(435090)

stock = _c_(435094, _a_(435093, _a_(435092, _n_(435091, "qs", lambda: qs), "utils"), "download_returns"), 'GLD')
_l_(435095)

_c_(435100, _a_(435098, _a_(435097, _n_(435096, "qs", lambda: qs), "reports"), "html"), _n_(435099, "stock", lambda: stock), output='Output/GLD.html')
_l_(435101)