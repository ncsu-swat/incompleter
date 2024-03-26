# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node(_n_(107081, "object", lambda: object)):
    _l_(107092)


    def __init__(self, data=None, next=None, prev=None):
        _l_(107091)

        _n_(107082, "self", lambda: self).data = _n_(107083, "data", lambda: data)
        _l_(107084)
        _n_(107085, "self", lambda: self).next = _n_(107086, "next", lambda: next)
        _l_(107087)
        _n_(107088, "self", lambda: self).prev = _n_(107089, "prev", lambda: prev)
        _l_(107090)

class doubly_linked_list(_n_(107093, "object", lambda: object)):
    _l_(107129)


    def __init__(self):
        _l_(107100)

        _n_(107094, "self", lambda: self).head = None
        _l_(107095)
        _n_(107096, "self", lambda: self).tail = None
        _l_(107097)
        _n_(107098, "self", lambda: self).count = 0
        _l_(107099)

    def append_item(self, data):
        _l_(107128)

        new_item = _c_(107103, _n_(107101, "Node", lambda: Node), _n_(107102, "data", lambda: data), None, None)
        _l_(107104)
        if _a_(107106, _n_(107105, "self", lambda: self), "head") is None:
            _l_(107125)

            _n_(107107, "self", lambda: self).head = _n_(107108, "new_item", lambda: new_item)
            _l_(107109)
            _n_(107110, "self", lambda: self).tail = _a_(107112, _n_(107111, "self", lambda: self), "head")
            _l_(107113)
        else:
            _n_(107114, "new_item", lambda: new_item).prev = _a_(107116, _n_(107115, "self", lambda: self), "tail")
            _l_(107117)
            _a_(107119, _n_(107118, "self", lambda: self), "tail").next = _n_(107120, "new_item", lambda: new_item)
            _l_(107121)
            _n_(107122, "self", lambda: self).tail = _n_(107123, "new_item", lambda: new_item)
            _l_(107124)
        _n_(107126, "self", lambda: self).count += 1
        _l_(107127)
_c_(107132, _a_(107131, _n_(107130, "items", lambda: items), "append_item"), 'PHP')
_l_(107133)
_c_(107136, _a_(107135, _n_(107134, "items", lambda: items), "append_item"), 'Python')
_l_(107137)
_c_(107140, _a_(107139, _n_(107138, "items", lambda: items), "append_item"), 'C#')
_l_(107141)
_c_(107144, _a_(107143, _n_(107142, "items", lambda: items), "append_item"), 'C++')
_l_(107145)
_c_(107148, _a_(107147, _n_(107146, "items", lambda: items), "append_item"), 'Java')
_l_(107149)
_c_(107152, _a_(107151, _n_(107150, "items", lambda: items), "append_item"), 'SQL')
_l_(107153)
_c_(107157, _n_(107154, "print", lambda: print), 'Number of items of the  Doubly linked list:', _a_(107156, _n_(107155, "items", lambda: items), "count"))
_l_(107158)