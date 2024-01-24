# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70081820/ibm-as400-file-not-found-error-while-the-table-object-is-still-there
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pyodbc
    _l_(645803)

except ImportError:
    pass

connection = _c_(645806, _a_(645805, _n_(645804, "pyodbc", lambda: pyodbc), "connect"), Driver='{iSeries Access ODBC Driver}',
    System='<host>',
    database='<database>',
    uid='<username>',
    pwd='<password>')
_l_(645807)
c1 = _c_(645810, _a_(645809, _n_(645808, "connection", lambda: connection), "cursor"))
_l_(645811)
_c_(645813, _n_(645812, "print", lambda: print), 'Connection established')
_l_(645814)