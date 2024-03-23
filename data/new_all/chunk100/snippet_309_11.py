# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node(_n_(27005, "object", lambda: object)):
    _l_(27016)


    def __init__(self, value=None, next=None, prev=None):
        _l_(27015)

        _n_(27006, "self", lambda: self).value = _n_(27007, "value", lambda: value)
        _l_(27008)
        _n_(27009, "self", lambda: self).next = _n_(27010, "next", lambda: next)
        _l_(27011)
        _n_(27012, "self", lambda: self).prev = _n_(27013, "prev", lambda: prev)
        _l_(27014)

class doubly_linked_list(_n_(27017, "object", lambda: object)):
    _l_(27141)


    def __init__(self):
        _l_(27024)

        _n_(27018, "self", lambda: self).head = None
        _l_(27019)
        _n_(27020, "self", lambda: self).tail = None
        _l_(27021)
        _n_(27022, "self", lambda: self).count = 0
        _l_(27023)

    def append_item(self, value):
        _l_(27052)

        new_item = _c_(27027, _n_(27025, "Node", lambda: Node), _n_(27026, "value", lambda: value), None, None)
        _l_(27028)
        if _a_(27030, _n_(27029, "self", lambda: self), "head") is None:
            _l_(27049)

            _n_(27031, "self", lambda: self).head = _n_(27032, "new_item", lambda: new_item)
            _l_(27033)
            _n_(27034, "self", lambda: self).tail = _a_(27036, _n_(27035, "self", lambda: self), "head")
            _l_(27037)
        else:
            _n_(27038, "new_item", lambda: new_item).prev = _a_(27040, _n_(27039, "self", lambda: self), "tail")
            _l_(27041)
            _a_(27043, _n_(27042, "self", lambda: self), "tail").next = _n_(27044, "new_item", lambda: new_item)
            _l_(27045)
            _n_(27046, "self", lambda: self).tail = _n_(27047, "new_item", lambda: new_item)
            _l_(27048)
        _n_(27050, "self", lambda: self).count += 1
        _l_(27051)

    def iter(self):
        _l_(27063)

        current = _a_(27054, _n_(27053, "self", lambda: self), "head")
        _l_(27055)
        while _n_(27056, "current", lambda: current):
            _l_(27062)

            item_val = _a_(27058, _n_(27057, "current", lambda: current), "value")
            _l_(27059)
            yield _n_(27060, "item_val", lambda: item_val)
            _l_(27061)

    def print_foward(self):
        _l_(27072)

        for node in _c_(27066, _a_(27065, _n_(27064, "self", lambda: self), "iter")):
            _l_(27071)

            _c_(27069, _n_(27067, "print", lambda: print), _n_(27068, "node", lambda: node))
            _l_(27070)

    def search_item(self, val):
        _l_(27082)

        for node in _c_(27075, _a_(27074, _n_(27073, "self", lambda: self), "iter")):
            _l_(27080)

            if _n_(27076, "val", lambda: val) == _n_(27077, "node", lambda: node):
                _l_(27079)

                aux = True
                _l_(27078)
                return aux
        aux = False
        _l_(27081)
        return aux

    def delete(self, value):
        _l_(27140)

        current = _a_(27084, _n_(27083, "self", lambda: self), "head")
        _l_(27085)
        node_deleted = False
        _l_(27086)
        if _n_(27087, "current", lambda: current) is None:
            _l_(27135)

            node_deleted = False
            _l_(27088)
        elif _a_(27090, _n_(27089, "current", lambda: current), "value") == _n_(27091, "value", lambda: value):
            _l_(27134)

            _n_(27092, "self", lambda: self).head = _a_(27094, _n_(27093, "current", lambda: current), "next")
            _l_(27095)
            _a_(27097, _n_(27096, "self", lambda: self), "head").prev = None
            _l_(27098)
            node_deleted = True
            _l_(27099)
        elif _a_(27102, _a_(27101, _n_(27100, "self", lambda: self), "tail"), "value") == _n_(27103, "value", lambda: value):
            _l_(27133)

            _n_(27104, "self", lambda: self).tail = _a_(27107, _a_(27106, _n_(27105, "self", lambda: self), "tail"), "prev")
            _l_(27108)
            _a_(27110, _n_(27109, "self", lambda: self), "tail").next = None
            _l_(27111)
            node_deleted = True
            _l_(27112)
        else:
            while _n_(27113, "current", lambda: current):
                _l_(27132)

                if _a_(27115, _n_(27114, "current", lambda: current), "value") == _n_(27116, "value", lambda: value):
                    _l_(27128)

                    _a_(27118, _n_(27117, "current", lambda: current), "prev").next = _a_(27120, _n_(27119, "current", lambda: current), "next")
                    _l_(27121)
                    _a_(27123, _n_(27122, "current", lambda: current), "next").prev = _a_(27125, _n_(27124, "current", lambda: current), "prev")
                    _l_(27126)
                    node_deleted = True
                    _l_(27127)
                current = _a_(27130, _n_(27129, "current", lambda: current), "next")
                _l_(27131)
        if _n_(27136, "node_deleted", lambda: node_deleted):
            _l_(27139)

            _n_(27137, "self", lambda: self).count -= 1
            _l_(27138)
items = _c_(27143, _n_(27142, "doubly_linked_list", lambda: doubly_linked_list))
_l_(27144)
_c_(27147, _a_(27146, _n_(27145, "items", lambda: items), "append_item"), 'PHP')
_l_(27148)
_c_(27151, _a_(27150, _n_(27149, "items", lambda: items), "append_item"), 'Python')
_l_(27152)
_c_(27155, _a_(27154, _n_(27153, "items", lambda: items), "append_item"), 'C#')
_l_(27156)
_c_(27159, _a_(27158, _n_(27157, "items", lambda: items), "append_item"), 'C++')
_l_(27160)
_c_(27163, _a_(27162, _n_(27161, "items", lambda: items), "append_item"), 'Java')
_l_(27164)
_c_(27167, _a_(27166, _n_(27165, "items", lambda: items), "append_item"), 'SQL')
_l_(27168)
_c_(27170, _n_(27169, "print", lambda: print), 'Original list:')
_l_(27171)
_c_(27174, _a_(27173, _n_(27172, "items", lambda: items), "print_foward"))
_l_(27175)
_c_(27178, _a_(27177, _n_(27176, "items", lambda: items), "delete"), 'Java')
_l_(27179)
_c_(27182, _a_(27181, _n_(27180, "items", lambda: items), "delete"), 'Python')
_l_(27183)
_c_(27185, _n_(27184, "print", lambda: print), '\nList after deleting two items:')
_l_(27186)
_c_(27189, _a_(27188, _n_(27187, "items", lambda: items), "print_foward"))
_l_(27190)