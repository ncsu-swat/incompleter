# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54435328/numpy-typeerror-could-not-be-cast-from-dtypem8us-to-dtypem8d
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(381007)

except ImportError:
    pass
try:
    import pandas_market_calendars as mcal
    _l_(381009)

except ImportError:
    pass
try:
    from datetime import datetime
    _l_(381011)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(381013)

except ImportError:
    pass

nyse = _c_(381016, _a_(381015, _n_(381014, "mcal", lambda: mcal), "get_calendar"), 'NYSE')
_l_(381017)
holidays = _c_(381020, _a_(381019, _n_(381018, "nyse", lambda: nyse), "holidays"))
_l_(381021)
holidays = _c_(381025, _n_(381022, "list", lambda: list), _a_(381024, _n_(381023, "holidays", lambda: holidays), "holidays")) # NYSE Holidays
_l_(381026) # NYSE Holidays

today = _c_(381029, _a_(381028, _n_(381027, "datetime", lambda: datetime), "now"))
_l_(381030)
expiration = _c_(381032, _n_(381031, "datetime", lambda: datetime), 2019,2,13,0,0)
_l_(381033)

days_to_expiration = _c_(381039, _a_(381035, _n_(381034, "np", lambda: np), "busday_count"), _n_(381036, "today", lambda: today),_n_(381037, "expiration", lambda: expiration),holidays=_n_(381038, "holidays", lambda: holidays))
_l_(381040)
_c_(381043, _n_(381041, "print", lambda: print), _n_(381042, "days_to_expiration", lambda: days_to_expiration))
_l_(381044)