# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node(_n_(20977, "object", lambda: object)):
    _l_(20988)


    def __init__(self, data=None, next=None, prev=None):
        _l_(20987)

        _n_(20978, "self", lambda: self).data = _n_(20979, "data", lambda: data)
        _l_(20980)
        _n_(20981, "self", lambda: self).next = _n_(20982, "next", lambda: next)
        _l_(20983)
        _n_(20984, "self", lambda: self).prev = _n_(20985, "prev", lambda: prev)
        _l_(20986)

class doubly_linked_list(_n_(20989, "object", lambda: object)):
    _l_(21023)


    def __init__(self):
        _l_(20994)

        _n_(20990, "self", lambda: self).head = None
        _l_(20991)
        _n_(20992, "self", lambda: self).count = 0
        _l_(20993)

    def append_item(self, data):
        _l_(21022)

        new_item = _c_(20997, _n_(20995, "Node", lambda: Node), _n_(20996, "data", lambda: data), None, None)
        _l_(20998)
        if _a_(21000, _n_(20999, "self", lambda: self), "head") is None:
            _l_(21019)

            _n_(21001, "self", lambda: self).head = _n_(21002, "new_item", lambda: new_item)
            _l_(21003)
            _n_(21004, "self", lambda: self).tail = _a_(21006, _n_(21005, "self", lambda: self), "head")
            _l_(21007)
        else:
            _n_(21008, "new_item", lambda: new_item).prev = _a_(21010, _n_(21009, "self", lambda: self), "tail")
            _l_(21011)
            _a_(21013, _n_(21012, "self", lambda: self), "tail").next = _n_(21014, "new_item", lambda: new_item)
            _l_(21015)
            _n_(21016, "self", lambda: self).tail = _n_(21017, "new_item", lambda: new_item)
            _l_(21018)
        _n_(21020, "self", lambda: self).count += 1
        _l_(21021)
items = _c_(21025, _n_(21024, "doubly_linked_list", lambda: doubly_linked_list))
_l_(21026)
_c_(21029, _a_(21028, _n_(21027, "items", lambda: items), "append_item"), 'PHP')
_l_(21030)
_c_(21033, _a_(21032, _n_(21031, "items", lambda: items), "append_item"), 'Python')
_l_(21034)
_c_(21037, _a_(21036, _n_(21035, "items", lambda: items), "append_item"), 'C#')
_l_(21038)
_c_(21041, _a_(21040, _n_(21039, "items", lambda: items), "append_item"), 'C++')
_l_(21042)
_c_(21045, _a_(21044, _n_(21043, "items", lambda: items), "append_item"), 'Java')
_l_(21046)
_c_(21049, _a_(21048, _n_(21047, "items", lambda: items), "append_item"), 'SQL')
_l_(21050)
_c_(21054, _n_(21051, "print", lambda: print), 'Number of items of the  Doubly linked list:', _a_(21053, _n_(21052, "items", lambda: items), "count"))
_l_(21055)