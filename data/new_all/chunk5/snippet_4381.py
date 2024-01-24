# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58819446/attribute-error-join-object-has-no-attribute-implicit-returning
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(648723, _a_(648722, _n_(648721, "session", lambda: session), "begin"))
_l_(648724)
i = _c_(648728, _a_(648726, _n_(648725, "sqlalchemy", lambda: sqlalchemy), "insert"), _n_(648727, "Example", lambda: Example))
_l_(648729)
i = _c_(648732, _a_(648731, _n_(648730, "i", lambda: i), "values"), {'id': 1, 'startdate': 1570798620, 'enddate': 1572526620})
_l_(648733)
_c_(648737, _a_(648735, _n_(648734, "session", lambda: session), "execute"), _n_(648736, "i", lambda: i))
_l_(648738)
_c_(648741, _a_(648740, _n_(648739, "session", lambda: session), "commit"))
_l_(648742)