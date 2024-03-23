# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(39245)

except ImportError:
    pass
try:
    from pandas.tseries.offsets import *
    _l_(39247)

except ImportError:
    pass
try:
    import datetime
    _l_(39249)

except ImportError:
    pass
try:
    from datetime import datetime, date
    _l_(39251)

except ImportError:
    pass
dt = _c_(39253, _n_(39252, "datetime", lambda: datetime), 2020, 1, 4)
_l_(39254)
_c_(39256, _n_(39255, "print", lambda: print), 'Specified date:')
_l_(39257)
_c_(39260, _n_(39258, "print", lambda: print), _n_(39259, "dt", lambda: dt))
_l_(39261)
_c_(39263, _n_(39262, "print", lambda: print), '\nOne business day from the said date:')
_l_(39264)
obday = _n_(39265, "dt", lambda: dt) + _c_(39267, _n_(39266, "BusinessDay", lambda: BusinessDay))
_l_(39268)
_c_(39271, _n_(39269, "print", lambda: print), _n_(39270, "obday", lambda: obday))
_l_(39272)
_c_(39274, _n_(39273, "print", lambda: print), '\nTwo business days from the said date:')
_l_(39275)
tbday = _n_(39276, "dt", lambda: dt) + 2 * _c_(39278, _n_(39277, "BusinessDay", lambda: BusinessDay))
_l_(39279)
_c_(39282, _n_(39280, "print", lambda: print), _n_(39281, "tbday", lambda: tbday))
_l_(39283)
_c_(39285, _n_(39284, "print", lambda: print), '\nThree business days from the said date:')
_l_(39286)
thbday = _n_(39287, "dt", lambda: dt) + 3 * _c_(39289, _n_(39288, "BusinessDay", lambda: BusinessDay))
_l_(39290)
_c_(39293, _n_(39291, "print", lambda: print), _n_(39292, "thbday", lambda: thbday))
_l_(39294)
_c_(39296, _n_(39295, "print", lambda: print), '\nNext business month end from the said date:')
_l_(39297)
_c_(39300, _n_(39298, "print", lambda: print), _n_(39299, "nbday", lambda: nbday))
_l_(39301)