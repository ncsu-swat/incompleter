# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node(_n_(20354, "object", lambda: object)):
    _l_(20362)


    def __init__(self, data=None, next=None, prev=None):
        _l_(20361)

        _n_(20355, "self", lambda: self).data = _n_(20356, "data", lambda: data)
        _l_(20357)
        _n_(20358, "self", lambda: self).next = _n_(20359, "next", lambda: next)
        _l_(20360)

class doubly_linked_list(_n_(20363, "object", lambda: object)):
    _l_(20399)


    def __init__(self):
        _l_(20370)

        _n_(20364, "self", lambda: self).head = None
        _l_(20365)
        _n_(20366, "self", lambda: self).tail = None
        _l_(20367)
        _n_(20368, "self", lambda: self).count = 0
        _l_(20369)

    def append_item(self, data):
        _l_(20398)

        new_item = _c_(20373, _n_(20371, "Node", lambda: Node), _n_(20372, "data", lambda: data), None, None)
        _l_(20374)
        if _a_(20376, _n_(20375, "self", lambda: self), "head") is None:
            _l_(20395)

            _n_(20377, "self", lambda: self).head = _n_(20378, "new_item", lambda: new_item)
            _l_(20379)
            _n_(20380, "self", lambda: self).tail = _a_(20382, _n_(20381, "self", lambda: self), "head")
            _l_(20383)
        else:
            _n_(20384, "new_item", lambda: new_item).prev = _a_(20386, _n_(20385, "self", lambda: self), "tail")
            _l_(20387)
            _a_(20389, _n_(20388, "self", lambda: self), "tail").next = _n_(20390, "new_item", lambda: new_item)
            _l_(20391)
            _n_(20392, "self", lambda: self).tail = _n_(20393, "new_item", lambda: new_item)
            _l_(20394)
        _n_(20396, "self", lambda: self).count += 1
        _l_(20397)
items = _c_(20401, _n_(20400, "doubly_linked_list", lambda: doubly_linked_list))
_l_(20402)
_c_(20405, _a_(20404, _n_(20403, "items", lambda: items), "append_item"), 'PHP')
_l_(20406)
_c_(20409, _a_(20408, _n_(20407, "items", lambda: items), "append_item"), 'Python')
_l_(20410)
_c_(20413, _a_(20412, _n_(20411, "items", lambda: items), "append_item"), 'C#')
_l_(20414)
_c_(20417, _a_(20416, _n_(20415, "items", lambda: items), "append_item"), 'C++')
_l_(20418)
_c_(20421, _a_(20420, _n_(20419, "items", lambda: items), "append_item"), 'Java')
_l_(20422)
_c_(20425, _a_(20424, _n_(20423, "items", lambda: items), "append_item"), 'SQL')
_l_(20426)
_c_(20430, _n_(20427, "print", lambda: print), 'Number of items of the  Doubly linked list:', _a_(20429, _n_(20428, "items", lambda: items), "count"))
_l_(20431)