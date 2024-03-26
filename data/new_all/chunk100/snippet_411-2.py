# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(115093)

except ImportError:
    pass
try:
    import numpy as np
    _l_(115095)

except ImportError:
    pass
sales_tuples = _c_(115100, _n_(115096, "list", lambda: list), _c_(115099, _n_(115097, "zip", lambda: zip), *_n_(115098, "sales_arrays", lambda: sales_arrays)))
_l_(115101)
sales_index = _c_(115106, _a_(115104, _a_(115103, _n_(115102, "pd", lambda: pd), "MultiIndex"), "from_tuples"), _n_(115105, "sales_tuples", lambda: sales_tuples), names=['sale', 'city'])
_l_(115107)
_c_(115110, _n_(115108, "print", lambda: print), _n_(115109, "sales_tuples", lambda: sales_tuples))
_l_(115111)
_c_(115113, _n_(115112, "print", lambda: print), '\nConstruct a Dataframe using the said MultiIndex levels: ')
_l_(115114)
df = _c_(115122, _a_(115116, _n_(115115, "pd", lambda: pd), "DataFrame"), _c_(115120, _a_(115119, _a_(115118, _n_(115117, "np", lambda: np), "random"), "randn"), 8, 5), index=_n_(115121, "sales_index", lambda: sales_index))
_l_(115123)
_c_(115126, _n_(115124, "print", lambda: print), _n_(115125, "df", lambda: df))
_l_(115127)
_c_(115129, _n_(115128, "print", lambda: print), '\nExtract a single row from the said dataframe:')
_l_(115130)
_c_(115134, _n_(115131, "print", lambda: print), _a_(115133, _n_(115132, "df", lambda: df), "loc")['sale2', 'city2'])
_l_(115135)
_c_(115137, _n_(115136, "print", lambda: print), '\nExtract a single row from the said dataframe:')
_l_(115138)
_c_(115142, _n_(115139, "print", lambda: print), _a_(115141, _n_(115140, "df", lambda: df), "loc")['sale2', 'city2'])
_l_(115143)
_c_(115145, _n_(115144, "print", lambda: print), '\nExtract number of rows from the said dataframe:')
_l_(115146)
_c_(115150, _n_(115147, "print", lambda: print), _a_(115149, _n_(115148, "df", lambda: df), "loc")['sale1'])
_l_(115151)
_c_(115153, _n_(115152, "print", lambda: print), '\nExtract number of rows from the said dataframe:')
_l_(115154)
_c_(115158, _n_(115155, "print", lambda: print), _a_(115157, _n_(115156, "df", lambda: df), "loc")['sale3'])
_l_(115159)
_c_(115161, _n_(115160, "print", lambda: print), '\nExtract a single value from the said dataframe:')
_l_(115162)
_c_(115166, _n_(115163, "print", lambda: print), _a_(115165, _n_(115164, "df", lambda: df), "loc")[('sale1', 'city2'), 1])
_l_(115167)
_c_(115169, _n_(115168, "print", lambda: print), '\nExtract a single value from the said dataframe:')
_l_(115170)
_c_(115174, _n_(115171, "print", lambda: print), _a_(115173, _n_(115172, "df", lambda: df), "loc")[('sale4', 'city1'), 4])
_l_(115175)