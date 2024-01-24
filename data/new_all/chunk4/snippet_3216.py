# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/77313190/filtering-pymongo-list-collection-names-throws-type-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
myclient = _c_(609219, _a_(609218, _n_(609217, "pymongo", lambda: pymongo), "MongoClient"), 'x.x.x.x', username='xxxxxx', 
            password='yyyyyyy', authSource='zzzz', authMechanism='SCRAM-SHA-256')
_l_(609220)
mydb = _n_(609221, "myclient", lambda: myclient)["db"]    
_l_(609222)    
filter = {"name": {"$regex": r"^(?!system\.)"}}
_l_(609223)
collection = _c_(609227, _a_(609225, _n_(609224, "mydb", lambda: mydb), "list_collection_names"), filter=_n_(609226, "filter", lambda: filter))
_l_(609228)
_c_(609231, _a_(609230, _n_(609229, "collection", lambda: collection), "sort"))
_l_(609232)
filtered_names = _c_(609238, _n_(609233, "list", lambda: list), _c_(609237, _n_(609234, "filter", lambda: filter), lambda x: "test" in _n_(609235, "x", lambda: x), _n_(609236, "collection", lambda: collection) ))
_l_(609239)