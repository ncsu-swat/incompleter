# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/46591205/accessing-an-objects-array-of-objects-attribute-gives-attribute-error-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Thing:
    _l_(381888)

    def __init__(self, attribute1='y', attribute2='n'):
        _l_(381884)

        _n_(381879, "self", lambda: self).attribute1, _n_(381880, "self", lambda: self).attribute2 = _n_(381881, "attribute1", lambda: attribute1), _n_(381882, "attribute2", lambda: attribute2)
        _l_(381883)
    def give_a_thing(self):
        _l_(381887)

        aux = _n_(381885, "self", lambda: self)
        _l_(381886)
        return aux

class ThingOfThings:
    _l_(381897)

    def __init__(self, items=[]):
        _l_(381892)

        _n_(381889, "self", lambda: self).items = _n_(381890, "items", lambda: items)
        _l_(381891)
    def get_thing(self, thing):
        _l_(381896)

        _n_(381893, "self", lambda: self).items += [_n_(381894, "thing", lambda: thing)]
        _l_(381895)

list_of_things = _c_(381899, _n_(381898, "ThingOfThings", lambda: ThingOfThings))
_l_(381900)

one_thing = _c_(381902, _n_(381901, "Thing", lambda: Thing))
_l_(381903)
for i in _c_(381905, _n_(381904, "range", lambda: range), 2):
    _l_(381912)

    _c_(381910, _a_(381907, _n_(381906, "list_of_things", lambda: list_of_things), "get_thing"), _a_(381909, _n_(381908, "one_thing", lambda: one_thing), "give_a_thing"))
    _l_(381911)
_c_(381917, _n_(381913, "print", lambda: print), _a_(381916, _a_(381915, _n_(381914, "list_of_things", lambda: list_of_things), "items")[0], "attribute1"))
_l_(381918)