# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49868472/gmap-draw-typeerror-must-be-real-number-not-str
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import gmplot
    _l_(459130)

except ImportError:
    pass

gmap = _c_(459134, _a_(459133, _a_(459132, _n_(459131, "gmplot", lambda: gmplot), "GoogleMapPlotter"), "from_geocode"), "Los Angeles",10)
_l_(459135)

_c_(459140, _a_(459137, _n_(459136, "gmap", lambda: gmap), "heatmap"), _n_(459138, "lat_lon", lambda: lat_lon)['latitude'], _n_(459139, "lat_lon", lambda: lat_lon)['longitude'])
_l_(459141)

_c_(459144, _a_(459143, _n_(459142, "gmap", lambda: gmap), "draw"), 'crime_map.html')
_l_(459145)