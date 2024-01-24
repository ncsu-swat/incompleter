# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54318925/basemap-typeerror-input-must-be-an-array-list-tuple-or-scalar
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(689648)

except ImportError:
    pass
try:
    import numpy as np
    _l_(689650)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(689652)

except ImportError:
    pass
try:
    from mpl_toolkits.basemap import Basemap
    _l_(689654)

except ImportError:
    pass

data = _c_(689657, _a_(689656, _n_(689655, "pd", lambda: pd), "ExcelFile"), 'C:\\Users\\...xlsx')
_l_(689658)
data_input = _c_(689662, _a_(689660, _n_(689659, "pd", lambda: pd), "read_excel"), _n_(689661, "data", lambda: data), 'Sheet2')
_l_(689663)

# Extract the data we're interested in
lat = _a_(689665, _n_(689664, "data_input", lambda: data_input)['value1'], "values")
_l_(689666)
lon = _a_(689668, _n_(689667, "data_input", lambda: data_input)['value2'], "values")
_l_(689669)
capacity = _a_(689671, _n_(689670, "data_input", lambda: data_input)['value3'], "values")
_l_(689672)

# 1. Draw the map background
fig = _c_(689675, _a_(689674, _n_(689673, "plt", lambda: plt), "figure"), figsize=(8, 8))
_l_(689676)
m = _c_(689678, _n_(689677, "Basemap", lambda: Basemap), projection='lcc', resolution='h', 
            lat_0=31.1351682, lon_0=-99.3350553,
            width=1.3E6, height=1.25E6)
_l_(689679)
_c_(689682, _a_(689681, _n_(689680, "m", lambda: m), "shadedrelief"))
_l_(689683)
_c_(689686, _a_(689685, _n_(689684, "m", lambda: m), "drawcoastlines"), color='gray')
_l_(689687)
_c_(689690, _a_(689689, _n_(689688, "m", lambda: m), "drawcountries"), color='gray')
_l_(689691)
_c_(689694, _a_(689693, _n_(689692, "m", lambda: m), "drawstates"), color='gray')
_l_(689695)

# 2. scatter city data, with color reflecting population
# and size reflecting area
_c_(689705, _a_(689697, _n_(689696, "m", lambda: m), "scatter"), _n_(689698, "lon", lambda: lon), _n_(689699, "lat", lambda: lat), latlon=True,
          c=_c_(689703, _a_(689701, _n_(689700, "np", lambda: np), "log10"), _n_(689702, "capacity", lambda: capacity)), s=_n_(689704, "capacity", lambda: capacity),
          cmap='Reds', alpha=0.5)
_l_(689706)