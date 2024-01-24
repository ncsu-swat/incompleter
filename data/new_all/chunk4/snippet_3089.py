# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/47732146/python-3-inheritance-attributeerror-how-to-solve-it
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class AttackDB(_n_(588532, "MongoData", lambda: MongoData)):
    _l_(588558)

    __metaclass__  = _a_(588533, abc, "ABCMeta")
    _l_(588534)

    def __init__(self, db_name, coll_name):
        _l_(588542)

        _c_(588540, _a_(588536, _n_(588535, "MongoData", lambda: MongoData), "__init__"), _n_(588537, "self", lambda: self), _n_(588538, "db_name", lambda: db_name), _n_(588539, "coll_name", lambda: coll_name))
        _l_(588541)

    @_a_(588543, abc, "abstractmethod")
    def writeDB(self, wdict):
        _l_(588557)

        doc_id = _a_(588549, _c_(588548, _a_(588546, _a_(588545, _n_(588544, "self", lambda: self), "__coll"), "insert_one"), _n_(588547, "attack", lambda: attack)), "inserted_id")
        _l_(588550)
        _c_(588555, _n_(588551, "print", lambda: print), _c_(588554, _a_(588552, "Attack with id {} was inserted in the DB.", "format"), _n_(588553, "dic_id", lambda: dic_id)))
        _l_(588556)