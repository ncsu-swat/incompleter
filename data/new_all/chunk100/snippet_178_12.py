# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node(_n_(13140, "object", lambda: object)):
    _l_(13148)


    def __init__(self, data=None, next=None, prev=None):
        _l_(13147)

        _n_(13141, "self", lambda: self).next = _n_(13142, "next", lambda: next)
        _l_(13143)
        _n_(13144, "self", lambda: self).prev = _n_(13145, "prev", lambda: prev)
        _l_(13146)

class doubly_linked_list(_n_(13149, "object", lambda: object)):
    _l_(13208)


    def __init__(self):
        _l_(13156)

        _n_(13150, "self", lambda: self).head = None
        _l_(13151)
        _n_(13152, "self", lambda: self).tail = None
        _l_(13153)
        _n_(13154, "self", lambda: self).count = 0
        _l_(13155)

    def append_item(self, data):
        _l_(13184)

        new_item = _c_(13159, _n_(13157, "Node", lambda: Node), _n_(13158, "data", lambda: data), None, None)
        _l_(13160)
        if _a_(13162, _n_(13161, "self", lambda: self), "head") is None:
            _l_(13181)

            _n_(13163, "self", lambda: self).head = _n_(13164, "new_item", lambda: new_item)
            _l_(13165)
            _n_(13166, "self", lambda: self).tail = _a_(13168, _n_(13167, "self", lambda: self), "head")
            _l_(13169)
        else:
            _n_(13170, "new_item", lambda: new_item).prev = _a_(13172, _n_(13171, "self", lambda: self), "tail")
            _l_(13173)
            _a_(13175, _n_(13174, "self", lambda: self), "tail").next = _n_(13176, "new_item", lambda: new_item)
            _l_(13177)
            _n_(13178, "self", lambda: self).tail = _n_(13179, "new_item", lambda: new_item)
            _l_(13180)
        _n_(13182, "self", lambda: self).count += 1
        _l_(13183)

    def print_foward(self):
        _l_(13193)

        for node in _c_(13187, _a_(13186, _n_(13185, "self", lambda: self), "iter")):
            _l_(13192)

            _c_(13190, _n_(13188, "print", lambda: print), _n_(13189, "node", lambda: node))
            _l_(13191)

    def iter(self):
        _l_(13207)

        current = _a_(13195, _n_(13194, "self", lambda: self), "head")
        _l_(13196)
        while _n_(13197, "current", lambda: current):
            _l_(13206)

            item_val = _a_(13199, _n_(13198, "current", lambda: current), "data")
            _l_(13200)
            current = _a_(13202, _n_(13201, "current", lambda: current), "next")
            _l_(13203)
            yield _n_(13204, "item_val", lambda: item_val)
            _l_(13205)
items = _c_(13210, _n_(13209, "doubly_linked_list", lambda: doubly_linked_list))
_l_(13211)
_c_(13214, _a_(13213, _n_(13212, "items", lambda: items), "append_item"), 'PHP')
_l_(13215)
_c_(13218, _a_(13217, _n_(13216, "items", lambda: items), "append_item"), 'Python')
_l_(13219)
_c_(13222, _a_(13221, _n_(13220, "items", lambda: items), "append_item"), 'C#')
_l_(13223)
_c_(13226, _a_(13225, _n_(13224, "items", lambda: items), "append_item"), 'C++')
_l_(13227)
_c_(13230, _a_(13229, _n_(13228, "items", lambda: items), "append_item"), 'Java')
_l_(13231)
_c_(13233, _n_(13232, "print", lambda: print), 'Items in the Doubly linked list: ')
_l_(13234)
_c_(13237, _a_(13236, _n_(13235, "items", lambda: items), "print_foward"))
_l_(13238)