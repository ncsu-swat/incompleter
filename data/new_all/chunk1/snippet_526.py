# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53064690/attributeerror-map-object-has-no-attribute-marker
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import folium
    _l_(408574)

except ImportError:
    pass
try:
    from folium.plugins import MarkerCluster
    _l_(408576)

except ImportError:
    pass

map1 = _c_(408580, _a_(408578, _n_(408577, "folium", lambda: folium), "Map"), location=_n_(408579, "SF_COORDINATES", lambda: SF_COORDINATES), zoom_start=12)
_l_(408581)
marker_cluster = _c_(408586, _a_(408584, _c_(408583, _n_(408582, "MarkerCluster", lambda: MarkerCluster)), "add_to"), _n_(408585, "map1", lambda: map1)) 
_l_(408587) 

for each in _c_(408591, _a_(408590, _n_(408588, "data", lambda: data)[0:_n_(408589, "MAX_RECORDS", lambda: MAX_RECORDS)], "iterrows")):
    _l_(408601)

    _c_(408599, _a_(408597, _c_(408596, _a_(408593, _n_(408592, "map1", lambda: map1), "Marker"), location = [_n_(408594, "each", lambda: each)[1]['Y'],_n_(408595, "each", lambda: each)[1]['X']], 
    clustered_marker = True), "add_to"), _n_(408598, "marker_cluster", lambda: marker_cluster))
    _l_(408600)

_c_(408604, _n_(408602, "display", lambda: display), _n_(408603, "map1", lambda: map1))
_l_(408605)