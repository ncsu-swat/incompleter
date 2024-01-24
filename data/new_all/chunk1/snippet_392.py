# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57448210/typeerror-update-missing-1-required-positional-argument-document
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from pymongo import MongoClient
    _l_(381046)

except ImportError:
    pass
client = _c_(381048, _n_(381047, "MongoClient", lambda: MongoClient), "mongodb://localhost:27017/")
_l_(381049)
db = _a_(381051, _n_(381050, "client", lambda: client), "Mydb")
_l_(381052)
collection = _a_(381054, _n_(381053, "db", lambda: db), "sampledb")
_l_(381055)
new_contact = "6369723748"
_l_(381056)
updatestmt = "{\"ID\" : \"12345\"},{\"$set\" :{\"ID\" : \"67891\",\"Account_Number\" : \"1234 5678 9101\"}}"
_l_(381057)
_c_(381060, _n_(381058, "print", lambda: print), _n_(381059, "updatestmt", lambda: updatestmt))
_l_(381061)

cursor = _c_(381065, _a_(381063, _n_(381062, "collection", lambda: collection), "update"), _n_(381064, "updatestmt", lambda: updatestmt))
_l_(381066)
cursor1 = _c_(381069, _a_(381068, _n_(381067, "collection", lambda: collection), "find"))
_l_(381070)

for i in _n_(381071, "cursor1", lambda: cursor1):
    _l_(381076)

    _c_(381074, _n_(381072, "print", lambda: print), _n_(381073, "i", lambda: i))
    _l_(381075)