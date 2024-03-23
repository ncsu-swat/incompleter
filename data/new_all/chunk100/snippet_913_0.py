# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(92108)

except ImportError:
    pass
try:
    import numpy as np
    _l_(92110)

except ImportError:
    pass
sales_arrays = [['sale1', 'sale1', 'sale2', 'sale2', 'sale3', 'sale3', 'sale4', 'sale4'], ['city1', 'city2', 'city1', 'city2', 'city1', 'city2', 'city1', 'city2']]
_l_(92111)
sales_tuples = _c_(92116, _n_(92112, "list", lambda: list), _c_(92115, _n_(92113, "zip", lambda: zip), *_n_(92114, "sales_arrays", lambda: sales_arrays)))
_l_(92117)
sales_index = _c_(92122, _a_(92120, _a_(92119, _n_(92118, "pd", lambda: pd), "MultiIndex"), "from_tuples"), _n_(92121, "sales_tuples", lambda: sales_tuples), names=['sale', 'city'])
_l_(92123)
_c_(92126, _n_(92124, "print", lambda: print), _n_(92125, "sales_tuples", lambda: sales_tuples))
_l_(92127)
_c_(92129, _n_(92128, "print", lambda: print), '\nConstruct a Dataframe using the said MultiIndex levels: ')
_l_(92130)
_c_(92133, _n_(92131, "print", lambda: print), _n_(92132, "df", lambda: df))
_l_(92134)
_c_(92136, _n_(92135, "print", lambda: print), '\nRename the columns name of the said dataframe')
_l_(92137)
df1 = _c_(92140, _a_(92139, _n_(92138, "df", lambda: df), "rename"), columns={0: 'col1', 1: 'col2', 2: 'col3', 3: 'col4', 4: 'col5'})
_l_(92141)
_c_(92144, _n_(92142, "print", lambda: print), _n_(92143, "df1", lambda: df1))
_l_(92145)
_c_(92147, _n_(92146, "print", lambda: print), '\nRename specific labels of the main index of the DataFrame')
_l_(92148)
df2 = _c_(92151, _a_(92150, _n_(92149, "df1", lambda: df1), "rename"), index={'sale2': 'S2', 'city2': 'C2'})
_l_(92152)
_c_(92155, _n_(92153, "print", lambda: print), _n_(92154, "df2", lambda: df2))
_l_(92156)