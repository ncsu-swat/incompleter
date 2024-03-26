# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(113495)

except ImportError:
    pass
try:
    import numpy as np
    _l_(113497)

except ImportError:
    pass
sales_tuples = _c_(113502, _n_(113498, "list", lambda: list), _c_(113501, _n_(113499, "zip", lambda: zip), *_n_(113500, "sales_arrays", lambda: sales_arrays)))
_l_(113503)
sales_index = _c_(113508, _a_(113506, _a_(113505, _n_(113504, "pd", lambda: pd), "MultiIndex"), "from_tuples"), _n_(113507, "sales_tuples", lambda: sales_tuples), names=['sale', 'city'])
_l_(113509)
_c_(113512, _n_(113510, "print", lambda: print), _n_(113511, "sales_tuples", lambda: sales_tuples))
_l_(113513)
_c_(113515, _n_(113514, "print", lambda: print), '\nConstruct a Dataframe using the said MultiIndex levels: ')
_l_(113516)
df = _c_(113524, _a_(113518, _n_(113517, "pd", lambda: pd), "DataFrame"), _c_(113522, _a_(113521, _a_(113520, _n_(113519, "np", lambda: np), "random"), "randn"), 8, 5), index=_n_(113523, "sales_index", lambda: sales_index))
_l_(113525)
_c_(113528, _n_(113526, "print", lambda: print), _n_(113527, "df", lambda: df))
_l_(113529)
_c_(113531, _n_(113530, "print", lambda: print), '\nSort on MultiIndex DataFrame:')
_l_(113532)
df1 = _c_(113535, _a_(113534, _n_(113533, "df", lambda: df), "sort_index"))
_l_(113536)
_c_(113538, _n_(113537, "print", lambda: print), '\nSort on Index level=0 of the DataFrame:')
_l_(113539)
df2 = _c_(113542, _a_(113541, _n_(113540, "df", lambda: df), "sort_index"), level=0)
_l_(113543)
_c_(113546, _n_(113544, "print", lambda: print), _n_(113545, "df2", lambda: df2))
_l_(113547)
_c_(113549, _n_(113548, "print", lambda: print), '\nSort on Index level=1 of the DataFrame:')
_l_(113550)
df2 = _c_(113553, _a_(113552, _n_(113551, "df", lambda: df), "sort_index"), level=1)
_l_(113554)
_c_(113557, _n_(113555, "print", lambda: print), _n_(113556, "df2", lambda: df2))
_l_(113558)
_c_(113560, _n_(113559, "print", lambda: print), '\nPass a level name to sort the DataFrame:')
_l_(113561)
df3 = _c_(113564, _a_(113563, _n_(113562, "df", lambda: df), "sort_index"), level='city')
_l_(113565)
_c_(113568, _n_(113566, "print", lambda: print), _n_(113567, "df3", lambda: df3))
_l_(113569)