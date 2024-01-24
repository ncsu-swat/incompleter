# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67992681/typeerror-not-all-arguments-converted-during-string-formatting-when-pymysql-c
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
sql = 'create table if not exists currency(t integer primary key, prediction real default null, realVal real default null)'
_l_(635473)
_c_(635477, _a_(635475, _n_(635474, "cursor", lambda: cursor), "execute"), _n_(635476, "sql", lambda: sql))
_l_(635478)