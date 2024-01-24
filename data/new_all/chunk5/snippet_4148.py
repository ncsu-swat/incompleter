# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61088917/getting-an-attributeerror-module-pandas-has-no-attribute-plotting-when-tr
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import folium
    _l_(684276)

except ImportError:
    pass
map = _c_(684279, _a_(684278, _n_(684277, "folium", lambda: folium), "Map"), location=[80, -100])
_l_(684280)
_c_(684283, _a_(684282, _n_(684281, "map", lambda: map), "save"), "Map1.html")
_l_(684284)