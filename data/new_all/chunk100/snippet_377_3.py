# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(37306)

except ImportError:
    pass
try:
    import numpy as np
    _l_(37308)

except ImportError:
    pass
sales_tuples = _c_(37313, _n_(37309, "list", lambda: list), _c_(37312, _n_(37310, "zip", lambda: zip), *_n_(37311, "sales_arrays", lambda: sales_arrays)))
_l_(37314)
sales_index = _c_(37319, _a_(37317, _a_(37316, _n_(37315, "pd", lambda: pd), "MultiIndex"), "from_tuples"), _n_(37318, "sales_tuples", lambda: sales_tuples), names=['sale', 'city'])
_l_(37320)
_c_(37323, _n_(37321, "print", lambda: print), _n_(37322, "sales_tuples", lambda: sales_tuples))
_l_(37324)
_c_(37326, _n_(37325, "print", lambda: print), '\nConstruct a Dataframe using the said MultiIndex levels: ')
_l_(37327)
df = _c_(37335, _a_(37329, _n_(37328, "pd", lambda: pd), "DataFrame"), _c_(37333, _a_(37332, _a_(37331, _n_(37330, "np", lambda: np), "random"), "randn"), 8, 5), index=_n_(37334, "sales_index", lambda: sales_index))
_l_(37336)
_c_(37339, _n_(37337, "print", lambda: print), _n_(37338, "df", lambda: df))
_l_(37340)
_c_(37342, _n_(37341, "print", lambda: print), '\nSort on MultiIndex DataFrame:')
_l_(37343)
df1 = _c_(37346, _a_(37345, _n_(37344, "df", lambda: df), "sort_index"))
_l_(37347)
_c_(37349, _n_(37348, "print", lambda: print), '\nSort on Index level=0 of the DataFrame:')
_l_(37350)
df2 = _c_(37353, _a_(37352, _n_(37351, "df", lambda: df), "sort_index"), level=0)
_l_(37354)
_c_(37357, _n_(37355, "print", lambda: print), _n_(37356, "df2", lambda: df2))
_l_(37358)
_c_(37360, _n_(37359, "print", lambda: print), '\nSort on Index level=1 of the DataFrame:')
_l_(37361)
df2 = _c_(37364, _a_(37363, _n_(37362, "df", lambda: df), "sort_index"), level=1)
_l_(37365)
_c_(37368, _n_(37366, "print", lambda: print), _n_(37367, "df2", lambda: df2))
_l_(37369)
_c_(37371, _n_(37370, "print", lambda: print), '\nPass a level name to sort the DataFrame:')
_l_(37372)
df3 = _c_(37375, _a_(37374, _n_(37373, "df", lambda: df), "sort_index"), level='city')
_l_(37376)
_c_(37379, _n_(37377, "print", lambda: print), _n_(37378, "df3", lambda: df3))
_l_(37380)