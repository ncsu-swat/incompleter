# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(114938)

except ImportError:
    pass
try:
    import numpy as np
    _l_(114940)

except ImportError:
    pass
sales_arrays = [['sale1', 'sale1', 'sale2', 'sale2', 'sale3', 'sale3', 'sale4', 'sale4'], ['city1', 'city2', 'city1', 'city2', 'city1', 'city2', 'city1', 'city2']]
_l_(114941)
sales_index = _c_(114946, _a_(114944, _a_(114943, _n_(114942, "pd", lambda: pd), "MultiIndex"), "from_tuples"), _n_(114945, "sales_tuples", lambda: sales_tuples), names=['sale', 'city'])
_l_(114947)
_c_(114950, _n_(114948, "print", lambda: print), _n_(114949, "sales_tuples", lambda: sales_tuples))
_l_(114951)
_c_(114953, _n_(114952, "print", lambda: print), '\nConstruct a Dataframe using the said MultiIndex levels: ')
_l_(114954)
df = _c_(114962, _a_(114956, _n_(114955, "pd", lambda: pd), "DataFrame"), _c_(114960, _a_(114959, _a_(114958, _n_(114957, "np", lambda: np), "random"), "randn"), 8, 5), index=_n_(114961, "sales_index", lambda: sales_index))
_l_(114963)
_c_(114966, _n_(114964, "print", lambda: print), _n_(114965, "df", lambda: df))
_l_(114967)
_c_(114969, _n_(114968, "print", lambda: print), '\nExtract a single row from the said dataframe:')
_l_(114970)
_c_(114974, _n_(114971, "print", lambda: print), _a_(114973, _n_(114972, "df", lambda: df), "loc")['sale2', 'city2'])
_l_(114975)
_c_(114977, _n_(114976, "print", lambda: print), '\nExtract a single row from the said dataframe:')
_l_(114978)
_c_(114982, _n_(114979, "print", lambda: print), _a_(114981, _n_(114980, "df", lambda: df), "loc")['sale2', 'city2'])
_l_(114983)
_c_(114985, _n_(114984, "print", lambda: print), '\nExtract number of rows from the said dataframe:')
_l_(114986)
_c_(114990, _n_(114987, "print", lambda: print), _a_(114989, _n_(114988, "df", lambda: df), "loc")['sale1'])
_l_(114991)
_c_(114993, _n_(114992, "print", lambda: print), '\nExtract number of rows from the said dataframe:')
_l_(114994)
_c_(114998, _n_(114995, "print", lambda: print), _a_(114997, _n_(114996, "df", lambda: df), "loc")['sale3'])
_l_(114999)
_c_(115001, _n_(115000, "print", lambda: print), '\nExtract a single value from the said dataframe:')
_l_(115002)
_c_(115006, _n_(115003, "print", lambda: print), _a_(115005, _n_(115004, "df", lambda: df), "loc")[('sale1', 'city2'), 1])
_l_(115007)
_c_(115009, _n_(115008, "print", lambda: print), '\nExtract a single value from the said dataframe:')
_l_(115010)
_c_(115014, _n_(115011, "print", lambda: print), _a_(115013, _n_(115012, "df", lambda: df), "loc")[('sale4', 'city1'), 4])
_l_(115015)