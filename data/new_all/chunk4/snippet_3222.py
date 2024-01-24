# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/77152839/reason-attributeerror-can-only-use-dt-accessor-with-datetimelike-values
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(608866)

except ImportError:
    pass
file = '/pathtocsv.csv'
_l_(608867)
df = _c_(608871, _a_(608869, _n_(608868, "pd", lambda: pd), "read_csv"), _n_(608870, "file", lambda: file), sep = ',', encoding='utf-8-sig', usecols= ['Date', 'ids'])    
_l_(608872)    
_n_(608873, "df", lambda: df)['Date'] = _c_(608877, _a_(608875, _n_(608874, "pd", lambda: pd), "to_datetime"), _n_(608876, "df", lambda: df)['Date'])
_l_(608878)
_n_(608879, "df", lambda: df)['Month'] = _a_(608882, _a_(608881, _n_(608880, "df", lambda: df)['Date'], "dt"), "month")
_l_(608883)