# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/47422466/type-error-in-pymysql-cursor
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
connection = _c_(469211, _a_(469210, _n_(469209, "pymysql", lambda: pymysql), "connect"), host = "localhost",
                     user = "root",
                     passwd = "",
                     db = "bugs",
                     charset = "utf8mb4",
                     cursorclass = "pymysql.cursors.Dictcursor")
_l_(469212)

try:
    _l_(469238)

    with _c_(469215, _a_(469214, _n_(469213, "connection", lambda: connection), "cursor")) as cur:
        _l_(469228)

        _c_(469218, _a_(469217, _n_(469216, "cur", lambda: cur), "execute"), '''SELECT COUNT(*) FROM tbl_firefox''')
        _l_(469219)

        for row in _c_(469222, _a_(469221, _n_(469220, "cur", lambda: cur), "fetchall")):
            _l_(469227)

            _c_(469225, _n_(469223, "print", lambda: print), "Number of rows in firefox table:", _n_(469224, "row", lambda: row))
            _l_(469226)
    _c_(469231, _a_(469230, _n_(469229, "connection", lambda: connection), "commit"))
    _l_(469232)
finally:
    _l_(469237)

    _c_(469235, _a_(469234, _n_(469233, "connection", lambda: connection), "close"))
    _l_(469236)