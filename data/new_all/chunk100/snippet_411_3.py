# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(40359)

except ImportError:
    pass
try:
    import numpy as np
    _l_(40361)

except ImportError:
    pass
sales_tuples = _c_(40366, _n_(40362, "list", lambda: list), _c_(40365, _n_(40363, "zip", lambda: zip), *_n_(40364, "sales_arrays", lambda: sales_arrays)))
_l_(40367)
sales_index = _c_(40372, _a_(40370, _a_(40369, _n_(40368, "pd", lambda: pd), "MultiIndex"), "from_tuples"), _n_(40371, "sales_tuples", lambda: sales_tuples), names=['sale', 'city'])
_l_(40373)
_c_(40376, _n_(40374, "print", lambda: print), _n_(40375, "sales_tuples", lambda: sales_tuples))
_l_(40377)
_c_(40379, _n_(40378, "print", lambda: print), '\nConstruct a Dataframe using the said MultiIndex levels: ')
_l_(40380)
df = _c_(40388, _a_(40382, _n_(40381, "pd", lambda: pd), "DataFrame"), _c_(40386, _a_(40385, _a_(40384, _n_(40383, "np", lambda: np), "random"), "randn"), 8, 5), index=_n_(40387, "sales_index", lambda: sales_index))
_l_(40389)
_c_(40392, _n_(40390, "print", lambda: print), _n_(40391, "df", lambda: df))
_l_(40393)
_c_(40395, _n_(40394, "print", lambda: print), '\nExtract a single row from the said dataframe:')
_l_(40396)
_c_(40400, _n_(40397, "print", lambda: print), _a_(40399, _n_(40398, "df", lambda: df), "loc")['sale2', 'city2'])
_l_(40401)
_c_(40403, _n_(40402, "print", lambda: print), '\nExtract a single row from the said dataframe:')
_l_(40404)
_c_(40408, _n_(40405, "print", lambda: print), _a_(40407, _n_(40406, "df", lambda: df), "loc")['sale2', 'city2'])
_l_(40409)
_c_(40411, _n_(40410, "print", lambda: print), '\nExtract number of rows from the said dataframe:')
_l_(40412)
_c_(40416, _n_(40413, "print", lambda: print), _a_(40415, _n_(40414, "df", lambda: df), "loc")['sale1'])
_l_(40417)
_c_(40419, _n_(40418, "print", lambda: print), '\nExtract number of rows from the said dataframe:')
_l_(40420)
_c_(40424, _n_(40421, "print", lambda: print), _a_(40423, _n_(40422, "df", lambda: df), "loc")['sale3'])
_l_(40425)
_c_(40427, _n_(40426, "print", lambda: print), '\nExtract a single value from the said dataframe:')
_l_(40428)
_c_(40432, _n_(40429, "print", lambda: print), _a_(40431, _n_(40430, "df", lambda: df), "loc")[('sale1', 'city2'), 1])
_l_(40433)
_c_(40435, _n_(40434, "print", lambda: print), '\nExtract a single value from the said dataframe:')
_l_(40436)
_c_(40440, _n_(40437, "print", lambda: print), _a_(40439, _n_(40438, "df", lambda: df), "loc")[('sale4', 'city1'), 4])
_l_(40441)