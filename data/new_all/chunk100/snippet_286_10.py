# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node(_n_(23275, "object", lambda: object)):
    _l_(23286)


    def __init__(self, data=None, next=None, prev=None):
        _l_(23285)

        _n_(23276, "self", lambda: self).data = _n_(23277, "data", lambda: data)
        _l_(23278)
        _n_(23279, "self", lambda: self).next = _n_(23280, "next", lambda: next)
        _l_(23281)
        _n_(23282, "self", lambda: self).prev = _n_(23283, "prev", lambda: prev)
        _l_(23284)

class doubly_linked_list(_n_(23287, "object", lambda: object)):
    _l_(23357)


    def __init__(self):
        _l_(23294)

        _n_(23288, "self", lambda: self).head = None
        _l_(23289)
        _n_(23290, "self", lambda: self).tail = None
        _l_(23291)
        _n_(23292, "self", lambda: self).count = 0
        _l_(23293)

    def append_item(self, data):
        _l_(23322)

        new_item = _c_(23297, _n_(23295, "Node", lambda: Node), _n_(23296, "data", lambda: data), None, None)
        _l_(23298)
        if _a_(23300, _n_(23299, "self", lambda: self), "head") is None:
            _l_(23319)

            _n_(23301, "self", lambda: self).head = _n_(23302, "new_item", lambda: new_item)
            _l_(23303)
            _n_(23304, "self", lambda: self).tail = _a_(23306, _n_(23305, "self", lambda: self), "head")
            _l_(23307)
        else:
            _n_(23308, "new_item", lambda: new_item).prev = _a_(23310, _n_(23309, "self", lambda: self), "tail")
            _l_(23311)
            _a_(23313, _n_(23312, "self", lambda: self), "tail").next = _n_(23314, "new_item", lambda: new_item)
            _l_(23315)
            _n_(23316, "self", lambda: self).tail = _n_(23317, "new_item", lambda: new_item)
            _l_(23318)
        _n_(23320, "self", lambda: self).count += 1
        _l_(23321)

    def print_foward(self):
        _l_(23331)

        for node in _c_(23325, _a_(23324, _n_(23323, "self", lambda: self), "iter")):
            _l_(23330)

            _c_(23328, _n_(23326, "print", lambda: print), _n_(23327, "node", lambda: node))
            _l_(23329)

    def print_backward(self):
        _l_(23342)

        while _n_(23332, "current", lambda: current):
            _l_(23341)

            _c_(23336, _n_(23333, "print", lambda: print), _a_(23335, _n_(23334, "current", lambda: current), "data"))
            _l_(23337)
            current = _a_(23339, _n_(23338, "current", lambda: current), "prev")
            _l_(23340)

    def iter(self):
        _l_(23356)

        current = _a_(23344, _n_(23343, "self", lambda: self), "head")
        _l_(23345)
        while _n_(23346, "current", lambda: current):
            _l_(23355)

            item_val = _a_(23348, _n_(23347, "current", lambda: current), "data")
            _l_(23349)
            current = _a_(23351, _n_(23350, "current", lambda: current), "next")
            _l_(23352)
            yield _n_(23353, "item_val", lambda: item_val)
            _l_(23354)
items = _c_(23359, _n_(23358, "doubly_linked_list", lambda: doubly_linked_list))
_l_(23360)
_c_(23363, _a_(23362, _n_(23361, "items", lambda: items), "append_item"), 'PHP')
_l_(23364)
_c_(23367, _a_(23366, _n_(23365, "items", lambda: items), "append_item"), 'Python')
_l_(23368)
_c_(23371, _a_(23370, _n_(23369, "items", lambda: items), "append_item"), 'C#')
_l_(23372)
_c_(23375, _a_(23374, _n_(23373, "items", lambda: items), "append_item"), 'C++')
_l_(23376)
_c_(23379, _a_(23378, _n_(23377, "items", lambda: items), "append_item"), 'Java')
_l_(23380)
_c_(23382, _n_(23381, "print", lambda: print), 'Print Items in the Doubly linked backwards:')
_l_(23383)
_c_(23386, _a_(23385, _n_(23384, "items", lambda: items), "print_backward"))
_l_(23387)