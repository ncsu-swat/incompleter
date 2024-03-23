# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(44307)

except ImportError:
    pass
_c_(44309, _n_(44308, "print", lambda: print), 'Timezone: Europe/Berlin:')
_l_(44310)
_c_(44312, _n_(44311, "print", lambda: print), 'Using pytz:')
_l_(44313)
date_pytz = _c_(44316, _a_(44315, _n_(44314, "pd", lambda: pd), "Timestamp"), '2019-01-01', tz='Europe/Berlin')
_l_(44317)
_c_(44321, _n_(44318, "print", lambda: print), _a_(44320, _n_(44319, "date_pytz", lambda: date_pytz), "tz"))
_l_(44322)
_c_(44324, _n_(44323, "print", lambda: print), 'Using dateutil:')
_l_(44325)
date_util = _c_(44328, _a_(44327, _n_(44326, "pd", lambda: pd), "Timestamp"), '2019-01-01', tz='dateutil/Europe/Berlin')
_l_(44329)
_c_(44333, _n_(44330, "print", lambda: print), _a_(44332, _n_(44331, "date_util", lambda: date_util), "tz"))
_l_(44334)
_c_(44336, _n_(44335, "print", lambda: print), '\nUS/Pacific:')
_l_(44337)
_c_(44339, _n_(44338, "print", lambda: print), 'Using pytz:')
_l_(44340)
_c_(44344, _n_(44341, "print", lambda: print), _a_(44343, _n_(44342, "date_pytz", lambda: date_pytz), "tz"))
_l_(44345)
_c_(44347, _n_(44346, "print", lambda: print), 'Using dateutil:')
_l_(44348)
date_util = _c_(44351, _a_(44350, _n_(44349, "pd", lambda: pd), "Timestamp"), '2019-01-01', tz='dateutil/US/Pacific')
_l_(44352)
_c_(44356, _n_(44353, "print", lambda: print), _a_(44355, _n_(44354, "date_util", lambda: date_util), "tz"))
_l_(44357)