# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53936383/folium-geo-mapping-leads-to-typeerror-must-be-real-number-not-str-while
#!/usr/bin/env python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(681581)

except ImportError:
    pass
try:
    import requests
    _l_(681583)

except ImportError:
    pass
try:
    from xml.etree import ElementTree
    _l_(681585)

except ImportError:
    pass
try:
    import numpy as np
    _l_(681587)

except ImportError:
    pass
try:
    import folium
    _l_(681589)

except ImportError:
    pass

xml_data = "coords.xml"
_l_(681590)

tree = _c_(681594, _a_(681592, _n_(681591, "ElementTree", lambda: ElementTree), "parse"), _n_(681593, "xml_data", lambda: xml_data))
_l_(681595)
counter = _c_(681598, _a_(681597, _n_(681596, "tree", lambda: tree), "find"), 'counter')
_l_(681599)

id = []
_l_(681600)
name = []
_l_(681601)
latitude = []
_l_(681602)
longitude = []
_l_(681603)

for c in _c_(681606, _a_(681605, _n_(681604, "tree", lambda: tree), "findall"), 'counter'):
    _l_(681637)

    _c_(681611, _a_(681608, _n_(681607, "id", lambda: id), "append"), _a_(681610, _n_(681609, "c", lambda: c), "attrib")['id'])
    _l_(681612)
    _c_(681619, _a_(681614, _n_(681613, "name", lambda: name), "append"), _a_(681618, _c_(681617, _a_(681616, _n_(681615, "c", lambda: c), "find"), 'name'), "text"))
    _l_(681620)
    _c_(681627, _a_(681622, _n_(681621, "latitude", lambda: latitude), "append"), _a_(681626, _c_(681625, _a_(681624, _n_(681623, "c", lambda: c), "find"), 'latitude'), "text"))
    _l_(681628)
    _c_(681635, _a_(681630, _n_(681629, "longitude", lambda: longitude), "append"), _a_(681634, _c_(681633, _a_(681632, _n_(681631, "c", lambda: c), "find"), 'longitude'), "text"))
    _l_(681636)

df_counters = _c_(681644, _a_(681639, _n_(681638, "pd", lambda: pd), "DataFrame"), {'ID' : _n_(681640, "id", lambda: id),
    'Name' : _n_(681641, "name", lambda: name),
    'latitude' : _n_(681642, "latitude", lambda: latitude),
    'longitude' : _n_(681643, "longitude", lambda: longitude)
    })
_l_(681645)
_c_(681648, _a_(681647, _n_(681646, "df_counters", lambda: df_counters), "head"))
_l_(681649)

locations = _n_(681650, "df_counters", lambda: df_counters)[['latitude', 'longitude']]
_l_(681651)
locationlist = _c_(681655, _a_(681654, _a_(681653, _n_(681652, "locations", lambda: locations), "values"), "tolist"))
_l_(681656)

map = _c_(681659, _a_(681658, _n_(681657, "folium", lambda: folium), "Map"), location=[47.3, 5.2], zoom_start=10)
_l_(681660)
for point in _c_(681665, _n_(681661, "range", lambda: range), 0, _c_(681664, _n_(681662, "len", lambda: len), _n_(681663, "locationlist", lambda: locationlist))):
    _l_(681677)

    _c_(681675, _a_(681673, _c_(681672, _a_(681667, _n_(681666, "folium", lambda: folium), "Marker"), _n_(681668, "locationlist", lambda: locationlist)[_n_(681669, "point", lambda: point)], popup=_n_(681670, "df_counters", lambda: df_counters)['Name'][_n_(681671, "point", lambda: point)]), "add_to"), _n_(681674, "map", lambda: map))
    _l_(681676)
_n_(681678, "map", lambda: map)
_l_(681679)