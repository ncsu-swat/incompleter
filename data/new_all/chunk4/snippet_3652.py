# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70650986/attribute-error-while-scraping-gdelt-data
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import gdelt
    _l_(627352)

except ImportError:
    pass
gd = _c_(627355, _a_(627354, _n_(627353, "gdelt", lambda: gdelt), "gdelt"), version=1)
_l_(627356)
try:
    from statsmodels.tsa.api import VAR
    _l_(627358)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(627360)

except ImportError:
    pass
try:
    import os
    _l_(627362)

except ImportError:
    pass
_c_(627365, _a_(627364, _n_(627363, "os", lambda: os), "makedirs"), "data",exist_ok=True)
_l_(627366)
try:
    import datetime
    _l_(627368)

except ImportError:
    pass

cur_date = _c_(627371, _a_(627370, _n_(627369, "datetime", lambda: datetime), "datetime"), 2022,1,10) - _c_(627374, _a_(627373, _n_(627372, "datetime", lambda: datetime), "timedelta"), days=10)
_l_(627375)
end_date = _c_(627378, _a_(627377, _n_(627376, "datetime", lambda: datetime), "datetime"), 2022,1,10)
_l_(627379)

year     = _a_(627381, _n_(627380, "cur_date", lambda: cur_date), "year")
_l_(627382)
month    = _c_(627386, _n_(627383, "str", lambda: str), _a_(627385, _n_(627384, "cur_date", lambda: cur_date), "month"))
_l_(627387)
day      = _c_(627391, _n_(627388, "str", lambda: str), _a_(627390, _n_(627389, "cur_date", lambda: cur_date), "day"))
_l_(627392)

if _a_(627394, _n_(627393, "cur_date", lambda: cur_date), "month") < 10:
    _l_(627397)

    month = "0" + _n_(627395, "month", lambda: month)
    _l_(627396)
if _a_(627399, _n_(627398, "cur_date", lambda: cur_date), "day") < 10:
    _l_(627402)

    day = "0" + _n_(627400, "day", lambda: day)  
    _l_(627401)  

_c_(627408, _a_(627404, _n_(627403, "gd", lambda: gd), "Search"), ['%s %s %s'%(_n_(627405, "year", lambda: year), _n_(627406, "month", lambda: month), _n_(627407, "day", lambda: day))],table='gkg',coverage=True, translation=False)
_l_(627409)