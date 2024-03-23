# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node(_n_(20432, "object", lambda: object)):
    _l_(20443)


    def __init__(self, data=None, next=None, prev=None):
        _l_(20442)

        _n_(20433, "self", lambda: self).data = _n_(20434, "data", lambda: data)
        _l_(20435)
        _n_(20436, "self", lambda: self).next = _n_(20437, "next", lambda: next)
        _l_(20438)
        _n_(20439, "self", lambda: self).prev = _n_(20440, "prev", lambda: prev)
        _l_(20441)

class doubly_linked_list(_n_(20444, "object", lambda: object)):
    _l_(20476)


    def __init__(self):
        _l_(20451)

        _n_(20445, "self", lambda: self).head = None
        _l_(20446)
        _n_(20447, "self", lambda: self).tail = None
        _l_(20448)
        _n_(20449, "self", lambda: self).count = 0
        _l_(20450)

    def append_item(self, data):
        _l_(20475)

        if _a_(20453, _n_(20452, "self", lambda: self), "head") is None:
            _l_(20472)

            _n_(20454, "self", lambda: self).head = _n_(20455, "new_item", lambda: new_item)
            _l_(20456)
            _n_(20457, "self", lambda: self).tail = _a_(20459, _n_(20458, "self", lambda: self), "head")
            _l_(20460)
        else:
            _n_(20461, "new_item", lambda: new_item).prev = _a_(20463, _n_(20462, "self", lambda: self), "tail")
            _l_(20464)
            _a_(20466, _n_(20465, "self", lambda: self), "tail").next = _n_(20467, "new_item", lambda: new_item)
            _l_(20468)
            _n_(20469, "self", lambda: self).tail = _n_(20470, "new_item", lambda: new_item)
            _l_(20471)
        _n_(20473, "self", lambda: self).count += 1
        _l_(20474)
items = _c_(20478, _n_(20477, "doubly_linked_list", lambda: doubly_linked_list))
_l_(20479)
_c_(20482, _a_(20481, _n_(20480, "items", lambda: items), "append_item"), 'PHP')
_l_(20483)
_c_(20486, _a_(20485, _n_(20484, "items", lambda: items), "append_item"), 'Python')
_l_(20487)
_c_(20490, _a_(20489, _n_(20488, "items", lambda: items), "append_item"), 'C#')
_l_(20491)
_c_(20494, _a_(20493, _n_(20492, "items", lambda: items), "append_item"), 'C++')
_l_(20495)
_c_(20498, _a_(20497, _n_(20496, "items", lambda: items), "append_item"), 'Java')
_l_(20499)
_c_(20502, _a_(20501, _n_(20500, "items", lambda: items), "append_item"), 'SQL')
_l_(20503)
_c_(20507, _n_(20504, "print", lambda: print), 'Number of items of the  Doubly linked list:', _a_(20506, _n_(20505, "items", lambda: items), "count"))
_l_(20508)