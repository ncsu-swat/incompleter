# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node:
    _l_(44821)


    def __init__(self, data=None):
        _l_(44820)

        _n_(44815, "self", lambda: self).data = _n_(44816, "data", lambda: data)
        _l_(44817)
        _n_(44818, "self", lambda: self).next = None
        _l_(44819)

class singly_linked_list:
    _l_(44890)


    def __init__(self):
        _l_(44826)

        _n_(44822, "self", lambda: self).head = None
        _l_(44823)
        _n_(44824, "self", lambda: self).count = 0
        _l_(44825)

    def append_item(self, data):
        _l_(44849)

        node = _c_(44829, _n_(44827, "Node", lambda: Node), _n_(44828, "data", lambda: data))
        _l_(44830)
        if _a_(44832, _n_(44831, "self", lambda: self), "head"):
            _l_(44846)

            _a_(44834, _n_(44833, "self", lambda: self), "head").next = _n_(44835, "node", lambda: node)
            _l_(44836)
            _n_(44837, "self", lambda: self).head = _n_(44838, "node", lambda: node)
            _l_(44839)
        else:
            _n_(44840, "self", lambda: self).tail = _n_(44841, "node", lambda: node)
            _l_(44842)
            _n_(44843, "self", lambda: self).head = _n_(44844, "node", lambda: node)
            _l_(44845)
        _n_(44847, "self", lambda: self).count += 1
        _l_(44848)

    def __getitem__(self, index):
        _l_(44868)

        if _n_(44850, "index", lambda: index) > _a_(44852, _n_(44851, "self", lambda: self), "count") - 1:
            _l_(44854)

            aux = 'Index out of range'
            _l_(44853)
            return aux
        current_val = _a_(44856, _n_(44855, "self", lambda: self), "tail")
        _l_(44857)
        for n in _c_(44860, _n_(44858, "range", lambda: range), _n_(44859, "index", lambda: index)):
            _l_(44864)

            current_val = _a_(44862, _n_(44861, "current_val", lambda: current_val), "next")
            _l_(44863)
        aux = _a_(44866, _n_(44865, "current_val", lambda: current_val), "data")
        _l_(44867)
        return aux

    def __setitem__(self, index, value):
        _l_(44889)

        if _n_(44869, "index", lambda: index) > _a_(44871, _n_(44870, "self", lambda: self), "count") - 1:
            _l_(44875)

            raise _c_(44873, _n_(44872, "Exception", lambda: Exception), 'Index out of range.')
            _l_(44874)
        current = _a_(44877, _n_(44876, "self", lambda: self), "tail")
        _l_(44878)
        for n in _c_(44881, _n_(44879, "range", lambda: range), _n_(44880, "index", lambda: index)):
            _l_(44885)

            current = _a_(44883, _n_(44882, "current", lambda: current), "next")
            _l_(44884)
        _n_(44886, "current", lambda: current).data = _n_(44887, "value", lambda: value)
        _l_(44888)
items = _c_(44892, _n_(44891, "singly_linked_list", lambda: singly_linked_list))
_l_(44893)
_c_(44896, _a_(44895, _n_(44894, "items", lambda: items), "append_item"), 'PHP')
_l_(44897)
_c_(44900, _a_(44899, _n_(44898, "items", lambda: items), "append_item"), 'Python')
_l_(44901)
_c_(44904, _a_(44903, _n_(44902, "items", lambda: items), "append_item"), 'C#')
_l_(44905)
_c_(44908, _a_(44907, _n_(44906, "items", lambda: items), "append_item"), 'C++')
_l_(44909)
_c_(44912, _a_(44911, _n_(44910, "items", lambda: items), "append_item"), 'Java')
_l_(44913)
_c_(44915, _n_(44914, "print", lambda: print), 'Modify items by index:')
_l_(44916)
_n_(44917, "items", lambda: items)[1] = 'SQL'
_l_(44918)
_c_(44921, _n_(44919, "print", lambda: print), 'New value: ', _n_(44920, "items", lambda: items)[1])
_l_(44922)
_n_(44923, "items", lambda: items)[4] = 'Perl'
_l_(44924)
_c_(44927, _n_(44925, "print", lambda: print), 'New value: ', _n_(44926, "items", lambda: items)[4])
_l_(44928)