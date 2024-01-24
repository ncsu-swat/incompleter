# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58819446/attribute-error-join-object-has-no-attribute-implicit-returning
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(684201, _a_(684200, _n_(684199, "session", lambda: session), "begin"))
_l_(684202)
i = _c_(684206, _a_(684204, _n_(684203, "sqlalchemy", lambda: sqlalchemy), "insert"), _n_(684205, "Example", lambda: Example))
_l_(684207)
i = _c_(684210, _a_(684209, _n_(684208, "i", lambda: i), "values"), {'id': 1, 'startdate': 1570798620, 'enddate': 1572526620})
_l_(684211)
_c_(684215, _a_(684213, _n_(684212, "session", lambda: session), "execute"), _n_(684214, "i", lambda: i))
_l_(684216)
_c_(684219, _a_(684218, _n_(684217, "session", lambda: session), "commit"))
_l_(684220)