# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53308766/bokehgetting-typeerror-object-of-type-polygon-is-not-json-serializable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import shapefile
    _l_(685669)

except ImportError:
    pass
try:
    import itertools
    _l_(685671)

except ImportError:
    pass

shp = _c_(685673, _n_(685672, "open", lambda: open), "/Users/xxxx/Desktop/cb_2015_us_state_500k/cb_2015_us_state_500k.shp", "rb")
_l_(685674)
dbf = _c_(685676, _n_(685675, "open", lambda: open), "/Users/xxxx/Desktop/cb_2015_us_state_500k/cb_2015_us_state_500k.dbf", "rb")
_l_(685677)
sf = _c_(685682, _a_(685679, _n_(685678, "shapefile", lambda: shapefile), "Reader"), shp=_n_(685680, "shp", lambda: shp), dbf=_n_(685681, "dbf", lambda: dbf))
_l_(685683)

lats = []
_l_(685684)
lons = []
_l_(685685)
ct_name = []
_l_(685686)
st_id = []
_l_(685687)
ct_state_name = []
_l_(685688)
for shprec in _c_(685691, _a_(685690, _n_(685689, "sf", lambda: sf), "shapeRecords")):
    _l_(685773)

    _c_(685698, _a_(685693, _n_(685692, "st_id", lambda: st_id), "append"), _c_(685697, _n_(685694, "int", lambda: int), _a_(685696, _n_(685695, "shprec", lambda: shprec), "record")[0]))
    _l_(685699)
    _c_(685704, _a_(685701, _n_(685700, "ct_name", lambda: ct_name), "append"), _a_(685703, _n_(685702, "shprec", lambda: shprec), "record")[5])
    _l_(685705)
    _c_(685710, _a_(685707, _n_(685706, "ct_state_name", lambda: ct_state_name), "append"), _a_(685709, _n_(685708, "shprec", lambda: shprec), "record")[4])
    _l_(685711)
    lat, lon = _c_(685719, _n_(685712, "map", lambda: map), _n_(685713, "list", lambda: list), _c_(685718, _n_(685714, "zip", lambda: zip), *_a_(685717, _a_(685716, _n_(685715, "shprec", lambda: shprec), "shape"), "points")))
    _l_(685720)
    indices = _c_(685725, _a_(685724, _a_(685723, _a_(685722, _n_(685721, "shprec", lambda: shprec), "shape"), "parts"), "tolist"))
    _l_(685726)
    lat = [_n_(685727, "lat", lambda: lat)[_n_(685728, "i", lambda: i):_n_(685729, "j", lambda: j)] + [_c_(685731, _n_(685730, "float", lambda: float), 'NaN')] for i, j in _c_(685735, _n_(685732, "zip", lambda: zip), _n_(685733, "indices", lambda: indices), _n_(685734, "indices", lambda: indices)[1:]+[None])]
    _l_(685736)
    lon = [_n_(685737, "lon", lambda: lon)[_n_(685738, "i", lambda: i):_n_(685739, "j", lambda: j)] + [_c_(685741, _n_(685740, "float", lambda: float), 'NaN')] for i, j in _c_(685745, _n_(685742, "zip", lambda: zip), _n_(685743, "indices", lambda: indices), _n_(685744, "indices", lambda: indices)[1:]+[None])]
    _l_(685746)
    lat = _c_(685753, _n_(685747, "list", lambda: list), _c_(685752, _a_(685750, _a_(685749, _n_(685748, "itertools", lambda: itertools), "chain"), "from_iterable"), _n_(685751, "lat", lambda: lat)))
    _l_(685754)
    lon = _c_(685761, _n_(685755, "list", lambda: list), _c_(685760, _a_(685758, _a_(685757, _n_(685756, "itertools", lambda: itertools), "chain"), "from_iterable"), _n_(685759, "lon", lambda: lon)))
    _l_(685762)
    _c_(685766, _a_(685764, _n_(685763, "lats", lambda: lats), "append"), _n_(685765, "lat", lambda: lat))
    _l_(685767)
    _c_(685771, _a_(685769, _n_(685768, "lons", lambda: lons), "append"), _n_(685770, "lon", lambda: lon))
    _l_(685772)

map_data = _c_(685781, _a_(685775, _n_(685774, "pd", lambda: pd), "DataFrame"), {'x': _n_(685776, "lats", lambda: lats), 'y': _n_(685777, "lons", lambda: lons), 'state': _n_(685778, "st_id", lambda: st_id), 'county_name': _n_(685779, "ct_name", lambda: ct_name), 'ct_state_name': _n_(685780, "ct_state_name", lambda: ct_state_name)})
_l_(685782)
map_data_m = _n_(685783, "map_data", lambda: map_data)[_c_(685787, _a_(685786, _a_(685785, _n_(685784, "map_data", lambda: map_data), "ct_state_name"), "isin"), ['NJ'])]    
_l_(685788)    

source = _c_(685791, _n_(685789, "ColumnDataSource", lambda: ColumnDataSource), _n_(685790, "map_data_m", lambda: map_data_m))
_l_(685792)

TOOLS="pan,wheel_zoom,box_zoom,reset,hover,save"
_l_(685793)

p = _c_(685796, _n_(685794, "figure", lambda: figure), title="Title", tools=_n_(685795, "TOOLS", lambda: TOOLS),
           x_axis_location=None, y_axis_location=None)
_l_(685797)
_a_(685799, _n_(685798, "p", lambda: p), "grid").grid_line_color = None
_l_(685800)

_c_(685804, _a_(685802, _n_(685801, "p", lambda: p), "patches"), 'x', 'y', source=_n_(685803, "source", lambda: source),
          fill_color='color', fill_alpha=0.7,
          line_color="white", line_width=0.5)
_l_(685805)

_c_(685808, _n_(685806, "show", lambda: show), _n_(685807, "p", lambda: p))
_l_(685809)