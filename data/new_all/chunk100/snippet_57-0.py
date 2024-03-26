# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(119264)

except ImportError:
    pass
try:
    import numpy as np
    _l_(119266)

except ImportError:
    pass
_c_(119269, _a_(119268, _n_(119267, "pd", lambda: pd), "set_option"), 'display.max_rows', None)
_l_(119270)
_c_(119272, _n_(119271, "print", lambda: print), 'Original Orders DataFrame:')
_l_(119273)
_c_(119276, _n_(119274, "print", lambda: print), _n_(119275, "df", lambda: df))
_l_(119277)
_c_(119279, _n_(119278, "print", lambda: print), '\nReplacing NaNs with the value from the previous row (purch_amt):')
_l_(119280)
_c_(119283, _a_(119282, _n_(119281, "df", lambda: df)['purch_amt'], "fillna"), method='pad', inplace=True)
_l_(119284)
_c_(119287, _n_(119285, "print", lambda: print), _n_(119286, "df", lambda: df))
_l_(119288)
_c_(119290, _n_(119289, "print", lambda: print), '\nReplacing NaNs with the value from the next row (sale_amt):')
_l_(119291)
_c_(119294, _a_(119293, _n_(119292, "df", lambda: df)['sale_amt'], "fillna"), method='bfill', inplace=True)
_l_(119295)
_c_(119298, _n_(119296, "print", lambda: print), _n_(119297, "df", lambda: df))
_l_(119299)