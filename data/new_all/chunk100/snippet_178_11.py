# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node(_n_(13041, "object", lambda: object)):
    _l_(13049)


    def __init__(self, data=None, next=None, prev=None):
        _l_(13048)

        _n_(13042, "self", lambda: self).data = _n_(13043, "data", lambda: data)
        _l_(13044)
        _n_(13045, "self", lambda: self).prev = _n_(13046, "prev", lambda: prev)
        _l_(13047)

class doubly_linked_list(_n_(13050, "object", lambda: object)):
    _l_(13109)


    def __init__(self):
        _l_(13057)

        _n_(13051, "self", lambda: self).head = None
        _l_(13052)
        _n_(13053, "self", lambda: self).tail = None
        _l_(13054)
        _n_(13055, "self", lambda: self).count = 0
        _l_(13056)

    def append_item(self, data):
        _l_(13085)

        new_item = _c_(13060, _n_(13058, "Node", lambda: Node), _n_(13059, "data", lambda: data), None, None)
        _l_(13061)
        if _a_(13063, _n_(13062, "self", lambda: self), "head") is None:
            _l_(13082)

            _n_(13064, "self", lambda: self).head = _n_(13065, "new_item", lambda: new_item)
            _l_(13066)
            _n_(13067, "self", lambda: self).tail = _a_(13069, _n_(13068, "self", lambda: self), "head")
            _l_(13070)
        else:
            _n_(13071, "new_item", lambda: new_item).prev = _a_(13073, _n_(13072, "self", lambda: self), "tail")
            _l_(13074)
            _a_(13076, _n_(13075, "self", lambda: self), "tail").next = _n_(13077, "new_item", lambda: new_item)
            _l_(13078)
            _n_(13079, "self", lambda: self).tail = _n_(13080, "new_item", lambda: new_item)
            _l_(13081)
        _n_(13083, "self", lambda: self).count += 1
        _l_(13084)

    def print_foward(self):
        _l_(13094)

        for node in _c_(13088, _a_(13087, _n_(13086, "self", lambda: self), "iter")):
            _l_(13093)

            _c_(13091, _n_(13089, "print", lambda: print), _n_(13090, "node", lambda: node))
            _l_(13092)

    def iter(self):
        _l_(13108)

        current = _a_(13096, _n_(13095, "self", lambda: self), "head")
        _l_(13097)
        while _n_(13098, "current", lambda: current):
            _l_(13107)

            item_val = _a_(13100, _n_(13099, "current", lambda: current), "data")
            _l_(13101)
            current = _a_(13103, _n_(13102, "current", lambda: current), "next")
            _l_(13104)
            yield _n_(13105, "item_val", lambda: item_val)
            _l_(13106)
items = _c_(13111, _n_(13110, "doubly_linked_list", lambda: doubly_linked_list))
_l_(13112)
_c_(13115, _a_(13114, _n_(13113, "items", lambda: items), "append_item"), 'PHP')
_l_(13116)
_c_(13119, _a_(13118, _n_(13117, "items", lambda: items), "append_item"), 'Python')
_l_(13120)
_c_(13123, _a_(13122, _n_(13121, "items", lambda: items), "append_item"), 'C#')
_l_(13124)
_c_(13127, _a_(13126, _n_(13125, "items", lambda: items), "append_item"), 'C++')
_l_(13128)
_c_(13131, _a_(13130, _n_(13129, "items", lambda: items), "append_item"), 'Java')
_l_(13132)
_c_(13134, _n_(13133, "print", lambda: print), 'Items in the Doubly linked list: ')
_l_(13135)
_c_(13138, _a_(13137, _n_(13136, "items", lambda: items), "print_foward"))
_l_(13139)