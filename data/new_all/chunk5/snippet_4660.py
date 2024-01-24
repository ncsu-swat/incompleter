# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53308766/bokehgetting-typeerror-object-of-type-polygon-is-not-json-serializable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import shapefile
    _l_(673691)

except ImportError:
    pass
try:
    import itertools
    _l_(673693)

except ImportError:
    pass

shp = _c_(673695, _n_(673694, "open", lambda: open), "/Users/xxxx/Desktop/cb_2015_us_state_500k/cb_2015_us_state_500k.shp", "rb")
_l_(673696)
dbf = _c_(673698, _n_(673697, "open", lambda: open), "/Users/xxxx/Desktop/cb_2015_us_state_500k/cb_2015_us_state_500k.dbf", "rb")
_l_(673699)
sf = _c_(673704, _a_(673701, _n_(673700, "shapefile", lambda: shapefile), "Reader"), shp=_n_(673702, "shp", lambda: shp), dbf=_n_(673703, "dbf", lambda: dbf))
_l_(673705)

lats = []
_l_(673706)
lons = []
_l_(673707)
ct_name = []
_l_(673708)
st_id = []
_l_(673709)
ct_state_name = []
_l_(673710)
for shprec in _c_(673713, _a_(673712, _n_(673711, "sf", lambda: sf), "shapeRecords")):
    _l_(673795)

    _c_(673720, _a_(673715, _n_(673714, "st_id", lambda: st_id), "append"), _c_(673719, _n_(673716, "int", lambda: int), _a_(673718, _n_(673717, "shprec", lambda: shprec), "record")[0]))
    _l_(673721)
    _c_(673726, _a_(673723, _n_(673722, "ct_name", lambda: ct_name), "append"), _a_(673725, _n_(673724, "shprec", lambda: shprec), "record")[5])
    _l_(673727)
    _c_(673732, _a_(673729, _n_(673728, "ct_state_name", lambda: ct_state_name), "append"), _a_(673731, _n_(673730, "shprec", lambda: shprec), "record")[4])
    _l_(673733)
    lat, lon = _c_(673741, _n_(673734, "map", lambda: map), _n_(673735, "list", lambda: list), _c_(673740, _n_(673736, "zip", lambda: zip), *_a_(673739, _a_(673738, _n_(673737, "shprec", lambda: shprec), "shape"), "points")))
    _l_(673742)
    indices = _c_(673747, _a_(673746, _a_(673745, _a_(673744, _n_(673743, "shprec", lambda: shprec), "shape"), "parts"), "tolist"))
    _l_(673748)
    lat = [_n_(673749, "lat", lambda: lat)[_n_(673750, "i", lambda: i):_n_(673751, "j", lambda: j)] + [_c_(673753, _n_(673752, "float", lambda: float), 'NaN')] for i, j in _c_(673757, _n_(673754, "zip", lambda: zip), _n_(673755, "indices", lambda: indices), _n_(673756, "indices", lambda: indices)[1:]+[None])]
    _l_(673758)
    lon = [_n_(673759, "lon", lambda: lon)[_n_(673760, "i", lambda: i):_n_(673761, "j", lambda: j)] + [_c_(673763, _n_(673762, "float", lambda: float), 'NaN')] for i, j in _c_(673767, _n_(673764, "zip", lambda: zip), _n_(673765, "indices", lambda: indices), _n_(673766, "indices", lambda: indices)[1:]+[None])]
    _l_(673768)
    lat = _c_(673775, _n_(673769, "list", lambda: list), _c_(673774, _a_(673772, _a_(673771, _n_(673770, "itertools", lambda: itertools), "chain"), "from_iterable"), _n_(673773, "lat", lambda: lat)))
    _l_(673776)
    lon = _c_(673783, _n_(673777, "list", lambda: list), _c_(673782, _a_(673780, _a_(673779, _n_(673778, "itertools", lambda: itertools), "chain"), "from_iterable"), _n_(673781, "lon", lambda: lon)))
    _l_(673784)
    _c_(673788, _a_(673786, _n_(673785, "lats", lambda: lats), "append"), _n_(673787, "lat", lambda: lat))
    _l_(673789)
    _c_(673793, _a_(673791, _n_(673790, "lons", lambda: lons), "append"), _n_(673792, "lon", lambda: lon))
    _l_(673794)

map_data = _c_(673803, _a_(673797, _n_(673796, "pd", lambda: pd), "DataFrame"), {'x': _n_(673798, "lats", lambda: lats), 'y': _n_(673799, "lons", lambda: lons), 'state': _n_(673800, "st_id", lambda: st_id), 'county_name': _n_(673801, "ct_name", lambda: ct_name), 'ct_state_name': _n_(673802, "ct_state_name", lambda: ct_state_name)})
_l_(673804)
map_data_m = _n_(673805, "map_data", lambda: map_data)[_c_(673809, _a_(673808, _a_(673807, _n_(673806, "map_data", lambda: map_data), "ct_state_name"), "isin"), ['NJ'])]    
_l_(673810)    

source = _c_(673813, _n_(673811, "ColumnDataSource", lambda: ColumnDataSource), _n_(673812, "map_data_m", lambda: map_data_m))
_l_(673814)

TOOLS="pan,wheel_zoom,box_zoom,reset,hover,save"
_l_(673815)

p = _c_(673818, _n_(673816, "figure", lambda: figure), title="Title", tools=_n_(673817, "TOOLS", lambda: TOOLS),
           x_axis_location=None, y_axis_location=None)
_l_(673819)
_a_(673821, _n_(673820, "p", lambda: p), "grid").grid_line_color = None
_l_(673822)

_c_(673826, _a_(673824, _n_(673823, "p", lambda: p), "patches"), 'x', 'y', source=_n_(673825, "source", lambda: source),
          fill_color='color', fill_alpha=0.7,
          line_color="white", line_width=0.5)
_l_(673827)

_c_(673830, _n_(673828, "show", lambda: show), _n_(673829, "p", lambda: p))
_l_(673831)