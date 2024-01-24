# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/52909401/mongo-client-typeerror-module-object-is-not-callable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pymongo
    _l_(540650)

except ImportError:
    pass
try:
    from pymongo import mongo_client
    _l_(540652)

except ImportError:
    pass
connection = _c_(540654, _n_(540653, "mongo_client", lambda: mongo_client))
_l_(540655)