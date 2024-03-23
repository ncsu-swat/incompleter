# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node:
    _l_(90420)


    def __init__(self, data=None):
        _l_(90419)

        _n_(90414, "self", lambda: self).data = _n_(90415, "data", lambda: data)
        _l_(90416)
        _n_(90417, "self", lambda: self).next = None
        _l_(90418)

class singly_linked_list:
    _l_(90496)


    def __init__(self):
        _l_(90425)

        _n_(90421, "self", lambda: self).tail = None
        _l_(90422)
        _n_(90423, "self", lambda: self).count = 0
        _l_(90424)

    def append_item(self, data):
        _l_(90448)

        node = _c_(90428, _n_(90426, "Node", lambda: Node), _n_(90427, "data", lambda: data))
        _l_(90429)
        if _a_(90431, _n_(90430, "self", lambda: self), "head"):
            _l_(90445)

            _a_(90433, _n_(90432, "self", lambda: self), "head").next = _n_(90434, "node", lambda: node)
            _l_(90435)
            _n_(90436, "self", lambda: self).head = _n_(90437, "node", lambda: node)
            _l_(90438)
        else:
            _n_(90439, "self", lambda: self).tail = _n_(90440, "node", lambda: node)
            _l_(90441)
            _n_(90442, "self", lambda: self).head = _n_(90443, "node", lambda: node)
            _l_(90444)
        _n_(90446, "self", lambda: self).count += 1
        _l_(90447)

    def delete_item(self, data):
        _l_(90481)

        current = _a_(90450, _n_(90449, "self", lambda: self), "tail")
        _l_(90451)
        prev = _a_(90453, _n_(90452, "self", lambda: self), "tail")
        _l_(90454)
        while _n_(90455, "current", lambda: current):
            _l_(90480)

            if _a_(90457, _n_(90456, "current", lambda: current), "data") == _n_(90458, "data", lambda: data):
                _l_(90474)

                if _n_(90459, "current", lambda: current) == _a_(90461, _n_(90460, "self", lambda: self), "tail"):
                    _l_(90470)

                    _n_(90462, "self", lambda: self).tail = _a_(90464, _n_(90463, "current", lambda: current), "next")
                    _l_(90465)
                else:
                    _n_(90466, "prev", lambda: prev).next = _a_(90468, _n_(90467, "current", lambda: current), "next")
                    _l_(90469)
                _n_(90471, "self", lambda: self).count -= 1
                _l_(90472)
                aux = ""
                _l_(90473)
                return aux
            prev = _n_(90475, "current", lambda: current)
            _l_(90476)
            current = _a_(90478, _n_(90477, "current", lambda: current), "next")
            _l_(90479)

    def iterate_item(self):
        _l_(90495)

        current_item = _a_(90483, _n_(90482, "self", lambda: self), "tail")
        _l_(90484)
        while _n_(90485, "current_item", lambda: current_item):
            _l_(90494)

            val = _a_(90487, _n_(90486, "current_item", lambda: current_item), "data")
            _l_(90488)
            current_item = _a_(90490, _n_(90489, "current_item", lambda: current_item), "next")
            _l_(90491)
            yield _n_(90492, "val", lambda: val)
            _l_(90493)
items = _c_(90498, _n_(90497, "singly_linked_list", lambda: singly_linked_list))
_l_(90499)
_c_(90502, _a_(90501, _n_(90500, "items", lambda: items), "append_item"), 'PHP')
_l_(90503)
_c_(90506, _a_(90505, _n_(90504, "items", lambda: items), "append_item"), 'Python')
_l_(90507)
_c_(90510, _a_(90509, _n_(90508, "items", lambda: items), "append_item"), 'C#')
_l_(90511)
_c_(90514, _a_(90513, _n_(90512, "items", lambda: items), "append_item"), 'C++')
_l_(90515)
_c_(90518, _a_(90517, _n_(90516, "items", lambda: items), "append_item"), 'Java')
_l_(90519)
_c_(90521, _n_(90520, "print", lambda: print), 'Original list:')
_l_(90522)
for val in _c_(90525, _a_(90524, _n_(90523, "items", lambda: items), "iterate_item")):
    _l_(90530)

    _c_(90528, _n_(90526, "print", lambda: print), _n_(90527, "val", lambda: val))
    _l_(90529)
_c_(90532, _n_(90531, "print", lambda: print), '\nAfter removing the last item from the list:')
_l_(90533)
_c_(90536, _a_(90535, _n_(90534, "items", lambda: items), "delete_item"), 'Java')
_l_(90537)
for val in _c_(90540, _a_(90539, _n_(90538, "items", lambda: items), "iterate_item")):
    _l_(90545)

    _c_(90543, _n_(90541, "print", lambda: print), _n_(90542, "val", lambda: val))
    _l_(90544)