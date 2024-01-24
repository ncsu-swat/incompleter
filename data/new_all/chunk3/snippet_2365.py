# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/48592965/attributeerror-module-peakutils-has-no-attribute-indexes
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(571390)

except ImportError:
    pass
try:
    import peakutils
    _l_(571392)

except ImportError:
    pass
try:
    from peakutils import *
    _l_(571394)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(571396)

except ImportError:
    pass

estimated_data = _c_(571399, _a_(571398, _n_(571397, "pd", lambda: pd), "read_csv"), "file", header=None)
_l_(571400)
col1 = _n_(571401, "estimated_data", lambda: estimated_data)[:][0]  # First column data
_l_(571402)  # First column data
col2 = _n_(571403, "estimated_data", lambda: estimated_data)[:][1]  # Second column data
_l_(571404)  # Second column data

index = _c_(571408, _a_(571406, _n_(571405, "peakutils", lambda: peakutils), "indexes"), _n_(571407, "col2", lambda: col2), thres=0.4, min_dist=1000)
_l_(571409)

_c_(571414, _a_(571411, _n_(571410, "plt", lambda: plt), "plot"), _n_(571412, "col1", lambda: col1), _n_(571413, "col2", lambda: col2), lw=0.4, alpha=0.4)
_l_(571415)
_c_(571422, _a_(571417, _n_(571416, "plt", lambda: plt), "plot"), _n_(571418, "col1", lambda: col1)[_n_(571419, "index", lambda: index)], _n_(571420, "col2", lambda: col2)[_n_(571421, "index", lambda: index)], marker="o", ls="", ms=3)
_l_(571423)

_c_(571426, _a_(571425, _n_(571424, "plt", lambda: plt), "show"))
_l_(571427)