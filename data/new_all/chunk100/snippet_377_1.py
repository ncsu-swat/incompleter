# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(37162)

except ImportError:
    pass
try:
    import numpy as np
    _l_(37164)

except ImportError:
    pass
sales_arrays = [['sale1', 'sale1', 'sale3', 'sale3', 'sale2', 'sale2', 'sale4', 'sale4'], ['city1', 'city2', 'city1', 'city2', 'city1', 'city2', 'city1', 'city2']]
_l_(37165)
sales_tuples = _c_(37170, _n_(37166, "list", lambda: list), _c_(37169, _n_(37167, "zip", lambda: zip), *_n_(37168, "sales_arrays", lambda: sales_arrays)))
_l_(37171)
sales_index = _c_(37176, _a_(37174, _a_(37173, _n_(37172, "pd", lambda: pd), "MultiIndex"), "from_tuples"), _n_(37175, "sales_tuples", lambda: sales_tuples), names=['sale', 'city'])
_l_(37177)
_c_(37180, _n_(37178, "print", lambda: print), _n_(37179, "sales_tuples", lambda: sales_tuples))
_l_(37181)
_c_(37183, _n_(37182, "print", lambda: print), '\nConstruct a Dataframe using the said MultiIndex levels: ')
_l_(37184)
df = _c_(37192, _a_(37186, _n_(37185, "pd", lambda: pd), "DataFrame"), _c_(37190, _a_(37189, _a_(37188, _n_(37187, "np", lambda: np), "random"), "randn"), 8, 5), index=_n_(37191, "sales_index", lambda: sales_index))
_l_(37193)
_c_(37196, _n_(37194, "print", lambda: print), _n_(37195, "df", lambda: df))
_l_(37197)
_c_(37199, _n_(37198, "print", lambda: print), '\nSort on MultiIndex DataFrame:')
_l_(37200)
df1 = _c_(37203, _a_(37202, _n_(37201, "df", lambda: df), "sort_index"))
_l_(37204)
_c_(37206, _n_(37205, "print", lambda: print), '\nSort on Index level=0 of the DataFrame:')
_l_(37207)
_c_(37210, _n_(37208, "print", lambda: print), _n_(37209, "df2", lambda: df2))
_l_(37211)
_c_(37213, _n_(37212, "print", lambda: print), '\nSort on Index level=1 of the DataFrame:')
_l_(37214)
df2 = _c_(37217, _a_(37216, _n_(37215, "df", lambda: df), "sort_index"), level=1)
_l_(37218)
_c_(37221, _n_(37219, "print", lambda: print), _n_(37220, "df2", lambda: df2))
_l_(37222)
_c_(37224, _n_(37223, "print", lambda: print), '\nPass a level name to sort the DataFrame:')
_l_(37225)
df3 = _c_(37228, _a_(37227, _n_(37226, "df", lambda: df), "sort_index"), level='city')
_l_(37229)
_c_(37232, _n_(37230, "print", lambda: print), _n_(37231, "df3", lambda: df3))
_l_(37233)