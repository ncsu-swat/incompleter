# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(113139)

except ImportError:
    pass
try:
    import numpy as np
    _l_(113141)

except ImportError:
    pass
sales_arrays = [['sale1', 'sale1', 'sale3', 'sale3', 'sale2', 'sale2', 'sale4', 'sale4'], ['city1', 'city2', 'city1', 'city2', 'city1', 'city2', 'city1', 'city2']]
_l_(113142)
sales_tuples = _c_(113147, _n_(113143, "list", lambda: list), _c_(113146, _n_(113144, "zip", lambda: zip), *_n_(113145, "sales_arrays", lambda: sales_arrays)))
_l_(113148)
sales_index = _c_(113153, _a_(113151, _a_(113150, _n_(113149, "pd", lambda: pd), "MultiIndex"), "from_tuples"), _n_(113152, "sales_tuples", lambda: sales_tuples), names=['sale', 'city'])
_l_(113154)
_c_(113157, _n_(113155, "print", lambda: print), _n_(113156, "sales_tuples", lambda: sales_tuples))
_l_(113158)
_c_(113160, _n_(113159, "print", lambda: print), '\nConstruct a Dataframe using the said MultiIndex levels: ')
_l_(113161)
df = _c_(113169, _a_(113163, _n_(113162, "pd", lambda: pd), "DataFrame"), _c_(113167, _a_(113166, _a_(113165, _n_(113164, "np", lambda: np), "random"), "randn"), 8, 5), index=_n_(113168, "sales_index", lambda: sales_index))
_l_(113170)
_c_(113173, _n_(113171, "print", lambda: print), _n_(113172, "df", lambda: df))
_l_(113174)
_c_(113176, _n_(113175, "print", lambda: print), '\nSort on MultiIndex DataFrame:')
_l_(113177)
df1 = _c_(113180, _a_(113179, _n_(113178, "df", lambda: df), "sort_index"))
_l_(113181)
_c_(113183, _n_(113182, "print", lambda: print), '\nSort on Index level=0 of the DataFrame:')
_l_(113184)
_c_(113187, _n_(113185, "print", lambda: print), _n_(113186, "df2", lambda: df2))
_l_(113188)
_c_(113190, _n_(113189, "print", lambda: print), '\nSort on Index level=1 of the DataFrame:')
_l_(113191)
df2 = _c_(113194, _a_(113193, _n_(113192, "df", lambda: df), "sort_index"), level=1)
_l_(113195)
_c_(113198, _n_(113196, "print", lambda: print), _n_(113197, "df2", lambda: df2))
_l_(113199)
_c_(113201, _n_(113200, "print", lambda: print), '\nPass a level name to sort the DataFrame:')
_l_(113202)
df3 = _c_(113205, _a_(113204, _n_(113203, "df", lambda: df), "sort_index"), level='city')
_l_(113206)
_c_(113209, _n_(113207, "print", lambda: print), _n_(113208, "df3", lambda: df3))
_l_(113210)