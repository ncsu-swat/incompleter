# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(115017)

except ImportError:
    pass
try:
    import numpy as np
    _l_(115019)

except ImportError:
    pass
sales_arrays = [['sale1', 'sale1', 'sale2', 'sale2', 'sale3', 'sale3', 'sale4', 'sale4'], ['city1', 'city2', 'city1', 'city2', 'city1', 'city2', 'city1', 'city2']]
_l_(115020)
sales_tuples = _c_(115025, _n_(115021, "list", lambda: list), _c_(115024, _n_(115022, "zip", lambda: zip), *_n_(115023, "sales_arrays", lambda: sales_arrays)))
_l_(115026)
sales_index = _c_(115031, _a_(115029, _a_(115028, _n_(115027, "pd", lambda: pd), "MultiIndex"), "from_tuples"), _n_(115030, "sales_tuples", lambda: sales_tuples), names=['sale', 'city'])
_l_(115032)
_c_(115035, _n_(115033, "print", lambda: print), _n_(115034, "sales_tuples", lambda: sales_tuples))
_l_(115036)
_c_(115038, _n_(115037, "print", lambda: print), '\nConstruct a Dataframe using the said MultiIndex levels: ')
_l_(115039)
_c_(115042, _n_(115040, "print", lambda: print), _n_(115041, "df", lambda: df))
_l_(115043)
_c_(115045, _n_(115044, "print", lambda: print), '\nExtract a single row from the said dataframe:')
_l_(115046)
_c_(115050, _n_(115047, "print", lambda: print), _a_(115049, _n_(115048, "df", lambda: df), "loc")['sale2', 'city2'])
_l_(115051)
_c_(115053, _n_(115052, "print", lambda: print), '\nExtract a single row from the said dataframe:')
_l_(115054)
_c_(115058, _n_(115055, "print", lambda: print), _a_(115057, _n_(115056, "df", lambda: df), "loc")['sale2', 'city2'])
_l_(115059)
_c_(115061, _n_(115060, "print", lambda: print), '\nExtract number of rows from the said dataframe:')
_l_(115062)
_c_(115066, _n_(115063, "print", lambda: print), _a_(115065, _n_(115064, "df", lambda: df), "loc")['sale1'])
_l_(115067)
_c_(115069, _n_(115068, "print", lambda: print), '\nExtract number of rows from the said dataframe:')
_l_(115070)
_c_(115074, _n_(115071, "print", lambda: print), _a_(115073, _n_(115072, "df", lambda: df), "loc")['sale3'])
_l_(115075)
_c_(115077, _n_(115076, "print", lambda: print), '\nExtract a single value from the said dataframe:')
_l_(115078)
_c_(115082, _n_(115079, "print", lambda: print), _a_(115081, _n_(115080, "df", lambda: df), "loc")[('sale1', 'city2'), 1])
_l_(115083)
_c_(115085, _n_(115084, "print", lambda: print), '\nExtract a single value from the said dataframe:')
_l_(115086)
_c_(115090, _n_(115087, "print", lambda: print), _a_(115089, _n_(115088, "df", lambda: df), "loc")[('sale4', 'city1'), 4])
_l_(115091)