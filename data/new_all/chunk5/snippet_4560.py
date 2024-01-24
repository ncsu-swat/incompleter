# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55540107/how-to-fix-attributeerror-function-object-has-no-attribute-rcparams
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(679051)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(679053)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(679055)

except ImportError:
    pass

df = _c_(679058, _a_(679057, _n_(679056, "pd", lambda: pd), "read_csv"), 'train.csv', index_col='time')
_l_(679059)
_c_(679062, _a_(679061, _n_(679060, "df", lambda: df), "sort_values"), by='time')
_l_(679063)

_c_(679067, _a_(679065, _n_(679064, "plt", lambda: plt), "plot"), _n_(679066, "df", lambda: df)['ecg'], label='data', color="orange")
_l_(679068)

_a_(679071, _a_(679070, _n_(679069, "plt", lambda: plt), "plot"), "rcParams")['agg.path.chunksize'] = 20000
_l_(679072)


_c_(679075, _a_(679074, _n_(679073, "plt", lambda: plt), "title"), "ECG Data")
_l_(679076)
_c_(679079, _a_(679078, _n_(679077, "plt", lambda: plt), "grid"))
_l_(679080)
_c_(679083, _a_(679082, _n_(679081, "plt", lambda: plt), "legend"))
_l_(679084)
_c_(679087, _a_(679086, _n_(679085, "plt", lambda: plt), "tight_layout"))
_l_(679088)
_c_(679091, _a_(679090, _n_(679089, "plt", lambda: plt), "show"))
_l_(679092)