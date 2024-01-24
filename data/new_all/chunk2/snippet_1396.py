# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65010286/typeerror-sqlite3-cursor-object-is-not-subscriptable-how-to-print-sql-select
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sqlite3
    _l_(453004)

except ImportError:
    pass
con=_c_(453007, _a_(453006, _n_(453005, "sqlite3", lambda: sqlite3), "connect"), "aditi")
_l_(453008)
_c_(453011, _a_(453010, _n_(453009, "con", lambda: con), "execute"), '''CREATE TABLE IF NOT EXISTS LOGIN
                   (ID         INTEGER PRIMARY KEY AUTOINCREMENT,
                    NAME       TEXT NOT NULL,
                    ROLL       INT NOT NULL,
                    PASS       TEXT NOT NULL);''')
_l_(453012)
quer=f'''INSERT INTO LOGIN(NAME,ROLL,PASS) VALUES('ADMIN','0','ADMIN123')'''
_l_(453013)
_c_(453017, _a_(453015, _n_(453014, "con", lambda: con), "execute"), _n_(453016, "quer", lambda: quer))
_l_(453018)
_c_(453021, _a_(453020, _n_(453019, "con", lambda: con), "commit"))
_l_(453022)

cursor=_c_(453025, _a_(453024, _n_(453023, "con", lambda: con), "execute"), '''SELECT NAME FROM LOGIN''')
_l_(453026)
_c_(453029, _n_(453027, "print", lambda: print), _n_(453028, "cursor", lambda: cursor)[0])   
_l_(453030)   
_c_(453033, _a_(453032, _n_(453031, "con", lambda: con), "close"))
_l_(453034)