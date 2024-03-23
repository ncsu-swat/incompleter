# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(40280)

except ImportError:
    pass
try:
    import numpy as np
    _l_(40282)

except ImportError:
    pass
sales_arrays = [['sale1', 'sale1', 'sale2', 'sale2', 'sale3', 'sale3', 'sale4', 'sale4'], ['city1', 'city2', 'city1', 'city2', 'city1', 'city2', 'city1', 'city2']]
_l_(40283)
sales_tuples = _c_(40288, _n_(40284, "list", lambda: list), _c_(40287, _n_(40285, "zip", lambda: zip), *_n_(40286, "sales_arrays", lambda: sales_arrays)))
_l_(40289)
_c_(40292, _n_(40290, "print", lambda: print), _n_(40291, "sales_tuples", lambda: sales_tuples))
_l_(40293)
_c_(40295, _n_(40294, "print", lambda: print), '\nConstruct a Dataframe using the said MultiIndex levels: ')
_l_(40296)
df = _c_(40304, _a_(40298, _n_(40297, "pd", lambda: pd), "DataFrame"), _c_(40302, _a_(40301, _a_(40300, _n_(40299, "np", lambda: np), "random"), "randn"), 8, 5), index=_n_(40303, "sales_index", lambda: sales_index))
_l_(40305)
_c_(40308, _n_(40306, "print", lambda: print), _n_(40307, "df", lambda: df))
_l_(40309)
_c_(40311, _n_(40310, "print", lambda: print), '\nExtract a single row from the said dataframe:')
_l_(40312)
_c_(40316, _n_(40313, "print", lambda: print), _a_(40315, _n_(40314, "df", lambda: df), "loc")['sale2', 'city2'])
_l_(40317)
_c_(40319, _n_(40318, "print", lambda: print), '\nExtract a single row from the said dataframe:')
_l_(40320)
_c_(40324, _n_(40321, "print", lambda: print), _a_(40323, _n_(40322, "df", lambda: df), "loc")['sale2', 'city2'])
_l_(40325)
_c_(40327, _n_(40326, "print", lambda: print), '\nExtract number of rows from the said dataframe:')
_l_(40328)
_c_(40332, _n_(40329, "print", lambda: print), _a_(40331, _n_(40330, "df", lambda: df), "loc")['sale1'])
_l_(40333)
_c_(40335, _n_(40334, "print", lambda: print), '\nExtract number of rows from the said dataframe:')
_l_(40336)
_c_(40340, _n_(40337, "print", lambda: print), _a_(40339, _n_(40338, "df", lambda: df), "loc")['sale3'])
_l_(40341)
_c_(40343, _n_(40342, "print", lambda: print), '\nExtract a single value from the said dataframe:')
_l_(40344)
_c_(40348, _n_(40345, "print", lambda: print), _a_(40347, _n_(40346, "df", lambda: df), "loc")[('sale1', 'city2'), 1])
_l_(40349)
_c_(40351, _n_(40350, "print", lambda: print), '\nExtract a single value from the said dataframe:')
_l_(40352)
_c_(40356, _n_(40353, "print", lambda: print), _a_(40355, _n_(40354, "df", lambda: df), "loc")[('sale4', 'city1'), 4])
_l_(40357)