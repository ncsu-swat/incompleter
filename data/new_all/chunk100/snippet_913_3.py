# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(92269)

except ImportError:
    pass
try:
    import numpy as np
    _l_(92271)

except ImportError:
    pass
sales_arrays = [['sale1', 'sale1', 'sale2', 'sale2', 'sale3', 'sale3', 'sale4', 'sale4'], ['city1', 'city2', 'city1', 'city2', 'city1', 'city2', 'city1', 'city2']]
_l_(92272)
sales_index = _c_(92277, _a_(92275, _a_(92274, _n_(92273, "pd", lambda: pd), "MultiIndex"), "from_tuples"), _n_(92276, "sales_tuples", lambda: sales_tuples), names=['sale', 'city'])
_l_(92278)
_c_(92281, _n_(92279, "print", lambda: print), _n_(92280, "sales_tuples", lambda: sales_tuples))
_l_(92282)
_c_(92284, _n_(92283, "print", lambda: print), '\nConstruct a Dataframe using the said MultiIndex levels: ')
_l_(92285)
df = _c_(92293, _a_(92287, _n_(92286, "pd", lambda: pd), "DataFrame"), _c_(92291, _a_(92290, _a_(92289, _n_(92288, "np", lambda: np), "random"), "randn"), 8, 5), index=_n_(92292, "sales_index", lambda: sales_index))
_l_(92294)
_c_(92297, _n_(92295, "print", lambda: print), _n_(92296, "df", lambda: df))
_l_(92298)
_c_(92300, _n_(92299, "print", lambda: print), '\nRename the columns name of the said dataframe')
_l_(92301)
df1 = _c_(92304, _a_(92303, _n_(92302, "df", lambda: df), "rename"), columns={0: 'col1', 1: 'col2', 2: 'col3', 3: 'col4', 4: 'col5'})
_l_(92305)
_c_(92308, _n_(92306, "print", lambda: print), _n_(92307, "df1", lambda: df1))
_l_(92309)
_c_(92311, _n_(92310, "print", lambda: print), '\nRename specific labels of the main index of the DataFrame')
_l_(92312)
df2 = _c_(92315, _a_(92314, _n_(92313, "df1", lambda: df1), "rename"), index={'sale2': 'S2', 'city2': 'C2'})
_l_(92316)
_c_(92319, _n_(92317, "print", lambda: print), _n_(92318, "df2", lambda: df2))
_l_(92320)