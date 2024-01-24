# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67992681/typeerror-not-all-arguments-converted-during-string-formatting-when-pymysql-c
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
data = [(1, 12.5), (2, 10.2)]
_l_(640945)
sql = 'insert into currency(t, prediction) values(%s, %s) on duplicate key update values prediction=values(prediction)'
_l_(640946)
_c_(640951, _a_(640948, _n_(640947, "cursor", lambda: cursor), "execute"), _n_(640949, "sql", lambda: sql), _n_(640950, "data", lambda: data))
_l_(640952)