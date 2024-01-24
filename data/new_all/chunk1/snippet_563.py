# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50053995/attributeerror-mysql-connection-object-has-no-attribute-cursor
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import _mysql as mc
    _l_(403140)

except ImportError:
    pass

db = _c_(403143, _a_(403142, _n_(403141, "mc", lambda: mc), "connect"), host = "localhost", user = "root", passwd = "password1234")
_l_(403144)
cursor = _c_(403147, _a_(403146, _n_(403145, "db", lambda: db), "cursor"))
_l_(403148)