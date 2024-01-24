# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/33251130/python-3-import-typeerror-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from myproject.app import db
    _l_(546822)

except ImportError:
    pass
try:
    from myproject.models.enum import DeclEnum
    _l_(546824)

except ImportError:
    pass

class Weekday(_n_(546825, "DeclEnum", lambda: DeclEnum)):
    _l_(546833)

    Sunday    = 'Sunday', {'offset': 0}
    _l_(546826)
    Monday    = 'Monday', {'offset': 1}
    _l_(546827)
    Tuesday   = 'Tuesday', {'offset': 2}
    _l_(546828)
    Wednesday = 'Wednesday', {'offset': 3}
    _l_(546829)
    Thursday  = 'Thursday', {'offset': 4}
    _l_(546830)
    Friday    = 'Friday', {'offset': 5}
    _l_(546831)
    Saturday  = 'Saturday', {'offset': 6}
    _l_(546832)

weekday_type = _c_(546838, _a_(546835, _n_(546834, "Weekday", lambda: Weekday), "db_type"), metadata=_a_(546837, _n_(546836, "db", lambda: db), "metadata"))
_l_(546839)
_c_(546844, _a_(546841, _n_(546840, "weekday_type", lambda: weekday_type), "register_with_psycopg"), _a_(546843, _n_(546842, "db", lambda: db), "engine"))
_l_(546845)