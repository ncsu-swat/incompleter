# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node:
    _l_(89762)


    def __init__(self, data=None):
        _l_(89761)

        _n_(89759, "self", lambda: self).next = None
        _l_(89760)

class singly_linked_list:
    _l_(89840)


    def __init__(self):
        _l_(89769)

        _n_(89763, "self", lambda: self).tail = None
        _l_(89764)
        _n_(89765, "self", lambda: self).head = None
        _l_(89766)
        _n_(89767, "self", lambda: self).count = 0
        _l_(89768)

    def append_item(self, data):
        _l_(89792)

        node = _c_(89772, _n_(89770, "Node", lambda: Node), _n_(89771, "data", lambda: data))
        _l_(89773)
        if _a_(89775, _n_(89774, "self", lambda: self), "head"):
            _l_(89789)

            _a_(89777, _n_(89776, "self", lambda: self), "head").next = _n_(89778, "node", lambda: node)
            _l_(89779)
            _n_(89780, "self", lambda: self).head = _n_(89781, "node", lambda: node)
            _l_(89782)
        else:
            _n_(89783, "self", lambda: self).tail = _n_(89784, "node", lambda: node)
            _l_(89785)
            _n_(89786, "self", lambda: self).head = _n_(89787, "node", lambda: node)
            _l_(89788)
        _n_(89790, "self", lambda: self).count += 1
        _l_(89791)

    def delete_item(self, data):
        _l_(89825)

        current = _a_(89794, _n_(89793, "self", lambda: self), "tail")
        _l_(89795)
        prev = _a_(89797, _n_(89796, "self", lambda: self), "tail")
        _l_(89798)
        while _n_(89799, "current", lambda: current):
            _l_(89824)

            if _a_(89801, _n_(89800, "current", lambda: current), "data") == _n_(89802, "data", lambda: data):
                _l_(89818)

                if _n_(89803, "current", lambda: current) == _a_(89805, _n_(89804, "self", lambda: self), "tail"):
                    _l_(89814)

                    _n_(89806, "self", lambda: self).tail = _a_(89808, _n_(89807, "current", lambda: current), "next")
                    _l_(89809)
                else:
                    _n_(89810, "prev", lambda: prev).next = _a_(89812, _n_(89811, "current", lambda: current), "next")
                    _l_(89813)
                _n_(89815, "self", lambda: self).count -= 1
                _l_(89816)
                aux = ""
                _l_(89817)
                return aux
            prev = _n_(89819, "current", lambda: current)
            _l_(89820)
            current = _a_(89822, _n_(89821, "current", lambda: current), "next")
            _l_(89823)

    def iterate_item(self):
        _l_(89839)

        current_item = _a_(89827, _n_(89826, "self", lambda: self), "tail")
        _l_(89828)
        while _n_(89829, "current_item", lambda: current_item):
            _l_(89838)

            val = _a_(89831, _n_(89830, "current_item", lambda: current_item), "data")
            _l_(89832)
            current_item = _a_(89834, _n_(89833, "current_item", lambda: current_item), "next")
            _l_(89835)
            yield _n_(89836, "val", lambda: val)
            _l_(89837)
items = _c_(89842, _n_(89841, "singly_linked_list", lambda: singly_linked_list))
_l_(89843)
_c_(89846, _a_(89845, _n_(89844, "items", lambda: items), "append_item"), 'PHP')
_l_(89847)
_c_(89850, _a_(89849, _n_(89848, "items", lambda: items), "append_item"), 'Python')
_l_(89851)
_c_(89854, _a_(89853, _n_(89852, "items", lambda: items), "append_item"), 'C#')
_l_(89855)
_c_(89858, _a_(89857, _n_(89856, "items", lambda: items), "append_item"), 'C++')
_l_(89859)
_c_(89862, _a_(89861, _n_(89860, "items", lambda: items), "append_item"), 'Java')
_l_(89863)
_c_(89865, _n_(89864, "print", lambda: print), 'Original list:')
_l_(89866)
for val in _c_(89869, _a_(89868, _n_(89867, "items", lambda: items), "iterate_item")):
    _l_(89874)

    _c_(89872, _n_(89870, "print", lambda: print), _n_(89871, "val", lambda: val))
    _l_(89873)
_c_(89876, _n_(89875, "print", lambda: print), '\nAfter removing the last item from the list:')
_l_(89877)
_c_(89880, _a_(89879, _n_(89878, "items", lambda: items), "delete_item"), 'Java')
_l_(89881)
for val in _c_(89884, _a_(89883, _n_(89882, "items", lambda: items), "iterate_item")):
    _l_(89889)

    _c_(89887, _n_(89885, "print", lambda: print), _n_(89886, "val", lambda: val))
    _l_(89888)