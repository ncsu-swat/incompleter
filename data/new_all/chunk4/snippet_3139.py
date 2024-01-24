# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/41384654/python3-pymongo-typeerror-nonetype-object-is-not-subscriptable-within-cla
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from src.common.database import Database
    _l_(646488)

except ImportError:
    pass

class Admin(_n_(646489, "object", lambda: object)):
    _l_(646495)

    local_settings = _c_(646493, _a_(646491, _n_(646490, "Database", lambda: Database), "find_sort"), _a_(646492, AdminConstants, "COLLECTION"), "admin.created_date", -1, 1)
    _l_(646494)