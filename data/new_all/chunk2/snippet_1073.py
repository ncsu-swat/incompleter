# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/45290161/attributeerror-module-object-has-no-attributes-extension-when-trying-to-use
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(453884)

except ImportError:
    pass
try:
    import numpy as np
    _l_(453886)

except ImportError:
    pass
try:
    import holoviews as hv
    _l_(453888)

except ImportError:
    pass
_c_(453891, _a_(453890, _n_(453889, "hv", lambda: hv), "extension"), 'bokeh')
_l_(453892)