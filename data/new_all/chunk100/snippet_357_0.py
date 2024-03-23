# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(35319)

except ImportError:
    pass
_c_(35321, _n_(35320, "print", lambda: print), 'First date:')
_l_(35322)
_c_(35325, _n_(35323, "print", lambda: print), _n_(35324, "newday", lambda: newday))
_l_(35326)
_c_(35328, _n_(35327, "print", lambda: print), '\nThe day name of the said date:')
_l_(35329)
_c_(35334, _n_(35330, "print", lambda: print), _c_(35333, _a_(35332, _n_(35331, "newday", lambda: newday), "day_name")))
_l_(35335)
_c_(35337, _n_(35336, "print", lambda: print), '\nAdd 2 days with the said date:')
_l_(35338)
newday1 = _n_(35339, "newday", lambda: newday) + _c_(35342, _a_(35341, _n_(35340, "pd", lambda: pd), "Timedelta"), '2 day')
_l_(35343)
_c_(35348, _n_(35344, "print", lambda: print), _c_(35347, _a_(35346, _n_(35345, "newday1", lambda: newday1), "day_name")))
_l_(35349)
_c_(35351, _n_(35350, "print", lambda: print), '\nNext business day:')
_l_(35352)
nbday = _n_(35353, "newday", lambda: newday) + _c_(35357, _a_(35356, _a_(35355, _n_(35354, "pd", lambda: pd), "offsets"), "BDay"))
_l_(35358)
_c_(35363, _n_(35359, "print", lambda: print), _c_(35362, _a_(35361, _n_(35360, "nbday", lambda: nbday), "day_name")))
_l_(35364)