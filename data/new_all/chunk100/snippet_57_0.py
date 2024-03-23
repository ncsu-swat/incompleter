# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(60206)

except ImportError:
    pass
try:
    import numpy as np
    _l_(60208)

except ImportError:
    pass
_c_(60211, _a_(60210, _n_(60209, "pd", lambda: pd), "set_option"), 'display.max_rows', None)
_l_(60212)
_c_(60214, _n_(60213, "print", lambda: print), 'Original Orders DataFrame:')
_l_(60215)
_c_(60218, _n_(60216, "print", lambda: print), _n_(60217, "df", lambda: df))
_l_(60219)
_c_(60221, _n_(60220, "print", lambda: print), '\nReplacing NaNs with the value from the previous row (purch_amt):')
_l_(60222)
_c_(60225, _a_(60224, _n_(60223, "df", lambda: df)['purch_amt'], "fillna"), method='pad', inplace=True)
_l_(60226)
_c_(60229, _n_(60227, "print", lambda: print), _n_(60228, "df", lambda: df))
_l_(60230)
_c_(60232, _n_(60231, "print", lambda: print), '\nReplacing NaNs with the value from the next row (sale_amt):')
_l_(60233)
_c_(60236, _a_(60235, _n_(60234, "df", lambda: df)['sale_amt'], "fillna"), method='bfill', inplace=True)
_l_(60237)
_c_(60240, _n_(60238, "print", lambda: print), _n_(60239, "df", lambda: df))
_l_(60241)