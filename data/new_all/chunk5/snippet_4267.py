# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57566737/attributeerror-module-rethinkdb-has-no-attribute-connect
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import rethinkdb as rdb
    _l_(651940)

except ImportError:
    pass
r = _c_(651943, _a_(651942, _n_(651941, "rdb", lambda: rdb), "RethinkDB"))
_l_(651944)
_n_(651945, "self", lambda: self).conn = _c_(651948, _a_(651947, _n_(651946, "r", lambda: r), "connect"), 'localhost', 28015)
_l_(651949)