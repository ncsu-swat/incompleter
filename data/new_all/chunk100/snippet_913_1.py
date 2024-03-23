# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(92158)

except ImportError:
    pass
try:
    import numpy as np
    _l_(92160)

except ImportError:
    pass
sales_arrays = [['sale1', 'sale1', 'sale2', 'sale2', 'sale3', 'sale3', 'sale4', 'sale4'], ['city1', 'city2', 'city1', 'city2', 'city1', 'city2', 'city1', 'city2']]
_l_(92161)
sales_tuples = _c_(92166, _n_(92162, "list", lambda: list), _c_(92165, _n_(92163, "zip", lambda: zip), *_n_(92164, "sales_arrays", lambda: sales_arrays)))
_l_(92167)
_c_(92170, _n_(92168, "print", lambda: print), _n_(92169, "sales_tuples", lambda: sales_tuples))
_l_(92171)
_c_(92173, _n_(92172, "print", lambda: print), '\nConstruct a Dataframe using the said MultiIndex levels: ')
_l_(92174)
df = _c_(92182, _a_(92176, _n_(92175, "pd", lambda: pd), "DataFrame"), _c_(92180, _a_(92179, _a_(92178, _n_(92177, "np", lambda: np), "random"), "randn"), 8, 5), index=_n_(92181, "sales_index", lambda: sales_index))
_l_(92183)
_c_(92186, _n_(92184, "print", lambda: print), _n_(92185, "df", lambda: df))
_l_(92187)
_c_(92189, _n_(92188, "print", lambda: print), '\nRename the columns name of the said dataframe')
_l_(92190)
df1 = _c_(92193, _a_(92192, _n_(92191, "df", lambda: df), "rename"), columns={0: 'col1', 1: 'col2', 2: 'col3', 3: 'col4', 4: 'col5'})
_l_(92194)
_c_(92197, _n_(92195, "print", lambda: print), _n_(92196, "df1", lambda: df1))
_l_(92198)
_c_(92200, _n_(92199, "print", lambda: print), '\nRename specific labels of the main index of the DataFrame')
_l_(92201)
df2 = _c_(92204, _a_(92203, _n_(92202, "df1", lambda: df1), "rename"), index={'sale2': 'S2', 'city2': 'C2'})
_l_(92205)
_c_(92208, _n_(92206, "print", lambda: print), _n_(92207, "df2", lambda: df2))
_l_(92209)