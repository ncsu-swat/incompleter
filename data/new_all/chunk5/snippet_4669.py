# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53284528/importing-file-with-constants-and-throwing-attributeerror-python-3
#Currency conversions - settings.py

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import main
    _l_(699530)

except ImportError:
    pass
try:
    import os
    _l_(699532)

except ImportError:
    pass

URL      = "https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml"
_l_(699533)
DIR      = _c_(699542, _a_(699536, _a_(699535, _n_(699534, "os", lambda: os), "path"), "dirname"), _c_(699541, _a_(699539, _a_(699538, _n_(699537, "os", lambda: os), "path"), "realpath"), _n_(699540, "__file__", lambda: __file__)))
_l_(699543)
FILE     = _c_(699548, _a_(699546, _a_(699545, _n_(699544, "os", lambda: os), "path"), "join"), _n_(699547, "DIR", lambda: DIR), 'exData.xml')
_l_(699549)

OPTIONS = {'USD' : _a_(699551, _n_(699550, "main", lambda: main), "toUSD"), 'JPY' : _a_(699553, _n_(699552, "main", lambda: main), "toJPY"), 'BGN' : _a_(699555, _n_(699554, "main", lambda: main), "toBGN"), 'CZK' : _a_(699557, _n_(699556, "main", lambda: main), "toCZK"),
           'DKK' : _a_(699559, _n_(699558, "main", lambda: main), "toDKK"), 'GBP' : _a_(699561, _n_(699560, "main", lambda: main), "toGBP"), 'HUF' : _a_(699563, _n_(699562, "main", lambda: main), "toHUF"), 'PLN' : _a_(699565, _n_(699564, "main", lambda: main), "toPLN"),
           'RON' : _a_(699567, _n_(699566, "main", lambda: main), "toRON"), 'SEK' : _a_(699569, _n_(699568, "main", lambda: main), "toSEK"), 'CHF' : _a_(699571, _n_(699570, "main", lambda: main), "toCHF"), 'ISK' : _a_(699573, _n_(699572, "main", lambda: main), "toISK"),
           'NOK' : _a_(699575, _n_(699574, "main", lambda: main), "toNOK")
}
_l_(699576)