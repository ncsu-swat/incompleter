# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(92211)

except ImportError:
    pass
try:
    import numpy as np
    _l_(92213)

except ImportError:
    pass
sales_tuples = _c_(92218, _n_(92214, "list", lambda: list), _c_(92217, _n_(92215, "zip", lambda: zip), *_n_(92216, "sales_arrays", lambda: sales_arrays)))
_l_(92219)
sales_index = _c_(92224, _a_(92222, _a_(92221, _n_(92220, "pd", lambda: pd), "MultiIndex"), "from_tuples"), _n_(92223, "sales_tuples", lambda: sales_tuples), names=['sale', 'city'])
_l_(92225)
_c_(92228, _n_(92226, "print", lambda: print), _n_(92227, "sales_tuples", lambda: sales_tuples))
_l_(92229)
_c_(92231, _n_(92230, "print", lambda: print), '\nConstruct a Dataframe using the said MultiIndex levels: ')
_l_(92232)
df = _c_(92240, _a_(92234, _n_(92233, "pd", lambda: pd), "DataFrame"), _c_(92238, _a_(92237, _a_(92236, _n_(92235, "np", lambda: np), "random"), "randn"), 8, 5), index=_n_(92239, "sales_index", lambda: sales_index))
_l_(92241)
_c_(92244, _n_(92242, "print", lambda: print), _n_(92243, "df", lambda: df))
_l_(92245)
_c_(92247, _n_(92246, "print", lambda: print), '\nRename the columns name of the said dataframe')
_l_(92248)
df1 = _c_(92251, _a_(92250, _n_(92249, "df", lambda: df), "rename"), columns={0: 'col1', 1: 'col2', 2: 'col3', 3: 'col4', 4: 'col5'})
_l_(92252)
_c_(92255, _n_(92253, "print", lambda: print), _n_(92254, "df1", lambda: df1))
_l_(92256)
_c_(92258, _n_(92257, "print", lambda: print), '\nRename specific labels of the main index of the DataFrame')
_l_(92259)
df2 = _c_(92262, _a_(92261, _n_(92260, "df1", lambda: df1), "rename"), index={'sale2': 'S2', 'city2': 'C2'})
_l_(92263)
_c_(92266, _n_(92264, "print", lambda: print), _n_(92265, "df2", lambda: df2))
_l_(92267)