# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(65743)

except ImportError:
    pass
_c_(65746, _a_(65745, _n_(65744, "pd", lambda: pd), "set_option"), 'display.max_rows', None)
_l_(65747)
_c_(65749, _n_(65748, "print", lambda: print), 'Original DataFrame:')
_l_(65750)
_c_(65753, _n_(65751, "print", lambda: print), _n_(65752, "student_data", lambda: student_data))
_l_(65754)
_c_(65756, _n_(65755, "print", lambda: print), '\nCast grouping as a list:')
_l_(65757)
result = _c_(65760, _a_(65759, _n_(65758, "student_data", lambda: student_data), "groupby"), ['school_code'])
_l_(65761)
_c_(65766, _n_(65762, "print", lambda: print), _c_(65765, _n_(65763, "list", lambda: list), _n_(65764, "result", lambda: result)))
_l_(65767)