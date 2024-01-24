# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49425270/attribute-error-map-object-has-no-attribute-create-map
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import folium
    _l_(379888)

except ImportError:
    pass
map_osm = _c_(379891, _a_(379890, _n_(379889, "folium", lambda: folium), "Map"), location=[45.5236, -122.6750])
_l_(379892)
_c_(379895, _a_(379894, _n_(379893, "map_osm", lambda: map_osm), "create_map"), path='osm.html')
_l_(379896)