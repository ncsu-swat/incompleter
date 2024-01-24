# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49249504/typeerror-argument-of-type-datetime-date-is-not-iterable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
connection = _c_(672715, _a_(672714, _n_(672713, "MySQLdb", lambda: MySQLdb), "connect"), host = "192.168.1.50", user = "root", 
password = "root", db = "mydb", port = 32768)
_l_(672716)
cursor = _c_(672719, _a_(672718, _n_(672717, "connection", lambda: connection), "cursor"))
_l_(672720)
_c_(672723, _a_(672722, _n_(672721, "cursor", lambda: cursor), "execute"), "select * from licenses")
_l_(672724)
data = _c_(672727, _a_(672726, _n_(672725, "cursor", lambda: cursor), "fetchall"))
_l_(672728)