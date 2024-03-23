# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node:
    _l_(6690)


    def __init__(self, data=None):
        _l_(6689)

        _n_(6684, "self", lambda: self).data = _n_(6685, "data", lambda: data)
        _l_(6686)
        _n_(6687, "self", lambda: self).next = None
        _l_(6688)

class singly_linked_list:
    _l_(6766)


    def __init__(self):
        _l_(6695)

        _n_(6691, "self", lambda: self).head = None
        _l_(6692)
        _n_(6693, "self", lambda: self).count = 0
        _l_(6694)

    def append_item(self, data):
        _l_(6718)

        node = _c_(6698, _n_(6696, "Node", lambda: Node), _n_(6697, "data", lambda: data))
        _l_(6699)
        if _a_(6701, _n_(6700, "self", lambda: self), "head"):
            _l_(6715)

            _a_(6703, _n_(6702, "self", lambda: self), "head").next = _n_(6704, "node", lambda: node)
            _l_(6705)
            _n_(6706, "self", lambda: self).head = _n_(6707, "node", lambda: node)
            _l_(6708)
        else:
            _n_(6709, "self", lambda: self).tail = _n_(6710, "node", lambda: node)
            _l_(6711)
            _n_(6712, "self", lambda: self).head = _n_(6713, "node", lambda: node)
            _l_(6714)
        _n_(6716, "self", lambda: self).count += 1
        _l_(6717)

    def delete_item(self, data):
        _l_(6751)

        current = _a_(6720, _n_(6719, "self", lambda: self), "tail")
        _l_(6721)
        prev = _a_(6723, _n_(6722, "self", lambda: self), "tail")
        _l_(6724)
        while _n_(6725, "current", lambda: current):
            _l_(6750)

            if _a_(6727, _n_(6726, "current", lambda: current), "data") == _n_(6728, "data", lambda: data):
                _l_(6744)

                if _n_(6729, "current", lambda: current) == _a_(6731, _n_(6730, "self", lambda: self), "tail"):
                    _l_(6740)

                    _n_(6732, "self", lambda: self).tail = _a_(6734, _n_(6733, "current", lambda: current), "next")
                    _l_(6735)
                else:
                    _n_(6736, "prev", lambda: prev).next = _a_(6738, _n_(6737, "current", lambda: current), "next")
                    _l_(6739)
                _n_(6741, "self", lambda: self).count -= 1
                _l_(6742)
                aux = ""
                _l_(6743)
                return aux
            prev = _n_(6745, "current", lambda: current)
            _l_(6746)
            current = _a_(6748, _n_(6747, "current", lambda: current), "next")
            _l_(6749)

    def iterate_item(self):
        _l_(6765)

        current_item = _a_(6753, _n_(6752, "self", lambda: self), "tail")
        _l_(6754)
        while _n_(6755, "current_item", lambda: current_item):
            _l_(6764)

            val = _a_(6757, _n_(6756, "current_item", lambda: current_item), "data")
            _l_(6758)
            current_item = _a_(6760, _n_(6759, "current_item", lambda: current_item), "next")
            _l_(6761)
            yield _n_(6762, "val", lambda: val)
            _l_(6763)
items = _c_(6768, _n_(6767, "singly_linked_list", lambda: singly_linked_list))
_l_(6769)
_c_(6772, _a_(6771, _n_(6770, "items", lambda: items), "append_item"), 'PHP')
_l_(6773)
_c_(6776, _a_(6775, _n_(6774, "items", lambda: items), "append_item"), 'Python')
_l_(6777)
_c_(6780, _a_(6779, _n_(6778, "items", lambda: items), "append_item"), 'C#')
_l_(6781)
_c_(6784, _a_(6783, _n_(6782, "items", lambda: items), "append_item"), 'C++')
_l_(6785)
_c_(6788, _a_(6787, _n_(6786, "items", lambda: items), "append_item"), 'Java')
_l_(6789)
_c_(6791, _n_(6790, "print", lambda: print), 'Original list:')
_l_(6792)
for val in _c_(6795, _a_(6794, _n_(6793, "items", lambda: items), "iterate_item")):
    _l_(6800)

    _c_(6798, _n_(6796, "print", lambda: print), _n_(6797, "val", lambda: val))
    _l_(6799)
_c_(6802, _n_(6801, "print", lambda: print), '\nAfter removing the first item from the list:')
_l_(6803)
_c_(6806, _a_(6805, _n_(6804, "items", lambda: items), "delete_item"), 'PHP')
_l_(6807)
for val in _c_(6810, _a_(6809, _n_(6808, "items", lambda: items), "iterate_item")):
    _l_(6815)

    _c_(6813, _n_(6811, "print", lambda: print), _n_(6812, "val", lambda: val))
    _l_(6814)