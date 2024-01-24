# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53550866/multiprocessing-typeerror-cant-pickle-thread-lock-objects
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class class_one(_n_(530495, "object", lambda: object)):
    _l_(530534)

    def __init__(self):
        _l_(530504)

        _n_(530496, "self", lambda: self).var = {}
        _l_(530497)
        _n_(530498, "self", lambda: self).list = []
        _l_(530499)
        _c_(530502, _a_(530501, _n_(530500, "self", lambda: self), "get"))
        _l_(530503)
    def get_result(self, varam):
        _l_(530512)

        _c_(530510, _a_(530506, _n_(530505, "q", lambda: q), "put"), _c_(530509, _n_(530507, "A", lambda: A), _n_(530508, "varam", lambda: varam)))
        _l_(530511)
    def get(self):
        _l_(530533)

        for i in [6,7,8,9]:
            _l_(530524)

            _c_(530522, _a_(530515, _a_(530514, _n_(530513, "self", lambda: self), "list"), "append"), _c_(530521, _a_(530517, _n_(530516, "pool", lambda: pool), "apply_async"), _a_(530519, _n_(530518, "self", lambda: self), "get_result"), (_n_(530520, "i", lambda: i), )))
            _l_(530523)
        _c_(530527, _a_(530526, _n_(530525, "pool", lambda: pool), "close"))
        _l_(530528)
        _c_(530531, _a_(530530, _n_(530529, "pool", lambda: pool), "join"))
        _l_(530532)

if _n_(530535, "__name__", lambda: __name__) == '__main__':
    _l_(530553)

    _c_(530537, _n_(530536, "freeze_support", lambda: freeze_support))
    _l_(530538)
    process_num =2
    _l_(530539)
    process_list = []
    _l_(530540)
    g = _c_(530542, _n_(530541, "class_one", lambda: class_one))
    _l_(530543)

    for i in _a_(530545, _n_(530544, "g", lambda: g), "list"):
        _l_(530552)

        _c_(530550, _n_(530546, "print", lambda: print), _c_(530549, _a_(530548, _n_(530547, "i", lambda: i), "get")))
        _l_(530551)