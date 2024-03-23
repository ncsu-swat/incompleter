# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(97244)

except ImportError:
    pass
epoch_t = 1621132355
_l_(97245)
_c_(97247, _n_(97246, "print", lambda: print), 'Regular time stamp in UTC:')
_l_(97248)
_c_(97251, _n_(97249, "print", lambda: print), _n_(97250, "time_stamp", lambda: time_stamp))
_l_(97252)
_c_(97254, _n_(97253, "print", lambda: print), '\nConvert the said timestamp in to US/Pacific:')
_l_(97255)
_c_(97262, _n_(97256, "print", lambda: print), _c_(97261, _a_(97260, _c_(97259, _a_(97258, _n_(97257, "time_stamp", lambda: time_stamp), "tz_localize"), 'UTC'), "tz_convert"), 'US/Pacific'))
_l_(97263)
_c_(97265, _n_(97264, "print", lambda: print), '\nConvert the said timestamp in to Europe/Berlin:')
_l_(97266)
_c_(97273, _n_(97267, "print", lambda: print), _c_(97272, _a_(97271, _c_(97270, _a_(97269, _n_(97268, "time_stamp", lambda: time_stamp), "tz_localize"), 'UTC'), "tz_convert"), 'Europe/Berlin'))
_l_(97274)