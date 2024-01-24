# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56079085/how-do-i-overcome-the-typeerror-cannot-convert-the-series-to-class-float-er
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(689953)

except ImportError:
    pass
try:
    from math import radians, cos, sin, asin, sqrt
    _l_(689955)

except ImportError:
    pass
# convert decimal degrees to radians 
lon1 = _c_(689959, _a_(689957, _n_(689956, "df1", lambda: df1)['from_lon'], "map"), _n_(689958, "radians", lambda: radians))
_l_(689960)
lat1 = _c_(689964, _a_(689962, _n_(689961, "df1", lambda: df1)['from_lat'], "map"), _n_(689963, "radians", lambda: radians))
_l_(689965)
lon2 = _c_(689969, _a_(689967, _n_(689966, "df1", lambda: df1)['dest_lon'], "map"), _n_(689968, "radians", lambda: radians))
_l_(689970)
lat2 = _c_(689974, _a_(689972, _n_(689971, "df1", lambda: df1)['dest_lat'], "map"), _n_(689973, "radians", lambda: radians))
_l_(689975)
# haversine formula 
dlon = _n_(689976, "lon2", lambda: lon2) - _n_(689977, "lon1", lambda: lon1) 
_l_(689978) 
dlat = _n_(689979, "lat2", lambda: lat2) - _n_(689980, "lat1", lambda: lat1) 
_l_(689981) 
a = _c_(689984, _n_(689982, "sin", lambda: sin), _n_(689983, "dlat", lambda: dlat)/2)**2 + _c_(689987, _n_(689985, "cos", lambda: cos), _n_(689986, "lat1", lambda: lat1)) * _c_(689990, _n_(689988, "cos", lambda: cos), _n_(689989, "lat2", lambda: lat2)) * _c_(689993, _n_(689991, "sin", lambda: sin), _n_(689992, "dlon", lambda: dlon)/2)**2
_l_(689994)
c = 2 * _c_(689999, _n_(689995, "asin", lambda: asin), _c_(689998, _n_(689996, "sqrt", lambda: sqrt), _n_(689997, "a", lambda: a)))
_l_(690000)
results = 3959.0 * _n_(690001, "c", lambda: c)
_l_(690002)