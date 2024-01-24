# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/52786661/typeerror-in-string-requires-string-as-left-operand-not-float
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(338051)

except ImportError:
    pass

data = _c_(338054, _a_(338053, _n_(338052, "pd", lambda: pd), "read_excel"), 'C:/Users/my/Desktop/my_list.xlsx', 'Sheet1')
_l_(338055)
real_list = _c_(338058, _a_(338057, _n_(338056, "data", lambda: data)['name'], "tolist"))
_l_(338059)