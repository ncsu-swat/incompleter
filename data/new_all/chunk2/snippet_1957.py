# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75388748/typeerror-read-excel-got-an-unexpected-keyword-argument-dtype
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(427723)

except ImportError:
    pass
data = _c_(427727, _a_(427725, _n_(427724, "pd", lambda: pd), "read_excel"), 'sheet_path', 'sheet_name', dtype={'col1':_n_(427726, "str", lambda: str)})
_l_(427728)