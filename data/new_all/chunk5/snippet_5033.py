# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49249504/typeerror-argument-of-type-datetime-date-is-not-iterable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
connection = _c_(688334, _a_(688333, _n_(688332, "MySQLdb", lambda: MySQLdb), "connect"), host = "192.168.1.50", user = "root", 
password = "root", db = "mydb", port = 32768)
_l_(688335)
cursor = _c_(688338, _a_(688337, _n_(688336, "connection", lambda: connection), "cursor"))
_l_(688339)
_c_(688342, _a_(688341, _n_(688340, "cursor", lambda: cursor), "execute"), "select * from licenses")
_l_(688343)
data = _c_(688346, _a_(688345, _n_(688344, "cursor", lambda: cursor), "fetchall"))
_l_(688347)