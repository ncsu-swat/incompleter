# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node(_n_(13832, "object", lambda: object)):
    _l_(13843)


    def __init__(self, data=None, next=None, prev=None):
        _l_(13842)

        _n_(13833, "self", lambda: self).data = _n_(13834, "data", lambda: data)
        _l_(13835)
        _n_(13836, "self", lambda: self).next = _n_(13837, "next", lambda: next)
        _l_(13838)
        _n_(13839, "self", lambda: self).prev = _n_(13840, "prev", lambda: prev)
        _l_(13841)

class doubly_linked_list(_n_(13844, "object", lambda: object)):
    _l_(13903)


    def __init__(self):
        _l_(13851)

        _n_(13845, "self", lambda: self).head = None
        _l_(13846)
        _n_(13847, "self", lambda: self).tail = None
        _l_(13848)
        _n_(13849, "self", lambda: self).count = 0
        _l_(13850)

    def append_item(self, data):
        _l_(13879)

        new_item = _c_(13854, _n_(13852, "Node", lambda: Node), _n_(13853, "data", lambda: data), None, None)
        _l_(13855)
        if _a_(13857, _n_(13856, "self", lambda: self), "head") is None:
            _l_(13876)

            _n_(13858, "self", lambda: self).head = _n_(13859, "new_item", lambda: new_item)
            _l_(13860)
            _n_(13861, "self", lambda: self).tail = _a_(13863, _n_(13862, "self", lambda: self), "head")
            _l_(13864)
        else:
            _n_(13865, "new_item", lambda: new_item).prev = _a_(13867, _n_(13866, "self", lambda: self), "tail")
            _l_(13868)
            _a_(13870, _n_(13869, "self", lambda: self), "tail").next = _n_(13871, "new_item", lambda: new_item)
            _l_(13872)
            _n_(13873, "self", lambda: self).tail = _n_(13874, "new_item", lambda: new_item)
            _l_(13875)
        _n_(13877, "self", lambda: self).count += 1
        _l_(13878)

    def print_foward(self):
        _l_(13888)

        for node in _c_(13882, _a_(13881, _n_(13880, "self", lambda: self), "iter")):
            _l_(13887)

            _c_(13885, _n_(13883, "print", lambda: print), _n_(13884, "node", lambda: node))
            _l_(13886)

    def iter(self):
        _l_(13902)

        current = _a_(13890, _n_(13889, "self", lambda: self), "head")
        _l_(13891)
        while _n_(13892, "current", lambda: current):
            _l_(13901)

            item_val = _a_(13894, _n_(13893, "current", lambda: current), "data")
            _l_(13895)
            current = _a_(13897, _n_(13896, "current", lambda: current), "next")
            _l_(13898)
            yield _n_(13899, "item_val", lambda: item_val)
            _l_(13900)
_c_(13906, _a_(13905, _n_(13904, "items", lambda: items), "append_item"), 'PHP')
_l_(13907)
_c_(13910, _a_(13909, _n_(13908, "items", lambda: items), "append_item"), 'Python')
_l_(13911)
_c_(13914, _a_(13913, _n_(13912, "items", lambda: items), "append_item"), 'C#')
_l_(13915)
_c_(13918, _a_(13917, _n_(13916, "items", lambda: items), "append_item"), 'C++')
_l_(13919)
_c_(13922, _a_(13921, _n_(13920, "items", lambda: items), "append_item"), 'Java')
_l_(13923)
_c_(13925, _n_(13924, "print", lambda: print), 'Items in the Doubly linked list: ')
_l_(13926)
_c_(13929, _a_(13928, _n_(13927, "items", lambda: items), "print_foward"))
_l_(13930)