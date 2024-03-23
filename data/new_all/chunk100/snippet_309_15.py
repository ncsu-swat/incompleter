# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node(_n_(27749, "object", lambda: object)):
    _l_(27760)


    def __init__(self, value=None, next=None, prev=None):
        _l_(27759)

        _n_(27750, "self", lambda: self).value = _n_(27751, "value", lambda: value)
        _l_(27752)
        _n_(27753, "self", lambda: self).next = _n_(27754, "next", lambda: next)
        _l_(27755)
        _n_(27756, "self", lambda: self).prev = _n_(27757, "prev", lambda: prev)
        _l_(27758)

class doubly_linked_list(_n_(27761, "object", lambda: object)):
    _l_(27886)


    def __init__(self):
        _l_(27766)

        _n_(27762, "self", lambda: self).head = None
        _l_(27763)
        _n_(27764, "self", lambda: self).count = 0
        _l_(27765)

    def append_item(self, value):
        _l_(27794)

        new_item = _c_(27769, _n_(27767, "Node", lambda: Node), _n_(27768, "value", lambda: value), None, None)
        _l_(27770)
        if _a_(27772, _n_(27771, "self", lambda: self), "head") is None:
            _l_(27791)

            _n_(27773, "self", lambda: self).head = _n_(27774, "new_item", lambda: new_item)
            _l_(27775)
            _n_(27776, "self", lambda: self).tail = _a_(27778, _n_(27777, "self", lambda: self), "head")
            _l_(27779)
        else:
            _n_(27780, "new_item", lambda: new_item).prev = _a_(27782, _n_(27781, "self", lambda: self), "tail")
            _l_(27783)
            _a_(27785, _n_(27784, "self", lambda: self), "tail").next = _n_(27786, "new_item", lambda: new_item)
            _l_(27787)
            _n_(27788, "self", lambda: self).tail = _n_(27789, "new_item", lambda: new_item)
            _l_(27790)
        _n_(27792, "self", lambda: self).count += 1
        _l_(27793)

    def iter(self):
        _l_(27808)

        current = _a_(27796, _n_(27795, "self", lambda: self), "head")
        _l_(27797)
        while _n_(27798, "current", lambda: current):
            _l_(27807)

            item_val = _a_(27800, _n_(27799, "current", lambda: current), "value")
            _l_(27801)
            current = _a_(27803, _n_(27802, "current", lambda: current), "next")
            _l_(27804)
            yield _n_(27805, "item_val", lambda: item_val)
            _l_(27806)

    def print_foward(self):
        _l_(27817)

        for node in _c_(27811, _a_(27810, _n_(27809, "self", lambda: self), "iter")):
            _l_(27816)

            _c_(27814, _n_(27812, "print", lambda: print), _n_(27813, "node", lambda: node))
            _l_(27815)

    def search_item(self, val):
        _l_(27827)

        for node in _c_(27820, _a_(27819, _n_(27818, "self", lambda: self), "iter")):
            _l_(27825)

            if _n_(27821, "val", lambda: val) == _n_(27822, "node", lambda: node):
                _l_(27824)

                aux = True
                _l_(27823)
                return aux
        aux = False
        _l_(27826)
        return aux

    def delete(self, value):
        _l_(27885)

        current = _a_(27829, _n_(27828, "self", lambda: self), "head")
        _l_(27830)
        node_deleted = False
        _l_(27831)
        if _n_(27832, "current", lambda: current) is None:
            _l_(27880)

            node_deleted = False
            _l_(27833)
        elif _a_(27835, _n_(27834, "current", lambda: current), "value") == _n_(27836, "value", lambda: value):
            _l_(27879)

            _n_(27837, "self", lambda: self).head = _a_(27839, _n_(27838, "current", lambda: current), "next")
            _l_(27840)
            _a_(27842, _n_(27841, "self", lambda: self), "head").prev = None
            _l_(27843)
            node_deleted = True
            _l_(27844)
        elif _a_(27847, _a_(27846, _n_(27845, "self", lambda: self), "tail"), "value") == _n_(27848, "value", lambda: value):
            _l_(27878)

            _n_(27849, "self", lambda: self).tail = _a_(27852, _a_(27851, _n_(27850, "self", lambda: self), "tail"), "prev")
            _l_(27853)
            _a_(27855, _n_(27854, "self", lambda: self), "tail").next = None
            _l_(27856)
            node_deleted = True
            _l_(27857)
        else:
            while _n_(27858, "current", lambda: current):
                _l_(27877)

                if _a_(27860, _n_(27859, "current", lambda: current), "value") == _n_(27861, "value", lambda: value):
                    _l_(27873)

                    _a_(27863, _n_(27862, "current", lambda: current), "prev").next = _a_(27865, _n_(27864, "current", lambda: current), "next")
                    _l_(27866)
                    _a_(27868, _n_(27867, "current", lambda: current), "next").prev = _a_(27870, _n_(27869, "current", lambda: current), "prev")
                    _l_(27871)
                    node_deleted = True
                    _l_(27872)
                current = _a_(27875, _n_(27874, "current", lambda: current), "next")
                _l_(27876)
        if _n_(27881, "node_deleted", lambda: node_deleted):
            _l_(27884)

            _n_(27882, "self", lambda: self).count -= 1
            _l_(27883)
items = _c_(27888, _n_(27887, "doubly_linked_list", lambda: doubly_linked_list))
_l_(27889)
_c_(27892, _a_(27891, _n_(27890, "items", lambda: items), "append_item"), 'PHP')
_l_(27893)
_c_(27896, _a_(27895, _n_(27894, "items", lambda: items), "append_item"), 'Python')
_l_(27897)
_c_(27900, _a_(27899, _n_(27898, "items", lambda: items), "append_item"), 'C#')
_l_(27901)
_c_(27904, _a_(27903, _n_(27902, "items", lambda: items), "append_item"), 'C++')
_l_(27905)
_c_(27908, _a_(27907, _n_(27906, "items", lambda: items), "append_item"), 'Java')
_l_(27909)
_c_(27912, _a_(27911, _n_(27910, "items", lambda: items), "append_item"), 'SQL')
_l_(27913)
_c_(27915, _n_(27914, "print", lambda: print), 'Original list:')
_l_(27916)
_c_(27919, _a_(27918, _n_(27917, "items", lambda: items), "print_foward"))
_l_(27920)
_c_(27923, _a_(27922, _n_(27921, "items", lambda: items), "delete"), 'Java')
_l_(27924)
_c_(27927, _a_(27926, _n_(27925, "items", lambda: items), "delete"), 'Python')
_l_(27928)
_c_(27930, _n_(27929, "print", lambda: print), '\nList after deleting two items:')
_l_(27931)
_c_(27934, _a_(27933, _n_(27932, "items", lambda: items), "print_foward"))
_l_(27935)