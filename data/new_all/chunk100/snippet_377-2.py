# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(113285)

except ImportError:
    pass
try:
    import numpy as np
    _l_(113287)

except ImportError:
    pass
sales_arrays = [['sale1', 'sale1', 'sale3', 'sale3', 'sale2', 'sale2', 'sale4', 'sale4'], ['city1', 'city2', 'city1', 'city2', 'city1', 'city2', 'city1', 'city2']]
_l_(113288)
sales_tuples = _c_(113293, _n_(113289, "list", lambda: list), _c_(113292, _n_(113290, "zip", lambda: zip), *_n_(113291, "sales_arrays", lambda: sales_arrays)))
_l_(113294)
_c_(113297, _n_(113295, "print", lambda: print), _n_(113296, "sales_tuples", lambda: sales_tuples))
_l_(113298)
_c_(113300, _n_(113299, "print", lambda: print), '\nConstruct a Dataframe using the said MultiIndex levels: ')
_l_(113301)
df = _c_(113309, _a_(113303, _n_(113302, "pd", lambda: pd), "DataFrame"), _c_(113307, _a_(113306, _a_(113305, _n_(113304, "np", lambda: np), "random"), "randn"), 8, 5), index=_n_(113308, "sales_index", lambda: sales_index))
_l_(113310)
_c_(113313, _n_(113311, "print", lambda: print), _n_(113312, "df", lambda: df))
_l_(113314)
_c_(113316, _n_(113315, "print", lambda: print), '\nSort on MultiIndex DataFrame:')
_l_(113317)
df1 = _c_(113320, _a_(113319, _n_(113318, "df", lambda: df), "sort_index"))
_l_(113321)
_c_(113323, _n_(113322, "print", lambda: print), '\nSort on Index level=0 of the DataFrame:')
_l_(113324)
df2 = _c_(113327, _a_(113326, _n_(113325, "df", lambda: df), "sort_index"), level=0)
_l_(113328)
_c_(113331, _n_(113329, "print", lambda: print), _n_(113330, "df2", lambda: df2))
_l_(113332)
_c_(113334, _n_(113333, "print", lambda: print), '\nSort on Index level=1 of the DataFrame:')
_l_(113335)
df2 = _c_(113338, _a_(113337, _n_(113336, "df", lambda: df), "sort_index"), level=1)
_l_(113339)
_c_(113342, _n_(113340, "print", lambda: print), _n_(113341, "df2", lambda: df2))
_l_(113343)
_c_(113345, _n_(113344, "print", lambda: print), '\nPass a level name to sort the DataFrame:')
_l_(113346)
df3 = _c_(113349, _a_(113348, _n_(113347, "df", lambda: df), "sort_index"), level='city')
_l_(113350)
_c_(113353, _n_(113351, "print", lambda: print), _n_(113352, "df3", lambda: df3))
_l_(113354)