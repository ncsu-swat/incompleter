# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62862895/attributeerror-map-object-has-no-attribute-simple-marker-in-folium
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import folium
    _l_(651910)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(651912)

except ImportError:
    pass
 
SF_COORDINATES = (37.76, -122.45)
_l_(651913)
crimedata = _c_(651916, _a_(651915, _n_(651914, "pd", lambda: pd), "read_csv"), 'SFPD_Incidents_2015.csv')
_l_(651917)
 
# for speed purposes
MAX_RECORDS = 1000
_l_(651918)
  
# create empty map zoomed in on San Francisco
map = _c_(651922, _a_(651920, _n_(651919, "folium", lambda: folium), "Map"), location=_n_(651921, "SF_COORDINATES", lambda: SF_COORDINATES), zoom_start=12)
_l_(651923)
 
# add a marker for every record in the filtered data, use a clustered view
for each in _c_(651927, _a_(651926, _n_(651924, "crimedata", lambda: crimedata)[0:_n_(651925, "MAX_RECORDS", lambda: MAX_RECORDS)], "iterrows")):
    _l_(651934)

    _c_(651932, _a_(651929, _n_(651928, "map", lambda: map), "simple_marker"), location = [_n_(651930, "each", lambda: each)[1]['Y'],_n_(651931, "each", lambda: each)[1]['X']], 
        clustered_marker = True)
    _l_(651933)
  
_c_(651937, _n_(651935, "display", lambda: display), _n_(651936, "map", lambda: map))
_l_(651938)