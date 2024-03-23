# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(37235)

except ImportError:
    pass
try:
    import numpy as np
    _l_(37237)

except ImportError:
    pass
sales_arrays = [['sale1', 'sale1', 'sale3', 'sale3', 'sale2', 'sale2', 'sale4', 'sale4'], ['city1', 'city2', 'city1', 'city2', 'city1', 'city2', 'city1', 'city2']]
_l_(37238)
sales_tuples = _c_(37243, _n_(37239, "list", lambda: list), _c_(37242, _n_(37240, "zip", lambda: zip), *_n_(37241, "sales_arrays", lambda: sales_arrays)))
_l_(37244)
_c_(37247, _n_(37245, "print", lambda: print), _n_(37246, "sales_tuples", lambda: sales_tuples))
_l_(37248)
_c_(37250, _n_(37249, "print", lambda: print), '\nConstruct a Dataframe using the said MultiIndex levels: ')
_l_(37251)
df = _c_(37259, _a_(37253, _n_(37252, "pd", lambda: pd), "DataFrame"), _c_(37257, _a_(37256, _a_(37255, _n_(37254, "np", lambda: np), "random"), "randn"), 8, 5), index=_n_(37258, "sales_index", lambda: sales_index))
_l_(37260)
_c_(37263, _n_(37261, "print", lambda: print), _n_(37262, "df", lambda: df))
_l_(37264)
_c_(37266, _n_(37265, "print", lambda: print), '\nSort on MultiIndex DataFrame:')
_l_(37267)
df1 = _c_(37270, _a_(37269, _n_(37268, "df", lambda: df), "sort_index"))
_l_(37271)
_c_(37273, _n_(37272, "print", lambda: print), '\nSort on Index level=0 of the DataFrame:')
_l_(37274)
df2 = _c_(37277, _a_(37276, _n_(37275, "df", lambda: df), "sort_index"), level=0)
_l_(37278)
_c_(37281, _n_(37279, "print", lambda: print), _n_(37280, "df2", lambda: df2))
_l_(37282)
_c_(37284, _n_(37283, "print", lambda: print), '\nSort on Index level=1 of the DataFrame:')
_l_(37285)
df2 = _c_(37288, _a_(37287, _n_(37286, "df", lambda: df), "sort_index"), level=1)
_l_(37289)
_c_(37292, _n_(37290, "print", lambda: print), _n_(37291, "df2", lambda: df2))
_l_(37293)
_c_(37295, _n_(37294, "print", lambda: print), '\nPass a level name to sort the DataFrame:')
_l_(37296)
df3 = _c_(37299, _a_(37298, _n_(37297, "df", lambda: df), "sort_index"), level='city')
_l_(37300)
_c_(37303, _n_(37301, "print", lambda: print), _n_(37302, "df3", lambda: df3))
_l_(37304)