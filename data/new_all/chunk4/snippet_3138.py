# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/41384654/python3-pymongo-typeerror-nonetype-object-is-not-subscriptable-within-cla
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pymongo
    _l_(631916)

except ImportError:
    pass
class Database(_n_(631917, "object", lambda: object)):
    _l_(631946)

    URI = "mongodb://127.0.0.1:27017"
    _l_(631918)
    DATABASE = None
    _l_(631919)

    @_n_(631920, "staticmethod", lambda: staticmethod)
    def initialize():
        _l_(631930)

        client = _c_(631925, _a_(631922, _n_(631921, "pymongo", lambda: pymongo), "MongoClient"), _a_(631924, _n_(631923, "Database", lambda: Database), "URI"))
        _l_(631926)
        _n_(631927, "Database", lambda: Database).DATABASE = _n_(631928, "client", lambda: client)['cvm']
        _l_(631929)

    @_n_(631931, "staticmethod", lambda: staticmethod)
    def find_sort(collection, query, direction, limit):
        _l_(631945)

        aux = _c_(631943, _a_(631941, _c_(631940, _a_(631937, _c_(631936, _a_(631935, _a_(631933, _n_(631932, "Database", lambda: Database), "DATABASE")[_n_(631934, "collection", lambda: collection)], "find"), {}), "sort"), _n_(631938, "query", lambda: query), _n_(631939, "direction", lambda: direction)), "limit"), _n_(631942, "limit", lambda: limit))
        _l_(631944)
        return aux