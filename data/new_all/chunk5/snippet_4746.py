# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49552931/typeerror-when-sqlalchemy-engine-connect-tries-to-compare-ms-sql-server-version
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from sqlalchemy import create_engine
    _l_(685445)

except ImportError:
    pass
try:
    import pyodbc
    _l_(685447)

except ImportError:
    pass

engine = _c_(685449, _n_(685448, "create_engine", lambda: create_engine), "mssql+pyodbc://user:pass@mydsn", echo=True)
_l_(685450)
cnxn = _c_(685453, _a_(685452, _n_(685451, "engine", lambda: engine), "connect"))
_l_(685454)
rows = _c_(685459, _a_(685458, _c_(685457, _a_(685456, _n_(685455, "cnxn", lambda: cnxn), "execute"), "SELECT name FROM sys.tables"), "fetchall"))
_l_(685460)
_c_(685463, _n_(685461, "print", lambda: print), _n_(685462, "rows", lambda: rows))
_l_(685464)