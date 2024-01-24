# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58458756/pyodbc-type-error-the-first-argument-to-execute-must-be-a-string-or-unicode-q
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pyodbc
    _l_(688045)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(688047)

except ImportError:
    pass

conn = _c_(688050, _a_(688049, _n_(688048, "pyodbc", lambda: pyodbc), "connect"), 'DRIVER={SQL Server};'
                      'SERVER=192.168.1.30;'
                      'DATABASE=Datamart;'
                      'Trusted_Connection=yes;')
_l_(688051)
cursor = _c_(688054, _a_(688053, _n_(688052, "conn", lambda: conn), "cursor")) 
_l_(688055) 
for row in _c_(688058, _a_(688057, _n_(688056, "cursor", lambda: cursor), "tables"), tableType='TABLE'):
    _l_(688063)

    _c_(688061, _n_(688059, "print", lambda: print), _n_(688060, "row", lambda: row))
    _l_(688062)
sql = """SELECT * FROM ETL.Dim_FC_UPS_Interface_Detail"""
_l_(688064)
_c_(688069, _a_(688066, _n_(688065, "cursor", lambda: cursor), "execute"), _n_(688067, "row", lambda: row), _n_(688068, "sql", lambda: sql))
_l_(688070)

df = _c_(688075, _a_(688072, _n_(688071, "pd", lambda: pd), "read_sql"), _n_(688073, "sql", lambda: sql), _n_(688074, "conn", lambda: conn))
_l_(688076)
_c_(688079, _a_(688078, _n_(688077, "df", lambda: df), "head"))
_l_(688080)