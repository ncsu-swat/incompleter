# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node(_n_(12743, "object", lambda: object)):
    _l_(12754)


    def __init__(self, data=None, next=None, prev=None):
        _l_(12753)

        _n_(12744, "self", lambda: self).data = _n_(12745, "data", lambda: data)
        _l_(12746)
        _n_(12747, "self", lambda: self).next = _n_(12748, "next", lambda: next)
        _l_(12749)
        _n_(12750, "self", lambda: self).prev = _n_(12751, "prev", lambda: prev)
        _l_(12752)

class doubly_linked_list(_n_(12755, "object", lambda: object)):
    _l_(12812)


    def __init__(self):
        _l_(12760)

        _n_(12756, "self", lambda: self).head = None
        _l_(12757)
        _n_(12758, "self", lambda: self).tail = None
        _l_(12759)

    def append_item(self, data):
        _l_(12788)

        new_item = _c_(12763, _n_(12761, "Node", lambda: Node), _n_(12762, "data", lambda: data), None, None)
        _l_(12764)
        if _a_(12766, _n_(12765, "self", lambda: self), "head") is None:
            _l_(12785)

            _n_(12767, "self", lambda: self).head = _n_(12768, "new_item", lambda: new_item)
            _l_(12769)
            _n_(12770, "self", lambda: self).tail = _a_(12772, _n_(12771, "self", lambda: self), "head")
            _l_(12773)
        else:
            _n_(12774, "new_item", lambda: new_item).prev = _a_(12776, _n_(12775, "self", lambda: self), "tail")
            _l_(12777)
            _a_(12779, _n_(12778, "self", lambda: self), "tail").next = _n_(12780, "new_item", lambda: new_item)
            _l_(12781)
            _n_(12782, "self", lambda: self).tail = _n_(12783, "new_item", lambda: new_item)
            _l_(12784)
        _n_(12786, "self", lambda: self).count += 1
        _l_(12787)

    def print_foward(self):
        _l_(12797)

        for node in _c_(12791, _a_(12790, _n_(12789, "self", lambda: self), "iter")):
            _l_(12796)

            _c_(12794, _n_(12792, "print", lambda: print), _n_(12793, "node", lambda: node))
            _l_(12795)

    def iter(self):
        _l_(12811)

        current = _a_(12799, _n_(12798, "self", lambda: self), "head")
        _l_(12800)
        while _n_(12801, "current", lambda: current):
            _l_(12810)

            item_val = _a_(12803, _n_(12802, "current", lambda: current), "data")
            _l_(12804)
            current = _a_(12806, _n_(12805, "current", lambda: current), "next")
            _l_(12807)
            yield _n_(12808, "item_val", lambda: item_val)
            _l_(12809)
items = _c_(12814, _n_(12813, "doubly_linked_list", lambda: doubly_linked_list))
_l_(12815)
_c_(12818, _a_(12817, _n_(12816, "items", lambda: items), "append_item"), 'PHP')
_l_(12819)
_c_(12822, _a_(12821, _n_(12820, "items", lambda: items), "append_item"), 'Python')
_l_(12823)
_c_(12826, _a_(12825, _n_(12824, "items", lambda: items), "append_item"), 'C#')
_l_(12827)
_c_(12830, _a_(12829, _n_(12828, "items", lambda: items), "append_item"), 'C++')
_l_(12831)
_c_(12834, _a_(12833, _n_(12832, "items", lambda: items), "append_item"), 'Java')
_l_(12835)
_c_(12837, _n_(12836, "print", lambda: print), 'Items in the Doubly linked list: ')
_l_(12838)
_c_(12841, _a_(12840, _n_(12839, "items", lambda: items), "print_foward"))
_l_(12842)