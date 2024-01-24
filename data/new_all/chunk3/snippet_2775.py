# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63683032/attributeerror-sqlite3-connection-object-attribute-execute-is-read-only-p
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os, sys
    _l_(535069)

except ImportError:
    pass
try:
    import sqlite3
    _l_(535071)

except ImportError:
    pass
try:
    from sqlite3 import Error
    _l_(535073)

except ImportError:
    pass

connection = None
_l_(535074)
try:
    _l_(535092)

    connection = _c_(535077, _a_(535076, _n_(535075, "sqlite3", lambda: sqlite3), "connect"), 'database.db')
    _l_(535078)
    cursor = _c_(535081, _a_(535080, _n_(535079, "connection", lambda: connection), "cursor"))
    _l_(535082)
    _c_(535084, _n_(535083, "print", lambda: print), "Connection to SQLite DB successful")
    _l_(535085)
except _n_(535086, "Error", lambda: Error) as e:
    _l_(535091)

    _c_(535089, _n_(535087, "print", lambda: print), f"The error '{_n_(535088, 'e', lambda: e)}' occurred")
    _l_(535090)

_c_(535095, _a_(535094, _n_(535093, "cursor", lambda: cursor), "execute"), """CREATE TABLE IF NOT EXISTS Tickets ( 
    id INT,
    indexNumber INT,
    movieNumber INT,
    screeningHall VARCHAR(30),
    movieName VARCHAR(30),
    screeningDate VARCHAR(30),
    screeningTime VARCHAR(30),
    ticketRow INT,
    ticketCol INT,
    ticketType VARCHAR(30),
    ticketPrice VARCHAR(30))"""
)
_l_(535096)
idNum = 0
_l_(535097)
tempInfoDict = {'indexNumber': 0, 'movieNumber': 1, 'hall': 'Hall 1', 'name': 'Terminator', 'date': '2020-09-01', 'time': '10:40', 'row': 1, 'col': 0}
_l_(535098)

_n_(535099, "connection", lambda: connection).execute = ("INSERT INTO Tickets (id, indexNumber, movieNumber, screeningHall, movieName, screeningDate, screeningTime, ticketRow, ticketCol, ticketType, ticketPrice) values(?,?,?,?,?,?,?,?,?,?,?)",
                                            (_n_(535100, "idNum", lambda: idNum), _n_(535101, "tempInfoDict", lambda: tempInfoDict)['indexNumber'], _n_(535102, "tempInfoDict", lambda: tempInfoDict)['movieNumber'], _n_(535103, "tempInfoDict", lambda: tempInfoDict)['hall'], _n_(535104, "tempInfoDict", lambda: tempInfoDict)['name'],
                                            _n_(535105, "tempInfoDict", lambda: tempInfoDict)['date'], _n_(535106, "tempInfoDict", lambda: tempInfoDict)['time'], _n_(535107, "tempInfoDict", lambda: tempInfoDict)['row'], _n_(535108, "tempInfoDict", lambda: tempInfoDict)['col'], 'Basic', '$20'))
_l_(535109)

_c_(535112, _a_(535111, _n_(535110, "connection", lambda: connection), "commit"))
_l_(535113)
_c_(535116, _a_(535115, _n_(535114, "connection", lambda: connection), "close"))
_l_(535117)