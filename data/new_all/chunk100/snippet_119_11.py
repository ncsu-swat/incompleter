# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node:
    _l_(6559)


    def __init__(self, data=None):
        _l_(6558)

        _n_(6553, "self", lambda: self).data = _n_(6554, "data", lambda: data)
        _l_(6555)
        _n_(6556, "self", lambda: self).next = None
        _l_(6557)

class singly_linked_list:
    _l_(6634)


    def __init__(self):
        _l_(6566)

        _n_(6560, "self", lambda: self).tail = None
        _l_(6561)
        _n_(6562, "self", lambda: self).head = None
        _l_(6563)
        _n_(6564, "self", lambda: self).count = 0
        _l_(6565)

    def append_item(self, data):
        _l_(6589)

        node = _c_(6569, _n_(6567, "Node", lambda: Node), _n_(6568, "data", lambda: data))
        _l_(6570)
        if _a_(6572, _n_(6571, "self", lambda: self), "head"):
            _l_(6586)

            _a_(6574, _n_(6573, "self", lambda: self), "head").next = _n_(6575, "node", lambda: node)
            _l_(6576)
            _n_(6577, "self", lambda: self).head = _n_(6578, "node", lambda: node)
            _l_(6579)
        else:
            _n_(6580, "self", lambda: self).tail = _n_(6581, "node", lambda: node)
            _l_(6582)
            _n_(6583, "self", lambda: self).head = _n_(6584, "node", lambda: node)
            _l_(6585)
        _n_(6587, "self", lambda: self).count += 1
        _l_(6588)

    def delete_item(self, data):
        _l_(6619)

        prev = _a_(6591, _n_(6590, "self", lambda: self), "tail")
        _l_(6592)
        while _n_(6593, "current", lambda: current):
            _l_(6618)

            if _a_(6595, _n_(6594, "current", lambda: current), "data") == _n_(6596, "data", lambda: data):
                _l_(6612)

                if _n_(6597, "current", lambda: current) == _a_(6599, _n_(6598, "self", lambda: self), "tail"):
                    _l_(6608)

                    _n_(6600, "self", lambda: self).tail = _a_(6602, _n_(6601, "current", lambda: current), "next")
                    _l_(6603)
                else:
                    _n_(6604, "prev", lambda: prev).next = _a_(6606, _n_(6605, "current", lambda: current), "next")
                    _l_(6607)
                _n_(6609, "self", lambda: self).count -= 1
                _l_(6610)
                aux = ""
                _l_(6611)
                return aux
            prev = _n_(6613, "current", lambda: current)
            _l_(6614)
            current = _a_(6616, _n_(6615, "current", lambda: current), "next")
            _l_(6617)

    def iterate_item(self):
        _l_(6633)

        current_item = _a_(6621, _n_(6620, "self", lambda: self), "tail")
        _l_(6622)
        while _n_(6623, "current_item", lambda: current_item):
            _l_(6632)

            val = _a_(6625, _n_(6624, "current_item", lambda: current_item), "data")
            _l_(6626)
            current_item = _a_(6628, _n_(6627, "current_item", lambda: current_item), "next")
            _l_(6629)
            yield _n_(6630, "val", lambda: val)
            _l_(6631)
items = _c_(6636, _n_(6635, "singly_linked_list", lambda: singly_linked_list))
_l_(6637)
_c_(6640, _a_(6639, _n_(6638, "items", lambda: items), "append_item"), 'PHP')
_l_(6641)
_c_(6644, _a_(6643, _n_(6642, "items", lambda: items), "append_item"), 'Python')
_l_(6645)
_c_(6648, _a_(6647, _n_(6646, "items", lambda: items), "append_item"), 'C#')
_l_(6649)
_c_(6652, _a_(6651, _n_(6650, "items", lambda: items), "append_item"), 'C++')
_l_(6653)
_c_(6656, _a_(6655, _n_(6654, "items", lambda: items), "append_item"), 'Java')
_l_(6657)
_c_(6659, _n_(6658, "print", lambda: print), 'Original list:')
_l_(6660)
for val in _c_(6663, _a_(6662, _n_(6661, "items", lambda: items), "iterate_item")):
    _l_(6668)

    _c_(6666, _n_(6664, "print", lambda: print), _n_(6665, "val", lambda: val))
    _l_(6667)
_c_(6670, _n_(6669, "print", lambda: print), '\nAfter removing the first item from the list:')
_l_(6671)
_c_(6674, _a_(6673, _n_(6672, "items", lambda: items), "delete_item"), 'PHP')
_l_(6675)
for val in _c_(6678, _a_(6677, _n_(6676, "items", lambda: items), "iterate_item")):
    _l_(6683)

    _c_(6681, _n_(6679, "print", lambda: print), _n_(6680, "val", lambda: val))
    _l_(6682)