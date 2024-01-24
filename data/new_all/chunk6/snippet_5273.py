# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75028036/flask-attributeerror-mysql-object-has-no-attribute-model
# msql_connector.py

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from application import mysql
    _l_(349727)

except ImportError:
    pass


_c_(349730, _n_(349728, "print", lambda: print), _n_(349729, "mysql", lambda: mysql))
_l_(349731)


conn = _c_(349734, _a_(349733, _n_(349732, "mysql", lambda: mysql), "connect"))
_l_(349735)
cursor = _c_(349738, _a_(349737, _n_(349736, "conn", lambda: conn), "cursor"))
_l_(349739)


_c_(349742, _a_(349741, _n_(349740, "cursor", lambda: cursor), "execute"), '''SHOW SCHEMAS;''')
_l_(349743)
rv = _c_(349746, _a_(349745, _n_(349744, "cursor", lambda: cursor), "fetchall"))
_l_(349747)

for db in _n_(349748, "rv", lambda: rv):
    _l_(349753)

    _c_(349751, _n_(349749, "print", lambda: print), _n_(349750, "db", lambda: db))
    _l_(349752)