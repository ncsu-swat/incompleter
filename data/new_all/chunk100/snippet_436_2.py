# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(44359)

except ImportError:
    pass
_c_(44361, _n_(44360, "print", lambda: print), 'Timezone: Europe/Berlin:')
_l_(44362)
_c_(44364, _n_(44363, "print", lambda: print), 'Using pytz:')
_l_(44365)
_c_(44369, _n_(44366, "print", lambda: print), _a_(44368, _n_(44367, "date_pytz", lambda: date_pytz), "tz"))
_l_(44370)
_c_(44372, _n_(44371, "print", lambda: print), 'Using dateutil:')
_l_(44373)
date_util = _c_(44376, _a_(44375, _n_(44374, "pd", lambda: pd), "Timestamp"), '2019-01-01', tz='dateutil/Europe/Berlin')
_l_(44377)
_c_(44381, _n_(44378, "print", lambda: print), _a_(44380, _n_(44379, "date_util", lambda: date_util), "tz"))
_l_(44382)
_c_(44384, _n_(44383, "print", lambda: print), '\nUS/Pacific:')
_l_(44385)
_c_(44387, _n_(44386, "print", lambda: print), 'Using pytz:')
_l_(44388)
date_pytz = _c_(44391, _a_(44390, _n_(44389, "pd", lambda: pd), "Timestamp"), '2019-01-01', tz='US/Pacific')
_l_(44392)
_c_(44396, _n_(44393, "print", lambda: print), _a_(44395, _n_(44394, "date_pytz", lambda: date_pytz), "tz"))
_l_(44397)
_c_(44399, _n_(44398, "print", lambda: print), 'Using dateutil:')
_l_(44400)
date_util = _c_(44403, _a_(44402, _n_(44401, "pd", lambda: pd), "Timestamp"), '2019-01-01', tz='dateutil/US/Pacific')
_l_(44404)
_c_(44408, _n_(44405, "print", lambda: print), _a_(44407, _n_(44406, "date_util", lambda: date_util), "tz"))
_l_(44409)