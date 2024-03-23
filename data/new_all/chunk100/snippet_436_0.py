# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(44255)

except ImportError:
    pass
_c_(44257, _n_(44256, "print", lambda: print), 'Timezone: Europe/Berlin:')
_l_(44258)
_c_(44260, _n_(44259, "print", lambda: print), 'Using pytz:')
_l_(44261)
date_pytz = _c_(44264, _a_(44263, _n_(44262, "pd", lambda: pd), "Timestamp"), '2019-01-01', tz='Europe/Berlin')
_l_(44265)
_c_(44269, _n_(44266, "print", lambda: print), _a_(44268, _n_(44267, "date_pytz", lambda: date_pytz), "tz"))
_l_(44270)
_c_(44272, _n_(44271, "print", lambda: print), 'Using dateutil:')
_l_(44273)
_c_(44277, _n_(44274, "print", lambda: print), _a_(44276, _n_(44275, "date_util", lambda: date_util), "tz"))
_l_(44278)
_c_(44280, _n_(44279, "print", lambda: print), '\nUS/Pacific:')
_l_(44281)
_c_(44283, _n_(44282, "print", lambda: print), 'Using pytz:')
_l_(44284)
date_pytz = _c_(44287, _a_(44286, _n_(44285, "pd", lambda: pd), "Timestamp"), '2019-01-01', tz='US/Pacific')
_l_(44288)
_c_(44292, _n_(44289, "print", lambda: print), _a_(44291, _n_(44290, "date_pytz", lambda: date_pytz), "tz"))
_l_(44293)
_c_(44295, _n_(44294, "print", lambda: print), 'Using dateutil:')
_l_(44296)
date_util = _c_(44299, _a_(44298, _n_(44297, "pd", lambda: pd), "Timestamp"), '2019-01-01', tz='dateutil/US/Pacific')
_l_(44300)
_c_(44304, _n_(44301, "print", lambda: print), _a_(44303, _n_(44302, "date_util", lambda: date_util), "tz"))
_l_(44305)