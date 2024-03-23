# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node(_n_(23388, "object", lambda: object)):
    _l_(23396)


    def __init__(self, data=None, next=None, prev=None):
        _l_(23395)

        _n_(23389, "self", lambda: self).next = _n_(23390, "next", lambda: next)
        _l_(23391)
        _n_(23392, "self", lambda: self).prev = _n_(23393, "prev", lambda: prev)
        _l_(23394)

class doubly_linked_list(_n_(23397, "object", lambda: object)):
    _l_(23470)


    def __init__(self):
        _l_(23404)

        _n_(23398, "self", lambda: self).head = None
        _l_(23399)
        _n_(23400, "self", lambda: self).tail = None
        _l_(23401)
        _n_(23402, "self", lambda: self).count = 0
        _l_(23403)

    def append_item(self, data):
        _l_(23432)

        new_item = _c_(23407, _n_(23405, "Node", lambda: Node), _n_(23406, "data", lambda: data), None, None)
        _l_(23408)
        if _a_(23410, _n_(23409, "self", lambda: self), "head") is None:
            _l_(23429)

            _n_(23411, "self", lambda: self).head = _n_(23412, "new_item", lambda: new_item)
            _l_(23413)
            _n_(23414, "self", lambda: self).tail = _a_(23416, _n_(23415, "self", lambda: self), "head")
            _l_(23417)
        else:
            _n_(23418, "new_item", lambda: new_item).prev = _a_(23420, _n_(23419, "self", lambda: self), "tail")
            _l_(23421)
            _a_(23423, _n_(23422, "self", lambda: self), "tail").next = _n_(23424, "new_item", lambda: new_item)
            _l_(23425)
            _n_(23426, "self", lambda: self).tail = _n_(23427, "new_item", lambda: new_item)
            _l_(23428)
        _n_(23430, "self", lambda: self).count += 1
        _l_(23431)

    def print_foward(self):
        _l_(23441)

        for node in _c_(23435, _a_(23434, _n_(23433, "self", lambda: self), "iter")):
            _l_(23440)

            _c_(23438, _n_(23436, "print", lambda: print), _n_(23437, "node", lambda: node))
            _l_(23439)

    def print_backward(self):
        _l_(23455)

        current = _a_(23443, _n_(23442, "self", lambda: self), "tail")
        _l_(23444)
        while _n_(23445, "current", lambda: current):
            _l_(23454)

            _c_(23449, _n_(23446, "print", lambda: print), _a_(23448, _n_(23447, "current", lambda: current), "data"))
            _l_(23450)
            current = _a_(23452, _n_(23451, "current", lambda: current), "prev")
            _l_(23453)

    def iter(self):
        _l_(23469)

        current = _a_(23457, _n_(23456, "self", lambda: self), "head")
        _l_(23458)
        while _n_(23459, "current", lambda: current):
            _l_(23468)

            item_val = _a_(23461, _n_(23460, "current", lambda: current), "data")
            _l_(23462)
            current = _a_(23464, _n_(23463, "current", lambda: current), "next")
            _l_(23465)
            yield _n_(23466, "item_val", lambda: item_val)
            _l_(23467)
items = _c_(23472, _n_(23471, "doubly_linked_list", lambda: doubly_linked_list))
_l_(23473)
_c_(23476, _a_(23475, _n_(23474, "items", lambda: items), "append_item"), 'PHP')
_l_(23477)
_c_(23480, _a_(23479, _n_(23478, "items", lambda: items), "append_item"), 'Python')
_l_(23481)
_c_(23484, _a_(23483, _n_(23482, "items", lambda: items), "append_item"), 'C#')
_l_(23485)
_c_(23488, _a_(23487, _n_(23486, "items", lambda: items), "append_item"), 'C++')
_l_(23489)
_c_(23492, _a_(23491, _n_(23490, "items", lambda: items), "append_item"), 'Java')
_l_(23493)
_c_(23495, _n_(23494, "print", lambda: print), 'Print Items in the Doubly linked backwards:')
_l_(23496)
_c_(23499, _a_(23498, _n_(23497, "items", lambda: items), "print_backward"))
_l_(23500)