# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58458756/pyodbc-type-error-the-first-argument-to-execute-must-be-a-string-or-unicode-q
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pyodbc
    _l_(691595)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(691597)

except ImportError:
    pass

conn = _c_(691600, _a_(691599, _n_(691598, "pyodbc", lambda: pyodbc), "connect"), 'DRIVER={SQL Server};'
                      'SERVER=192.168.1.30;'
                      'DATABASE=Datamart;'
                      'Trusted_Connection=yes;')
_l_(691601)
cursor = _c_(691604, _a_(691603, _n_(691602, "conn", lambda: conn), "cursor")) 
_l_(691605) 
for row in _c_(691608, _a_(691607, _n_(691606, "cursor", lambda: cursor), "tables"), tableType='TABLE'):
    _l_(691613)

    _c_(691611, _n_(691609, "print", lambda: print), _n_(691610, "row", lambda: row))
    _l_(691612)
sql = """SELECT * FROM ETL.Dim_FC_UPS_Interface_Detail"""
_l_(691614)
_c_(691619, _a_(691616, _n_(691615, "cursor", lambda: cursor), "execute"), _n_(691617, "row", lambda: row), _n_(691618, "sql", lambda: sql))
_l_(691620)

df = _c_(691625, _a_(691622, _n_(691621, "pd", lambda: pd), "read_sql"), _n_(691623, "sql", lambda: sql), _n_(691624, "conn", lambda: conn))
_l_(691626)
_c_(691629, _a_(691628, _n_(691627, "df", lambda: df), "head"))
_l_(691630)