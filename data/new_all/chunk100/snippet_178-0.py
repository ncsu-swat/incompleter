# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node(_n_(103617, "object", lambda: object)):
    _l_(103628)


    def __init__(self, data=None, next=None, prev=None):
        _l_(103627)

        _n_(103618, "self", lambda: self).data = _n_(103619, "data", lambda: data)
        _l_(103620)
        _n_(103621, "self", lambda: self).next = _n_(103622, "next", lambda: next)
        _l_(103623)
        _n_(103624, "self", lambda: self).prev = _n_(103625, "prev", lambda: prev)
        _l_(103626)

class doubly_linked_list(_n_(103629, "object", lambda: object)):
    _l_(103688)


    def __init__(self):
        _l_(103636)

        _n_(103630, "self", lambda: self).head = None
        _l_(103631)
        _n_(103632, "self", lambda: self).tail = None
        _l_(103633)
        _n_(103634, "self", lambda: self).count = 0
        _l_(103635)

    def append_item(self, data):
        _l_(103664)

        new_item = _c_(103639, _n_(103637, "Node", lambda: Node), _n_(103638, "data", lambda: data), None, None)
        _l_(103640)
        if _a_(103642, _n_(103641, "self", lambda: self), "head") is None:
            _l_(103661)

            _n_(103643, "self", lambda: self).head = _n_(103644, "new_item", lambda: new_item)
            _l_(103645)
            _n_(103646, "self", lambda: self).tail = _a_(103648, _n_(103647, "self", lambda: self), "head")
            _l_(103649)
        else:
            _n_(103650, "new_item", lambda: new_item).prev = _a_(103652, _n_(103651, "self", lambda: self), "tail")
            _l_(103653)
            _a_(103655, _n_(103654, "self", lambda: self), "tail").next = _n_(103656, "new_item", lambda: new_item)
            _l_(103657)
            _n_(103658, "self", lambda: self).tail = _n_(103659, "new_item", lambda: new_item)
            _l_(103660)
        _n_(103662, "self", lambda: self).count += 1
        _l_(103663)

    def print_foward(self):
        _l_(103673)

        for node in _c_(103667, _a_(103666, _n_(103665, "self", lambda: self), "iter")):
            _l_(103672)

            _c_(103670, _n_(103668, "print", lambda: print), _n_(103669, "node", lambda: node))
            _l_(103671)

    def iter(self):
        _l_(103687)

        current = _a_(103675, _n_(103674, "self", lambda: self), "head")
        _l_(103676)
        while _n_(103677, "current", lambda: current):
            _l_(103686)

            item_val = _a_(103679, _n_(103678, "current", lambda: current), "data")
            _l_(103680)
            current = _a_(103682, _n_(103681, "current", lambda: current), "next")
            _l_(103683)
            yield _n_(103684, "item_val", lambda: item_val)
            _l_(103685)
_c_(103691, _a_(103690, _n_(103689, "items", lambda: items), "append_item"), 'PHP')
_l_(103692)
_c_(103695, _a_(103694, _n_(103693, "items", lambda: items), "append_item"), 'Python')
_l_(103696)
_c_(103699, _a_(103698, _n_(103697, "items", lambda: items), "append_item"), 'C#')
_l_(103700)
_c_(103703, _a_(103702, _n_(103701, "items", lambda: items), "append_item"), 'C++')
_l_(103704)
_c_(103707, _a_(103706, _n_(103705, "items", lambda: items), "append_item"), 'Java')
_l_(103708)
_c_(103710, _n_(103709, "print", lambda: print), 'Items in the Doubly linked list: ')
_l_(103711)
_c_(103714, _a_(103713, _n_(103712, "items", lambda: items), "print_foward"))
_l_(103715)