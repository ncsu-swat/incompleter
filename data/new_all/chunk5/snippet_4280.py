# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60345611/dont-understand-cause-of-this-typeerror-exception
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import json
    _l_(647474)

except ImportError:
    pass
try:
    import pygal
    _l_(647476)

except ImportError:
    pass
try:
    from pygal.style import LightColorizedStyle as LCS,RotateStyle as RC
    _l_(647478)

except ImportError:
    pass
try:
    from pygal.maps.world import World
    _l_(647480)

except ImportError:
    pass
try:
    from country_codes import get_country_code
    _l_(647482)

except ImportError:
    pass
#load data into a list
filename = 'gdp.json'
_l_(647483)
with _c_(647486, _n_(647484, "open", lambda: open), _n_(647485, "filename", lambda: filename)) as f:
    _l_(647492)

    gdp_data = _c_(647490, _a_(647488, _n_(647487, "json", lambda: json), "load"), _n_(647489, "f", lambda: f))
    _l_(647491)