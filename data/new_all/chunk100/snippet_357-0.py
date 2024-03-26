# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(111930)

except ImportError:
    pass
_c_(111932, _n_(111931, "print", lambda: print), 'First date:')
_l_(111933)
_c_(111936, _n_(111934, "print", lambda: print), _n_(111935, "newday", lambda: newday))
_l_(111937)
_c_(111939, _n_(111938, "print", lambda: print), '\nThe day name of the said date:')
_l_(111940)
_c_(111945, _n_(111941, "print", lambda: print), _c_(111944, _a_(111943, _n_(111942, "newday", lambda: newday), "day_name")))
_l_(111946)
_c_(111948, _n_(111947, "print", lambda: print), '\nAdd 2 days with the said date:')
_l_(111949)
newday1 = _n_(111950, "newday", lambda: newday) + _c_(111953, _a_(111952, _n_(111951, "pd", lambda: pd), "Timedelta"), '2 day')
_l_(111954)
_c_(111959, _n_(111955, "print", lambda: print), _c_(111958, _a_(111957, _n_(111956, "newday1", lambda: newday1), "day_name")))
_l_(111960)
_c_(111962, _n_(111961, "print", lambda: print), '\nNext business day:')
_l_(111963)
nbday = _n_(111964, "newday", lambda: newday) + _c_(111968, _a_(111967, _a_(111966, _n_(111965, "pd", lambda: pd), "offsets"), "BDay"))
_l_(111969)
_c_(111974, _n_(111970, "print", lambda: print), _c_(111973, _a_(111972, _n_(111971, "nbday", lambda: nbday), "day_name")))
_l_(111975)