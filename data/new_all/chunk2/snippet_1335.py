# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/40892848/attributeerror-connection-object-has-no-attribute-fetchall
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
engine_str = 'mysql+mysqlconnector://my_username:my_pass@localhost/my_db'
_l_(454770)
engine = _c_(454774, _a_(454772, _n_(454771, "sqlalchemy", lambda: sqlalchemy), "create_engine"), _n_(454773, "engine_str", lambda: engine_str), echo=False, encoding='utf-8')
_l_(454775)
connection = _c_(454778, _a_(454777, _n_(454776, "engine", lambda: engine), "connect"))
_l_(454779)
query = "SELECT * from history_table"
_l_(454780)

_c_(454784, _a_(454782, _n_(454781, "connection", lambda: connection), "execute"), _n_(454783, "query", lambda: query))
_l_(454785)
rows = _c_(454788, _a_(454787, _n_(454786, "connection", lambda: connection), "fetchall"))
_l_(454789)