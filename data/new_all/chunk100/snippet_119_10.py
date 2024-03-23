# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node:
    _l_(6428)


    def __init__(self, data=None):
        _l_(6427)

        _n_(6422, "self", lambda: self).data = _n_(6423, "data", lambda: data)
        _l_(6424)
        _n_(6425, "self", lambda: self).next = None
        _l_(6426)

class singly_linked_list:
    _l_(6506)


    def __init__(self):
        _l_(6435)

        _n_(6429, "self", lambda: self).tail = None
        _l_(6430)
        _n_(6431, "self", lambda: self).head = None
        _l_(6432)
        _n_(6433, "self", lambda: self).count = 0
        _l_(6434)

    def append_item(self, data):
        _l_(6458)

        node = _c_(6438, _n_(6436, "Node", lambda: Node), _n_(6437, "data", lambda: data))
        _l_(6439)
        if _a_(6441, _n_(6440, "self", lambda: self), "head"):
            _l_(6455)

            _a_(6443, _n_(6442, "self", lambda: self), "head").next = _n_(6444, "node", lambda: node)
            _l_(6445)
            _n_(6446, "self", lambda: self).head = _n_(6447, "node", lambda: node)
            _l_(6448)
        else:
            _n_(6449, "self", lambda: self).tail = _n_(6450, "node", lambda: node)
            _l_(6451)
            _n_(6452, "self", lambda: self).head = _n_(6453, "node", lambda: node)
            _l_(6454)
        _n_(6456, "self", lambda: self).count += 1
        _l_(6457)

    def delete_item(self, data):
        _l_(6491)

        current = _a_(6460, _n_(6459, "self", lambda: self), "tail")
        _l_(6461)
        prev = _a_(6463, _n_(6462, "self", lambda: self), "tail")
        _l_(6464)
        while _n_(6465, "current", lambda: current):
            _l_(6490)

            if _a_(6467, _n_(6466, "current", lambda: current), "data") == _n_(6468, "data", lambda: data):
                _l_(6484)

                if _n_(6469, "current", lambda: current) == _a_(6471, _n_(6470, "self", lambda: self), "tail"):
                    _l_(6480)

                    _n_(6472, "self", lambda: self).tail = _a_(6474, _n_(6473, "current", lambda: current), "next")
                    _l_(6475)
                else:
                    _n_(6476, "prev", lambda: prev).next = _a_(6478, _n_(6477, "current", lambda: current), "next")
                    _l_(6479)
                _n_(6481, "self", lambda: self).count -= 1
                _l_(6482)
                aux = ""
                _l_(6483)
                return aux
            prev = _n_(6485, "current", lambda: current)
            _l_(6486)
            current = _a_(6488, _n_(6487, "current", lambda: current), "next")
            _l_(6489)

    def iterate_item(self):
        _l_(6505)

        current_item = _a_(6493, _n_(6492, "self", lambda: self), "tail")
        _l_(6494)
        while _n_(6495, "current_item", lambda: current_item):
            _l_(6504)

            val = _a_(6497, _n_(6496, "current_item", lambda: current_item), "data")
            _l_(6498)
            current_item = _a_(6500, _n_(6499, "current_item", lambda: current_item), "next")
            _l_(6501)
            yield _n_(6502, "val", lambda: val)
            _l_(6503)
_c_(6509, _a_(6508, _n_(6507, "items", lambda: items), "append_item"), 'PHP')
_l_(6510)
_c_(6513, _a_(6512, _n_(6511, "items", lambda: items), "append_item"), 'Python')
_l_(6514)
_c_(6517, _a_(6516, _n_(6515, "items", lambda: items), "append_item"), 'C#')
_l_(6518)
_c_(6521, _a_(6520, _n_(6519, "items", lambda: items), "append_item"), 'C++')
_l_(6522)
_c_(6525, _a_(6524, _n_(6523, "items", lambda: items), "append_item"), 'Java')
_l_(6526)
_c_(6528, _n_(6527, "print", lambda: print), 'Original list:')
_l_(6529)
for val in _c_(6532, _a_(6531, _n_(6530, "items", lambda: items), "iterate_item")):
    _l_(6537)

    _c_(6535, _n_(6533, "print", lambda: print), _n_(6534, "val", lambda: val))
    _l_(6536)
_c_(6539, _n_(6538, "print", lambda: print), '\nAfter removing the first item from the list:')
_l_(6540)
_c_(6543, _a_(6542, _n_(6541, "items", lambda: items), "delete_item"), 'PHP')
_l_(6544)
for val in _c_(6547, _a_(6546, _n_(6545, "items", lambda: items), "iterate_item")):
    _l_(6552)

    _c_(6550, _n_(6548, "print", lambda: print), _n_(6549, "val", lambda: val))
    _l_(6551)