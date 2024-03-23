# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node(_n_(20275, "object", lambda: object)):
    _l_(20286)


    def __init__(self, data=None, next=None, prev=None):
        _l_(20285)

        _n_(20276, "self", lambda: self).data = _n_(20277, "data", lambda: data)
        _l_(20278)
        _n_(20279, "self", lambda: self).next = _n_(20280, "next", lambda: next)
        _l_(20281)
        _n_(20282, "self", lambda: self).prev = _n_(20283, "prev", lambda: prev)
        _l_(20284)

class doubly_linked_list(_n_(20287, "object", lambda: object)):
    _l_(20321)


    def __init__(self):
        _l_(20292)

        _n_(20288, "self", lambda: self).head = None
        _l_(20289)
        _n_(20290, "self", lambda: self).tail = None
        _l_(20291)

    def append_item(self, data):
        _l_(20320)

        new_item = _c_(20295, _n_(20293, "Node", lambda: Node), _n_(20294, "data", lambda: data), None, None)
        _l_(20296)
        if _a_(20298, _n_(20297, "self", lambda: self), "head") is None:
            _l_(20317)

            _n_(20299, "self", lambda: self).head = _n_(20300, "new_item", lambda: new_item)
            _l_(20301)
            _n_(20302, "self", lambda: self).tail = _a_(20304, _n_(20303, "self", lambda: self), "head")
            _l_(20305)
        else:
            _n_(20306, "new_item", lambda: new_item).prev = _a_(20308, _n_(20307, "self", lambda: self), "tail")
            _l_(20309)
            _a_(20311, _n_(20310, "self", lambda: self), "tail").next = _n_(20312, "new_item", lambda: new_item)
            _l_(20313)
            _n_(20314, "self", lambda: self).tail = _n_(20315, "new_item", lambda: new_item)
            _l_(20316)
        _n_(20318, "self", lambda: self).count += 1
        _l_(20319)
items = _c_(20323, _n_(20322, "doubly_linked_list", lambda: doubly_linked_list))
_l_(20324)
_c_(20327, _a_(20326, _n_(20325, "items", lambda: items), "append_item"), 'PHP')
_l_(20328)
_c_(20331, _a_(20330, _n_(20329, "items", lambda: items), "append_item"), 'Python')
_l_(20332)
_c_(20335, _a_(20334, _n_(20333, "items", lambda: items), "append_item"), 'C#')
_l_(20336)
_c_(20339, _a_(20338, _n_(20337, "items", lambda: items), "append_item"), 'C++')
_l_(20340)
_c_(20343, _a_(20342, _n_(20341, "items", lambda: items), "append_item"), 'Java')
_l_(20344)
_c_(20347, _a_(20346, _n_(20345, "items", lambda: items), "append_item"), 'SQL')
_l_(20348)
_c_(20352, _n_(20349, "print", lambda: print), 'Number of items of the  Doubly linked list:', _a_(20351, _n_(20350, "items", lambda: items), "count"))
_l_(20353)