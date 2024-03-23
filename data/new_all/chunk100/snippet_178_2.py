# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node(_n_(13339, "object", lambda: object)):
    _l_(13350)


    def __init__(self, data=None, next=None, prev=None):
        _l_(13349)

        _n_(13340, "self", lambda: self).data = _n_(13341, "data", lambda: data)
        _l_(13342)
        _n_(13343, "self", lambda: self).next = _n_(13344, "next", lambda: next)
        _l_(13345)
        _n_(13346, "self", lambda: self).prev = _n_(13347, "prev", lambda: prev)
        _l_(13348)

class doubly_linked_list(_n_(13351, "object", lambda: object)):
    _l_(13407)


    def __init__(self):
        _l_(13358)

        _n_(13352, "self", lambda: self).head = None
        _l_(13353)
        _n_(13354, "self", lambda: self).tail = None
        _l_(13355)
        _n_(13356, "self", lambda: self).count = 0
        _l_(13357)

    def append_item(self, data):
        _l_(13386)

        new_item = _c_(13361, _n_(13359, "Node", lambda: Node), _n_(13360, "data", lambda: data), None, None)
        _l_(13362)
        if _a_(13364, _n_(13363, "self", lambda: self), "head") is None:
            _l_(13383)

            _n_(13365, "self", lambda: self).head = _n_(13366, "new_item", lambda: new_item)
            _l_(13367)
            _n_(13368, "self", lambda: self).tail = _a_(13370, _n_(13369, "self", lambda: self), "head")
            _l_(13371)
        else:
            _n_(13372, "new_item", lambda: new_item).prev = _a_(13374, _n_(13373, "self", lambda: self), "tail")
            _l_(13375)
            _a_(13377, _n_(13376, "self", lambda: self), "tail").next = _n_(13378, "new_item", lambda: new_item)
            _l_(13379)
            _n_(13380, "self", lambda: self).tail = _n_(13381, "new_item", lambda: new_item)
            _l_(13382)
        _n_(13384, "self", lambda: self).count += 1
        _l_(13385)

    def print_foward(self):
        _l_(13395)

        for node in _c_(13389, _a_(13388, _n_(13387, "self", lambda: self), "iter")):
            _l_(13394)

            _c_(13392, _n_(13390, "print", lambda: print), _n_(13391, "node", lambda: node))
            _l_(13393)

    def iter(self):
        _l_(13406)

        current = _a_(13397, _n_(13396, "self", lambda: self), "head")
        _l_(13398)
        while _n_(13399, "current", lambda: current):
            _l_(13405)

            current = _a_(13401, _n_(13400, "current", lambda: current), "next")
            _l_(13402)
            yield _n_(13403, "item_val", lambda: item_val)
            _l_(13404)
items = _c_(13409, _n_(13408, "doubly_linked_list", lambda: doubly_linked_list))
_l_(13410)
_c_(13413, _a_(13412, _n_(13411, "items", lambda: items), "append_item"), 'PHP')
_l_(13414)
_c_(13417, _a_(13416, _n_(13415, "items", lambda: items), "append_item"), 'Python')
_l_(13418)
_c_(13421, _a_(13420, _n_(13419, "items", lambda: items), "append_item"), 'C#')
_l_(13422)
_c_(13425, _a_(13424, _n_(13423, "items", lambda: items), "append_item"), 'C++')
_l_(13426)
_c_(13429, _a_(13428, _n_(13427, "items", lambda: items), "append_item"), 'Java')
_l_(13430)
_c_(13432, _n_(13431, "print", lambda: print), 'Items in the Doubly linked list: ')
_l_(13433)
_c_(13436, _a_(13435, _n_(13434, "items", lambda: items), "print_foward"))
_l_(13437)