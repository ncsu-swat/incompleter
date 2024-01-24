# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62862895/attributeerror-map-object-has-no-attribute-simple-marker-in-folium
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import folium
    _l_(647494)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(647496)

except ImportError:
    pass
 
SF_COORDINATES = (37.76, -122.45)
_l_(647497)
crimedata = _c_(647500, _a_(647499, _n_(647498, "pd", lambda: pd), "read_csv"), 'SFPD_Incidents_2015.csv')
_l_(647501)
 
# for speed purposes
MAX_RECORDS = 1000
_l_(647502)
  
# create empty map zoomed in on San Francisco
map = _c_(647506, _a_(647504, _n_(647503, "folium", lambda: folium), "Map"), location=_n_(647505, "SF_COORDINATES", lambda: SF_COORDINATES), zoom_start=12)
_l_(647507)
 
# add a marker for every record in the filtered data, use a clustered view
for each in _c_(647511, _a_(647510, _n_(647508, "crimedata", lambda: crimedata)[0:_n_(647509, "MAX_RECORDS", lambda: MAX_RECORDS)], "iterrows")):
    _l_(647518)

    _c_(647516, _a_(647513, _n_(647512, "map", lambda: map), "simple_marker"), location = [_n_(647514, "each", lambda: each)[1]['Y'],_n_(647515, "each", lambda: each)[1]['X']], 
        clustered_marker = True)
    _l_(647517)
  
_c_(647521, _n_(647519, "display", lambda: display), _n_(647520, "map", lambda: map))
_l_(647522)