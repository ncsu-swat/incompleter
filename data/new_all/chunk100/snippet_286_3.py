# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node(_n_(23727, "object", lambda: object)):
    _l_(23738)


    def __init__(self, data=None, next=None, prev=None):
        _l_(23737)

        _n_(23728, "self", lambda: self).data = _n_(23729, "data", lambda: data)
        _l_(23730)
        _n_(23731, "self", lambda: self).next = _n_(23732, "next", lambda: next)
        _l_(23733)
        _n_(23734, "self", lambda: self).prev = _n_(23735, "prev", lambda: prev)
        _l_(23736)

class doubly_linked_list(_n_(23739, "object", lambda: object)):
    _l_(23809)


    def __init__(self):
        _l_(23746)

        _n_(23740, "self", lambda: self).head = None
        _l_(23741)
        _n_(23742, "self", lambda: self).tail = None
        _l_(23743)
        _n_(23744, "self", lambda: self).count = 0
        _l_(23745)

    def append_item(self, data):
        _l_(23771)

        new_item = _c_(23749, _n_(23747, "Node", lambda: Node), _n_(23748, "data", lambda: data), None, None)
        _l_(23750)
        if _a_(23752, _n_(23751, "self", lambda: self), "head") is None:
            _l_(23768)

            _n_(23753, "self", lambda: self).tail = _a_(23755, _n_(23754, "self", lambda: self), "head")
            _l_(23756)
        else:
            _n_(23757, "new_item", lambda: new_item).prev = _a_(23759, _n_(23758, "self", lambda: self), "tail")
            _l_(23760)
            _a_(23762, _n_(23761, "self", lambda: self), "tail").next = _n_(23763, "new_item", lambda: new_item)
            _l_(23764)
            _n_(23765, "self", lambda: self).tail = _n_(23766, "new_item", lambda: new_item)
            _l_(23767)
        _n_(23769, "self", lambda: self).count += 1
        _l_(23770)

    def print_foward(self):
        _l_(23780)

        for node in _c_(23774, _a_(23773, _n_(23772, "self", lambda: self), "iter")):
            _l_(23779)

            _c_(23777, _n_(23775, "print", lambda: print), _n_(23776, "node", lambda: node))
            _l_(23778)

    def print_backward(self):
        _l_(23794)

        current = _a_(23782, _n_(23781, "self", lambda: self), "tail")
        _l_(23783)
        while _n_(23784, "current", lambda: current):
            _l_(23793)

            _c_(23788, _n_(23785, "print", lambda: print), _a_(23787, _n_(23786, "current", lambda: current), "data"))
            _l_(23789)
            current = _a_(23791, _n_(23790, "current", lambda: current), "prev")
            _l_(23792)

    def iter(self):
        _l_(23808)

        current = _a_(23796, _n_(23795, "self", lambda: self), "head")
        _l_(23797)
        while _n_(23798, "current", lambda: current):
            _l_(23807)

            item_val = _a_(23800, _n_(23799, "current", lambda: current), "data")
            _l_(23801)
            current = _a_(23803, _n_(23802, "current", lambda: current), "next")
            _l_(23804)
            yield _n_(23805, "item_val", lambda: item_val)
            _l_(23806)
items = _c_(23811, _n_(23810, "doubly_linked_list", lambda: doubly_linked_list))
_l_(23812)
_c_(23815, _a_(23814, _n_(23813, "items", lambda: items), "append_item"), 'PHP')
_l_(23816)
_c_(23819, _a_(23818, _n_(23817, "items", lambda: items), "append_item"), 'Python')
_l_(23820)
_c_(23823, _a_(23822, _n_(23821, "items", lambda: items), "append_item"), 'C#')
_l_(23824)
_c_(23827, _a_(23826, _n_(23825, "items", lambda: items), "append_item"), 'C++')
_l_(23828)
_c_(23831, _a_(23830, _n_(23829, "items", lambda: items), "append_item"), 'Java')
_l_(23832)
_c_(23834, _n_(23833, "print", lambda: print), 'Print Items in the Doubly linked backwards:')
_l_(23835)
_c_(23838, _a_(23837, _n_(23836, "items", lambda: items), "print_backward"))
_l_(23839)