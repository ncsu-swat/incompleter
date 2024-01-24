# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/42098053/typeerror-object-takes-no-parameters-in-python-3-x
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Media:
    _l_(693446)

    _id = None
    _l_(693411)
    _taken_time = None
    _l_(693412)

    def __init__(self, id=None, taken_time=None):
        _l_(693419)

        _n_(693413, "self", lambda: self)._id = _n_(693414, "id", lambda: id)
        _l_(693415)
        _n_(693416, "self", lambda: self)._taken_time = _n_(693417, "taken_time", lambda: taken_time)
        _l_(693418)

    @_n_(693420, "property", lambda: property)
    def id(self):
        _l_(693424)

        aux = _a_(693422, _n_(693421, "self", lambda: self), "_id")
        _l_(693423)
        return aux

    @_a_(693425, yguid, "setter")
    def id(self, value):
        _l_(693429)

        _n_(693426, "self", lambda: self)._id = _n_(693427, "value", lambda: value)
        _l_(693428)

    @_n_(693430, "property", lambda: property)
    def taken_time(self):
        _l_(693434)

        aux = _a_(693432, _n_(693431, "self", lambda: self), "_taken_time")
        _l_(693433)
        return aux

    @_a_(693435, taken_time, "setter")
    def taken_time(self, value):
        _l_(693439)

        _n_(693436, "self", lambda: self)._taken_time = _n_(693437, "value", lambda: value)
        _l_(693438)

    def serialize(self):
        _l_(693445)

        aux = {
            "id": _a_(693441, _n_(693440, "self", lambda: self), "_id"),
            "taken_time": _a_(693443, _n_(693442, "self", lambda: self), "_taken_time")
        }
        _l_(693444)
        return aux