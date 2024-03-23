# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(44411)

except ImportError:
    pass
_c_(44413, _n_(44412, "print", lambda: print), 'Timezone: Europe/Berlin:')
_l_(44414)
_c_(44416, _n_(44415, "print", lambda: print), 'Using pytz:')
_l_(44417)
date_pytz = _c_(44420, _a_(44419, _n_(44418, "pd", lambda: pd), "Timestamp"), '2019-01-01', tz='Europe/Berlin')
_l_(44421)
_c_(44425, _n_(44422, "print", lambda: print), _a_(44424, _n_(44423, "date_pytz", lambda: date_pytz), "tz"))
_l_(44426)
_c_(44428, _n_(44427, "print", lambda: print), 'Using dateutil:')
_l_(44429)
date_util = _c_(44432, _a_(44431, _n_(44430, "pd", lambda: pd), "Timestamp"), '2019-01-01', tz='dateutil/Europe/Berlin')
_l_(44433)
_c_(44437, _n_(44434, "print", lambda: print), _a_(44436, _n_(44435, "date_util", lambda: date_util), "tz"))
_l_(44438)
_c_(44440, _n_(44439, "print", lambda: print), '\nUS/Pacific:')
_l_(44441)
_c_(44443, _n_(44442, "print", lambda: print), 'Using pytz:')
_l_(44444)
date_pytz = _c_(44447, _a_(44446, _n_(44445, "pd", lambda: pd), "Timestamp"), '2019-01-01', tz='US/Pacific')
_l_(44448)
_c_(44452, _n_(44449, "print", lambda: print), _a_(44451, _n_(44450, "date_pytz", lambda: date_pytz), "tz"))
_l_(44453)
_c_(44455, _n_(44454, "print", lambda: print), 'Using dateutil:')
_l_(44456)
_c_(44460, _n_(44457, "print", lambda: print), _a_(44459, _n_(44458, "date_util", lambda: date_util), "tz"))
_l_(44461)