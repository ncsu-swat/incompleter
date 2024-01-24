# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55805086/python-postgres-insert-error-typeerror-not-all-arguments-converted-during-stri
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
data1 = _c_(649073, _a_(649071, _n_(649070, "json", lambda: json), "load"), _n_(649072, "response", lambda: response))
_l_(649074)

volume = _c_(649077, _n_(649075, "len", lambda: len), _n_(649076, "data1", lambda: data1)['data'])
_l_(649078)


data = (_n_(649079, "data1", lambda: data1)["data"])
_l_(649080)

jsonstr = _c_(649084, _a_(649082, _n_(649081, "json", lambda: json), "dumps"), _n_(649083, "data", lambda: data), indent=4)
_l_(649085)

_c_(649088, _n_(649086, "print", lambda: print), _n_(649087, "jsonstr", lambda: jsonstr))
_l_(649089)

connection = _c_(649092, _a_(649091, _n_(649090, "psycopg2", lambda: psycopg2), "connect"), "host=localhost dbname=xxx user=xxx password=xxx")
_l_(649093)

cur = _c_(649096, _a_(649095, _n_(649094, "connection", lambda: connection), "cursor"))
_l_(649097)

_n_(649098, "connection", lambda: connection).autocommit = True
_l_(649099)

query =  "INSERT INTO xxx.xxx (xxx) VALUES (%s);"
_l_(649100)
sql = "INSERT INTO xxx.xxx VALUES (%s)"
_l_(649101)
_c_(649106, _a_(649103, _n_(649102, "cur", lambda: cur), "execute"), _n_(649104, "sql", lambda: sql), _n_(649105, "jsonstr", lambda: jsonstr))
_l_(649107)