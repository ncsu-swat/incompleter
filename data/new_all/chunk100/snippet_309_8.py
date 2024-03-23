# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node(_n_(29050, "object", lambda: object)):
    _l_(29061)


    def __init__(self, value=None, next=None, prev=None):
        _l_(29060)

        _n_(29051, "self", lambda: self).value = _n_(29052, "value", lambda: value)
        _l_(29053)
        _n_(29054, "self", lambda: self).next = _n_(29055, "next", lambda: next)
        _l_(29056)
        _n_(29057, "self", lambda: self).prev = _n_(29058, "prev", lambda: prev)
        _l_(29059)

class doubly_linked_list(_n_(29062, "object", lambda: object)):
    _l_(29187)


    def __init__(self):
        _l_(29067)

        _n_(29063, "self", lambda: self).tail = None
        _l_(29064)
        _n_(29065, "self", lambda: self).count = 0
        _l_(29066)

    def append_item(self, value):
        _l_(29095)

        new_item = _c_(29070, _n_(29068, "Node", lambda: Node), _n_(29069, "value", lambda: value), None, None)
        _l_(29071)
        if _a_(29073, _n_(29072, "self", lambda: self), "head") is None:
            _l_(29092)

            _n_(29074, "self", lambda: self).head = _n_(29075, "new_item", lambda: new_item)
            _l_(29076)
            _n_(29077, "self", lambda: self).tail = _a_(29079, _n_(29078, "self", lambda: self), "head")
            _l_(29080)
        else:
            _n_(29081, "new_item", lambda: new_item).prev = _a_(29083, _n_(29082, "self", lambda: self), "tail")
            _l_(29084)
            _a_(29086, _n_(29085, "self", lambda: self), "tail").next = _n_(29087, "new_item", lambda: new_item)
            _l_(29088)
            _n_(29089, "self", lambda: self).tail = _n_(29090, "new_item", lambda: new_item)
            _l_(29091)
        _n_(29093, "self", lambda: self).count += 1
        _l_(29094)

    def iter(self):
        _l_(29109)

        current = _a_(29097, _n_(29096, "self", lambda: self), "head")
        _l_(29098)
        while _n_(29099, "current", lambda: current):
            _l_(29108)

            item_val = _a_(29101, _n_(29100, "current", lambda: current), "value")
            _l_(29102)
            current = _a_(29104, _n_(29103, "current", lambda: current), "next")
            _l_(29105)
            yield _n_(29106, "item_val", lambda: item_val)
            _l_(29107)

    def print_foward(self):
        _l_(29118)

        for node in _c_(29112, _a_(29111, _n_(29110, "self", lambda: self), "iter")):
            _l_(29117)

            _c_(29115, _n_(29113, "print", lambda: print), _n_(29114, "node", lambda: node))
            _l_(29116)

    def search_item(self, val):
        _l_(29128)

        for node in _c_(29121, _a_(29120, _n_(29119, "self", lambda: self), "iter")):
            _l_(29126)

            if _n_(29122, "val", lambda: val) == _n_(29123, "node", lambda: node):
                _l_(29125)

                aux = True
                _l_(29124)
                return aux
        aux = False
        _l_(29127)
        return aux

    def delete(self, value):
        _l_(29186)

        current = _a_(29130, _n_(29129, "self", lambda: self), "head")
        _l_(29131)
        node_deleted = False
        _l_(29132)
        if _n_(29133, "current", lambda: current) is None:
            _l_(29181)

            node_deleted = False
            _l_(29134)
        elif _a_(29136, _n_(29135, "current", lambda: current), "value") == _n_(29137, "value", lambda: value):
            _l_(29180)

            _n_(29138, "self", lambda: self).head = _a_(29140, _n_(29139, "current", lambda: current), "next")
            _l_(29141)
            _a_(29143, _n_(29142, "self", lambda: self), "head").prev = None
            _l_(29144)
            node_deleted = True
            _l_(29145)
        elif _a_(29148, _a_(29147, _n_(29146, "self", lambda: self), "tail"), "value") == _n_(29149, "value", lambda: value):
            _l_(29179)

            _n_(29150, "self", lambda: self).tail = _a_(29153, _a_(29152, _n_(29151, "self", lambda: self), "tail"), "prev")
            _l_(29154)
            _a_(29156, _n_(29155, "self", lambda: self), "tail").next = None
            _l_(29157)
            node_deleted = True
            _l_(29158)
        else:
            while _n_(29159, "current", lambda: current):
                _l_(29178)

                if _a_(29161, _n_(29160, "current", lambda: current), "value") == _n_(29162, "value", lambda: value):
                    _l_(29174)

                    _a_(29164, _n_(29163, "current", lambda: current), "prev").next = _a_(29166, _n_(29165, "current", lambda: current), "next")
                    _l_(29167)
                    _a_(29169, _n_(29168, "current", lambda: current), "next").prev = _a_(29171, _n_(29170, "current", lambda: current), "prev")
                    _l_(29172)
                    node_deleted = True
                    _l_(29173)
                current = _a_(29176, _n_(29175, "current", lambda: current), "next")
                _l_(29177)
        if _n_(29182, "node_deleted", lambda: node_deleted):
            _l_(29185)

            _n_(29183, "self", lambda: self).count -= 1
            _l_(29184)
items = _c_(29189, _n_(29188, "doubly_linked_list", lambda: doubly_linked_list))
_l_(29190)
_c_(29193, _a_(29192, _n_(29191, "items", lambda: items), "append_item"), 'PHP')
_l_(29194)
_c_(29197, _a_(29196, _n_(29195, "items", lambda: items), "append_item"), 'Python')
_l_(29198)
_c_(29201, _a_(29200, _n_(29199, "items", lambda: items), "append_item"), 'C#')
_l_(29202)
_c_(29205, _a_(29204, _n_(29203, "items", lambda: items), "append_item"), 'C++')
_l_(29206)
_c_(29209, _a_(29208, _n_(29207, "items", lambda: items), "append_item"), 'Java')
_l_(29210)
_c_(29213, _a_(29212, _n_(29211, "items", lambda: items), "append_item"), 'SQL')
_l_(29214)
_c_(29216, _n_(29215, "print", lambda: print), 'Original list:')
_l_(29217)
_c_(29220, _a_(29219, _n_(29218, "items", lambda: items), "print_foward"))
_l_(29221)
_c_(29224, _a_(29223, _n_(29222, "items", lambda: items), "delete"), 'Java')
_l_(29225)
_c_(29228, _a_(29227, _n_(29226, "items", lambda: items), "delete"), 'Python')
_l_(29229)
_c_(29231, _n_(29230, "print", lambda: print), '\nList after deleting two items:')
_l_(29232)
_c_(29235, _a_(29234, _n_(29233, "items", lambda: items), "print_foward"))
_l_(29236)