# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node:
    _l_(45727)


    def __init__(self, data=None):
        _l_(45726)

        _n_(45721, "self", lambda: self).data = _n_(45722, "data", lambda: data)
        _l_(45723)
        _n_(45724, "self", lambda: self).next = None
        _l_(45725)

class singly_linked_list:
    _l_(45795)


    def __init__(self):
        _l_(45734)

        _n_(45728, "self", lambda: self).tail = None
        _l_(45729)
        _n_(45730, "self", lambda: self).head = None
        _l_(45731)
        _n_(45732, "self", lambda: self).count = 0
        _l_(45733)

    def append_item(self, data):
        _l_(45757)

        node = _c_(45737, _n_(45735, "Node", lambda: Node), _n_(45736, "data", lambda: data))
        _l_(45738)
        if _a_(45740, _n_(45739, "self", lambda: self), "head"):
            _l_(45754)

            _a_(45742, _n_(45741, "self", lambda: self), "head").next = _n_(45743, "node", lambda: node)
            _l_(45744)
            _n_(45745, "self", lambda: self).head = _n_(45746, "node", lambda: node)
            _l_(45747)
        else:
            _n_(45748, "self", lambda: self).tail = _n_(45749, "node", lambda: node)
            _l_(45750)
            _n_(45751, "self", lambda: self).head = _n_(45752, "node", lambda: node)
            _l_(45753)
        _n_(45755, "self", lambda: self).count += 1
        _l_(45756)

    def __getitem__(self, index):
        _l_(45776)

        if _n_(45758, "index", lambda: index) > _a_(45760, _n_(45759, "self", lambda: self), "count") - 1:
            _l_(45762)

            aux = 'Index out of range'
            _l_(45761)
            return aux
        current_val = _a_(45764, _n_(45763, "self", lambda: self), "tail")
        _l_(45765)
        for n in _c_(45768, _n_(45766, "range", lambda: range), _n_(45767, "index", lambda: index)):
            _l_(45772)

            current_val = _a_(45770, _n_(45769, "current_val", lambda: current_val), "next")
            _l_(45771)
        aux = _a_(45774, _n_(45773, "current_val", lambda: current_val), "data")
        _l_(45775)
        return aux

    def __setitem__(self, index, value):
        _l_(45794)

        if _n_(45777, "index", lambda: index) > _a_(45779, _n_(45778, "self", lambda: self), "count") - 1:
            _l_(45783)

            raise _c_(45781, _n_(45780, "Exception", lambda: Exception), 'Index out of range.')
            _l_(45782)
        for n in _c_(45786, _n_(45784, "range", lambda: range), _n_(45785, "index", lambda: index)):
            _l_(45790)

            current = _a_(45788, _n_(45787, "current", lambda: current), "next")
            _l_(45789)
        _n_(45791, "current", lambda: current).data = _n_(45792, "value", lambda: value)
        _l_(45793)
items = _c_(45797, _n_(45796, "singly_linked_list", lambda: singly_linked_list))
_l_(45798)
_c_(45801, _a_(45800, _n_(45799, "items", lambda: items), "append_item"), 'PHP')
_l_(45802)
_c_(45805, _a_(45804, _n_(45803, "items", lambda: items), "append_item"), 'Python')
_l_(45806)
_c_(45809, _a_(45808, _n_(45807, "items", lambda: items), "append_item"), 'C#')
_l_(45810)
_c_(45813, _a_(45812, _n_(45811, "items", lambda: items), "append_item"), 'C++')
_l_(45814)
_c_(45817, _a_(45816, _n_(45815, "items", lambda: items), "append_item"), 'Java')
_l_(45818)
_c_(45820, _n_(45819, "print", lambda: print), 'Modify items by index:')
_l_(45821)
_n_(45822, "items", lambda: items)[1] = 'SQL'
_l_(45823)
_c_(45826, _n_(45824, "print", lambda: print), 'New value: ', _n_(45825, "items", lambda: items)[1])
_l_(45827)
_n_(45828, "items", lambda: items)[4] = 'Perl'
_l_(45829)
_c_(45832, _n_(45830, "print", lambda: print), 'New value: ', _n_(45831, "items", lambda: items)[4])
_l_(45833)