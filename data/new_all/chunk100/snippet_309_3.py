# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node(_n_(28122, "object", lambda: object)):
    _l_(28133)


    def __init__(self, value=None, next=None, prev=None):
        _l_(28132)

        _n_(28123, "self", lambda: self).value = _n_(28124, "value", lambda: value)
        _l_(28125)
        _n_(28126, "self", lambda: self).next = _n_(28127, "next", lambda: next)
        _l_(28128)
        _n_(28129, "self", lambda: self).prev = _n_(28130, "prev", lambda: prev)
        _l_(28131)

class doubly_linked_list(_n_(28134, "object", lambda: object)):
    _l_(28257)


    def __init__(self):
        _l_(28141)

        _n_(28135, "self", lambda: self).head = None
        _l_(28136)
        _n_(28137, "self", lambda: self).tail = None
        _l_(28138)
        _n_(28139, "self", lambda: self).count = 0
        _l_(28140)

    def append_item(self, value):
        _l_(28165)

        if _a_(28143, _n_(28142, "self", lambda: self), "head") is None:
            _l_(28162)

            _n_(28144, "self", lambda: self).head = _n_(28145, "new_item", lambda: new_item)
            _l_(28146)
            _n_(28147, "self", lambda: self).tail = _a_(28149, _n_(28148, "self", lambda: self), "head")
            _l_(28150)
        else:
            _n_(28151, "new_item", lambda: new_item).prev = _a_(28153, _n_(28152, "self", lambda: self), "tail")
            _l_(28154)
            _a_(28156, _n_(28155, "self", lambda: self), "tail").next = _n_(28157, "new_item", lambda: new_item)
            _l_(28158)
            _n_(28159, "self", lambda: self).tail = _n_(28160, "new_item", lambda: new_item)
            _l_(28161)
        _n_(28163, "self", lambda: self).count += 1
        _l_(28164)

    def iter(self):
        _l_(28179)

        current = _a_(28167, _n_(28166, "self", lambda: self), "head")
        _l_(28168)
        while _n_(28169, "current", lambda: current):
            _l_(28178)

            item_val = _a_(28171, _n_(28170, "current", lambda: current), "value")
            _l_(28172)
            current = _a_(28174, _n_(28173, "current", lambda: current), "next")
            _l_(28175)
            yield _n_(28176, "item_val", lambda: item_val)
            _l_(28177)

    def print_foward(self):
        _l_(28188)

        for node in _c_(28182, _a_(28181, _n_(28180, "self", lambda: self), "iter")):
            _l_(28187)

            _c_(28185, _n_(28183, "print", lambda: print), _n_(28184, "node", lambda: node))
            _l_(28186)

    def search_item(self, val):
        _l_(28198)

        for node in _c_(28191, _a_(28190, _n_(28189, "self", lambda: self), "iter")):
            _l_(28196)

            if _n_(28192, "val", lambda: val) == _n_(28193, "node", lambda: node):
                _l_(28195)

                aux = True
                _l_(28194)
                return aux
        aux = False
        _l_(28197)
        return aux

    def delete(self, value):
        _l_(28256)

        current = _a_(28200, _n_(28199, "self", lambda: self), "head")
        _l_(28201)
        node_deleted = False
        _l_(28202)
        if _n_(28203, "current", lambda: current) is None:
            _l_(28251)

            node_deleted = False
            _l_(28204)
        elif _a_(28206, _n_(28205, "current", lambda: current), "value") == _n_(28207, "value", lambda: value):
            _l_(28250)

            _n_(28208, "self", lambda: self).head = _a_(28210, _n_(28209, "current", lambda: current), "next")
            _l_(28211)
            _a_(28213, _n_(28212, "self", lambda: self), "head").prev = None
            _l_(28214)
            node_deleted = True
            _l_(28215)
        elif _a_(28218, _a_(28217, _n_(28216, "self", lambda: self), "tail"), "value") == _n_(28219, "value", lambda: value):
            _l_(28249)

            _n_(28220, "self", lambda: self).tail = _a_(28223, _a_(28222, _n_(28221, "self", lambda: self), "tail"), "prev")
            _l_(28224)
            _a_(28226, _n_(28225, "self", lambda: self), "tail").next = None
            _l_(28227)
            node_deleted = True
            _l_(28228)
        else:
            while _n_(28229, "current", lambda: current):
                _l_(28248)

                if _a_(28231, _n_(28230, "current", lambda: current), "value") == _n_(28232, "value", lambda: value):
                    _l_(28244)

                    _a_(28234, _n_(28233, "current", lambda: current), "prev").next = _a_(28236, _n_(28235, "current", lambda: current), "next")
                    _l_(28237)
                    _a_(28239, _n_(28238, "current", lambda: current), "next").prev = _a_(28241, _n_(28240, "current", lambda: current), "prev")
                    _l_(28242)
                    node_deleted = True
                    _l_(28243)
                current = _a_(28246, _n_(28245, "current", lambda: current), "next")
                _l_(28247)
        if _n_(28252, "node_deleted", lambda: node_deleted):
            _l_(28255)

            _n_(28253, "self", lambda: self).count -= 1
            _l_(28254)
items = _c_(28259, _n_(28258, "doubly_linked_list", lambda: doubly_linked_list))
_l_(28260)
_c_(28263, _a_(28262, _n_(28261, "items", lambda: items), "append_item"), 'PHP')
_l_(28264)
_c_(28267, _a_(28266, _n_(28265, "items", lambda: items), "append_item"), 'Python')
_l_(28268)
_c_(28271, _a_(28270, _n_(28269, "items", lambda: items), "append_item"), 'C#')
_l_(28272)
_c_(28275, _a_(28274, _n_(28273, "items", lambda: items), "append_item"), 'C++')
_l_(28276)
_c_(28279, _a_(28278, _n_(28277, "items", lambda: items), "append_item"), 'Java')
_l_(28280)
_c_(28283, _a_(28282, _n_(28281, "items", lambda: items), "append_item"), 'SQL')
_l_(28284)
_c_(28286, _n_(28285, "print", lambda: print), 'Original list:')
_l_(28287)
_c_(28290, _a_(28289, _n_(28288, "items", lambda: items), "print_foward"))
_l_(28291)
_c_(28294, _a_(28293, _n_(28292, "items", lambda: items), "delete"), 'Java')
_l_(28295)
_c_(28298, _a_(28297, _n_(28296, "items", lambda: items), "delete"), 'Python')
_l_(28299)
_c_(28301, _n_(28300, "print", lambda: print), '\nList after deleting two items:')
_l_(28302)
_c_(28305, _a_(28304, _n_(28303, "items", lambda: items), "print_foward"))
_l_(28306)