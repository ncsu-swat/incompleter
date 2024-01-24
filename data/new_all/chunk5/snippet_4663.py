# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53284528/importing-file-with-constants-and-throwing-attributeerror-python-3
#Currency conversions - settings.py

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import main
    _l_(684369)

except ImportError:
    pass
try:
    import os
    _l_(684371)

except ImportError:
    pass

URL      = "https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml"
_l_(684372)
DIR      = _c_(684381, _a_(684375, _a_(684374, _n_(684373, "os", lambda: os), "path"), "dirname"), _c_(684380, _a_(684378, _a_(684377, _n_(684376, "os", lambda: os), "path"), "realpath"), _n_(684379, "__file__", lambda: __file__)))
_l_(684382)
FILE     = _c_(684387, _a_(684385, _a_(684384, _n_(684383, "os", lambda: os), "path"), "join"), _n_(684386, "DIR", lambda: DIR), 'exData.xml')
_l_(684388)

OPTIONS = {'USD' : _a_(684390, _n_(684389, "main", lambda: main), "toUSD"), 'JPY' : _a_(684392, _n_(684391, "main", lambda: main), "toJPY"), 'BGN' : _a_(684394, _n_(684393, "main", lambda: main), "toBGN"), 'CZK' : _a_(684396, _n_(684395, "main", lambda: main), "toCZK"),
           'DKK' : _a_(684398, _n_(684397, "main", lambda: main), "toDKK"), 'GBP' : _a_(684400, _n_(684399, "main", lambda: main), "toGBP"), 'HUF' : _a_(684402, _n_(684401, "main", lambda: main), "toHUF"), 'PLN' : _a_(684404, _n_(684403, "main", lambda: main), "toPLN"),
           'RON' : _a_(684406, _n_(684405, "main", lambda: main), "toRON"), 'SEK' : _a_(684408, _n_(684407, "main", lambda: main), "toSEK"), 'CHF' : _a_(684410, _n_(684409, "main", lambda: main), "toCHF"), 'ISK' : _a_(684412, _n_(684411, "main", lambda: main), "toISK"),
           'NOK' : _a_(684414, _n_(684413, "main", lambda: main), "toNOK")
}
_l_(684415)