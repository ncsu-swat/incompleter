# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(115256)

except ImportError:
    pass
try:
    import numpy as np
    _l_(115258)

except ImportError:
    pass
_c_(115261, _a_(115260, _n_(115259, "pd", lambda: pd), "set_option"), 'display.max_rows', None)
_l_(115262)
df = _c_(115299, _a_(115264, _n_(115263, "pd", lambda: pd), "DataFrame"), {'ord_no': [_a_(115266, _n_(115265, "np", lambda: np), "nan"), _a_(115268, _n_(115267, "np", lambda: np), "nan"), 70002, _a_(115270, _n_(115269, "np", lambda: np), "nan"), _a_(115272, _n_(115271, "np", lambda: np), "nan"), 70005, _a_(115274, _n_(115273, "np", lambda: np), "nan"), 70010, 70003, 70012, _a_(115276, _n_(115275, "np", lambda: np), "nan"), _a_(115278, _n_(115277, "np", lambda: np), "nan")], 'purch_amt': [_a_(115280, _n_(115279, "np", lambda: np), "nan"), 270.65, 65.26, _a_(115282, _n_(115281, "np", lambda: np), "nan"), 948.5, 2400.6, 5760, 1983.43, 2480.4, 250.45, 75.29, _a_(115284, _n_(115283, "np", lambda: np), "nan")], 'ord_date': [_a_(115286, _n_(115285, "np", lambda: np), "nan"), '2012-09-10', _a_(115288, _n_(115287, "np", lambda: np), "nan"), _a_(115290, _n_(115289, "np", lambda: np), "nan"), '2012-09-10', '2012-07-27', '2012-09-10', '2012-10-10', '2012-10-10', '2012-06-27', '2012-08-17', _a_(115292, _n_(115291, "np", lambda: np), "nan")], 'customer_id': [_a_(115294, _n_(115293, "np", lambda: np), "nan"), 3001, 3001, _a_(115296, _n_(115295, "np", lambda: np), "nan"), 3002, 3001, 3001, 3004, 3003, 3002, 3001, _a_(115298, _n_(115297, "np", lambda: np), "nan")]})
_l_(115300)
_c_(115302, _n_(115301, "print", lambda: print), 'Original Orders DataFrame:')
_l_(115303)
_c_(115306, _n_(115304, "print", lambda: print), _n_(115305, "df", lambda: df))
_l_(115307)
_c_(115309, _n_(115308, "print", lambda: print), '\nTotal number of missing values of the said DataFrame:')
_l_(115310)
_c_(115313, _n_(115311, "print", lambda: print), _n_(115312, "result", lambda: result))
_l_(115314)