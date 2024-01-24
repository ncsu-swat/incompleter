# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54480138/typeerror-parser-f-got-multiple-values-for-argument-sep
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(398045)

except ImportError:
    pass

df = _c_(398050, _a_(398047, _n_(398046, "pd", lambda: pd), "read_csv"), _c_(398049, _n_(398048, "open", lambda: open), 'duplicate1.csv'),'Sheet1',sep=',',delimiter=None, index_col=0)
_l_(398051)

_c_(398054, _a_(398053, _n_(398052, "df", lambda: df), "to_excel"), 'duplicateexcel.xlsx',encoding='utf-8')
_l_(398055)