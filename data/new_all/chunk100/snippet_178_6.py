# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node(_n_(13733, "object", lambda: object)):
    _l_(13744)


    def __init__(self, data=None, next=None, prev=None):
        _l_(13743)

        _n_(13734, "self", lambda: self).data = _n_(13735, "data", lambda: data)
        _l_(13736)
        _n_(13737, "self", lambda: self).next = _n_(13738, "next", lambda: next)
        _l_(13739)
        _n_(13740, "self", lambda: self).prev = _n_(13741, "prev", lambda: prev)
        _l_(13742)

class doubly_linked_list(_n_(13745, "object", lambda: object)):
    _l_(13801)


    def __init__(self):
        _l_(13752)

        _n_(13746, "self", lambda: self).head = None
        _l_(13747)
        _n_(13748, "self", lambda: self).tail = None
        _l_(13749)
        _n_(13750, "self", lambda: self).count = 0
        _l_(13751)

    def append_item(self, data):
        _l_(13780)

        new_item = _c_(13755, _n_(13753, "Node", lambda: Node), _n_(13754, "data", lambda: data), None, None)
        _l_(13756)
        if _a_(13758, _n_(13757, "self", lambda: self), "head") is None:
            _l_(13777)

            _n_(13759, "self", lambda: self).head = _n_(13760, "new_item", lambda: new_item)
            _l_(13761)
            _n_(13762, "self", lambda: self).tail = _a_(13764, _n_(13763, "self", lambda: self), "head")
            _l_(13765)
        else:
            _n_(13766, "new_item", lambda: new_item).prev = _a_(13768, _n_(13767, "self", lambda: self), "tail")
            _l_(13769)
            _a_(13771, _n_(13770, "self", lambda: self), "tail").next = _n_(13772, "new_item", lambda: new_item)
            _l_(13773)
            _n_(13774, "self", lambda: self).tail = _n_(13775, "new_item", lambda: new_item)
            _l_(13776)
        _n_(13778, "self", lambda: self).count += 1
        _l_(13779)

    def print_foward(self):
        _l_(13789)

        for node in _c_(13783, _a_(13782, _n_(13781, "self", lambda: self), "iter")):
            _l_(13788)

            _c_(13786, _n_(13784, "print", lambda: print), _n_(13785, "node", lambda: node))
            _l_(13787)

    def iter(self):
        _l_(13800)

        current = _a_(13791, _n_(13790, "self", lambda: self), "head")
        _l_(13792)
        while _n_(13793, "current", lambda: current):
            _l_(13799)

            item_val = _a_(13795, _n_(13794, "current", lambda: current), "data")
            _l_(13796)
            yield _n_(13797, "item_val", lambda: item_val)
            _l_(13798)
items = _c_(13803, _n_(13802, "doubly_linked_list", lambda: doubly_linked_list))
_l_(13804)
_c_(13807, _a_(13806, _n_(13805, "items", lambda: items), "append_item"), 'PHP')
_l_(13808)
_c_(13811, _a_(13810, _n_(13809, "items", lambda: items), "append_item"), 'Python')
_l_(13812)
_c_(13815, _a_(13814, _n_(13813, "items", lambda: items), "append_item"), 'C#')
_l_(13816)
_c_(13819, _a_(13818, _n_(13817, "items", lambda: items), "append_item"), 'C++')
_l_(13820)
_c_(13823, _a_(13822, _n_(13821, "items", lambda: items), "append_item"), 'Java')
_l_(13824)
_c_(13826, _n_(13825, "print", lambda: print), 'Items in the Doubly linked list: ')
_l_(13827)
_c_(13830, _a_(13829, _n_(13828, "items", lambda: items), "print_foward"))
_l_(13831)