# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(37094)

except ImportError:
    pass
try:
    import numpy as np
    _l_(37096)

except ImportError:
    pass
sales_arrays = [['sale1', 'sale1', 'sale3', 'sale3', 'sale2', 'sale2', 'sale4', 'sale4'], ['city1', 'city2', 'city1', 'city2', 'city1', 'city2', 'city1', 'city2']]
_l_(37097)
sales_tuples = _c_(37102, _n_(37098, "list", lambda: list), _c_(37101, _n_(37099, "zip", lambda: zip), *_n_(37100, "sales_arrays", lambda: sales_arrays)))
_l_(37103)
sales_index = _c_(37108, _a_(37106, _a_(37105, _n_(37104, "pd", lambda: pd), "MultiIndex"), "from_tuples"), _n_(37107, "sales_tuples", lambda: sales_tuples), names=['sale', 'city'])
_l_(37109)
_c_(37112, _n_(37110, "print", lambda: print), _n_(37111, "sales_tuples", lambda: sales_tuples))
_l_(37113)
_c_(37115, _n_(37114, "print", lambda: print), '\nConstruct a Dataframe using the said MultiIndex levels: ')
_l_(37116)
_c_(37119, _n_(37117, "print", lambda: print), _n_(37118, "df", lambda: df))
_l_(37120)
_c_(37122, _n_(37121, "print", lambda: print), '\nSort on MultiIndex DataFrame:')
_l_(37123)
df1 = _c_(37126, _a_(37125, _n_(37124, "df", lambda: df), "sort_index"))
_l_(37127)
_c_(37129, _n_(37128, "print", lambda: print), '\nSort on Index level=0 of the DataFrame:')
_l_(37130)
df2 = _c_(37133, _a_(37132, _n_(37131, "df", lambda: df), "sort_index"), level=0)
_l_(37134)
_c_(37137, _n_(37135, "print", lambda: print), _n_(37136, "df2", lambda: df2))
_l_(37138)
_c_(37140, _n_(37139, "print", lambda: print), '\nSort on Index level=1 of the DataFrame:')
_l_(37141)
df2 = _c_(37144, _a_(37143, _n_(37142, "df", lambda: df), "sort_index"), level=1)
_l_(37145)
_c_(37148, _n_(37146, "print", lambda: print), _n_(37147, "df2", lambda: df2))
_l_(37149)
_c_(37151, _n_(37150, "print", lambda: print), '\nPass a level name to sort the DataFrame:')
_l_(37152)
df3 = _c_(37155, _a_(37154, _n_(37153, "df", lambda: df), "sort_index"), level='city')
_l_(37156)
_c_(37159, _n_(37157, "print", lambda: print), _n_(37158, "df3", lambda: df3))
_l_(37160)