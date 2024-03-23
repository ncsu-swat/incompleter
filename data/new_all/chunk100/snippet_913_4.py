# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(92322)

except ImportError:
    pass
try:
    import numpy as np
    _l_(92324)

except ImportError:
    pass
sales_arrays = [['sale1', 'sale1', 'sale2', 'sale2', 'sale3', 'sale3', 'sale4', 'sale4'], ['city1', 'city2', 'city1', 'city2', 'city1', 'city2', 'city1', 'city2']]
_l_(92325)
sales_tuples = _c_(92330, _n_(92326, "list", lambda: list), _c_(92329, _n_(92327, "zip", lambda: zip), *_n_(92328, "sales_arrays", lambda: sales_arrays)))
_l_(92331)
sales_index = _c_(92336, _a_(92334, _a_(92333, _n_(92332, "pd", lambda: pd), "MultiIndex"), "from_tuples"), _n_(92335, "sales_tuples", lambda: sales_tuples), names=['sale', 'city'])
_l_(92337)
_c_(92340, _n_(92338, "print", lambda: print), _n_(92339, "sales_tuples", lambda: sales_tuples))
_l_(92341)
_c_(92343, _n_(92342, "print", lambda: print), '\nConstruct a Dataframe using the said MultiIndex levels: ')
_l_(92344)
df = _c_(92352, _a_(92346, _n_(92345, "pd", lambda: pd), "DataFrame"), _c_(92350, _a_(92349, _a_(92348, _n_(92347, "np", lambda: np), "random"), "randn"), 8, 5), index=_n_(92351, "sales_index", lambda: sales_index))
_l_(92353)
_c_(92356, _n_(92354, "print", lambda: print), _n_(92355, "df", lambda: df))
_l_(92357)
_c_(92359, _n_(92358, "print", lambda: print), '\nRename the columns name of the said dataframe')
_l_(92360)
df1 = _c_(92363, _a_(92362, _n_(92361, "df", lambda: df), "rename"), columns={0: 'col1', 1: 'col2', 2: 'col3', 3: 'col4', 4: 'col5'})
_l_(92364)
_c_(92367, _n_(92365, "print", lambda: print), _n_(92366, "df1", lambda: df1))
_l_(92368)
_c_(92370, _n_(92369, "print", lambda: print), '\nRename specific labels of the main index of the DataFrame')
_l_(92371)
_c_(92374, _n_(92372, "print", lambda: print), _n_(92373, "df2", lambda: df2))
_l_(92375)