# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64940395/typeerror-read-excel-got-an-unexpected-keyword-argument-parse-cols
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(447477)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(447479)

except ImportError:
    pass

url = 'https://www.dropbox.com/s/yze3laidhv7gl1x/Homework4.xlsx?dl=1'
_l_(447480)

changedate = lambda x: _c_(447484, _a_(447482, _n_(447481, "pd", lambda: pd), "to_datetime"), _n_(447483, "x", lambda: x), format = "%Y%m") 
_l_(447485) 

df = _c_(447490, _a_(447487, _n_(447486, "pd", lambda: pd), "read_excel"), _n_(447488, "url", lambda: url), sheet_name = '49_Industry_Portfolios', header = 6, 
                   parse_cols = 'AZ:CW', index_col = 0, parse_dates = True, 
                   date_parser = _n_(447489, "changedate", lambda: changedate), na_values = [-99.99, -999])
_l_(447491)
_c_(447494, _n_(447492, "print", lambda: print), _n_(447493, "df", lambda: df))
_l_(447495)