# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node(_n_(42254, "object", lambda: object)):
    _l_(42262)


    def __init__(self, data=None, next=None, prev=None):
        _l_(42261)

        _n_(42255, "self", lambda: self).data = _n_(42256, "data", lambda: data)
        _l_(42257)
        _n_(42258, "self", lambda: self).next = _n_(42259, "next", lambda: next)
        _l_(42260)

class doubly_linked_list(_n_(42263, "object", lambda: object)):
    _l_(42332)


    def __init__(self):
        _l_(42270)

        _n_(42264, "self", lambda: self).head = None
        _l_(42265)
        _n_(42266, "self", lambda: self).tail = None
        _l_(42267)
        _n_(42268, "self", lambda: self).count = 0
        _l_(42269)

    def append_item(self, data):
        _l_(42298)

        new_item = _c_(42273, _n_(42271, "Node", lambda: Node), _n_(42272, "data", lambda: data), None, None)
        _l_(42274)
        if _a_(42276, _n_(42275, "self", lambda: self), "head") is None:
            _l_(42295)

            _n_(42277, "self", lambda: self).head = _n_(42278, "new_item", lambda: new_item)
            _l_(42279)
            _n_(42280, "self", lambda: self).tail = _a_(42282, _n_(42281, "self", lambda: self), "head")
            _l_(42283)
        else:
            _n_(42284, "new_item", lambda: new_item).prev = _a_(42286, _n_(42285, "self", lambda: self), "tail")
            _l_(42287)
            _a_(42289, _n_(42288, "self", lambda: self), "tail").next = _n_(42290, "new_item", lambda: new_item)
            _l_(42291)
            _n_(42292, "self", lambda: self).tail = _n_(42293, "new_item", lambda: new_item)
            _l_(42294)
        _n_(42296, "self", lambda: self).count += 1
        _l_(42297)

    def iter(self):
        _l_(42312)

        current = _a_(42300, _n_(42299, "self", lambda: self), "head")
        _l_(42301)
        while _n_(42302, "current", lambda: current):
            _l_(42311)

            item_val = _a_(42304, _n_(42303, "current", lambda: current), "data")
            _l_(42305)
            current = _a_(42307, _n_(42306, "current", lambda: current), "next")
            _l_(42308)
            yield _n_(42309, "item_val", lambda: item_val)
            _l_(42310)

    def print_foward(self):
        _l_(42321)

        for node in _c_(42315, _a_(42314, _n_(42313, "self", lambda: self), "iter")):
            _l_(42320)

            _c_(42318, _n_(42316, "print", lambda: print), _n_(42317, "node", lambda: node))
            _l_(42319)

    def search_item(self, val):
        _l_(42331)

        for node in _c_(42324, _a_(42323, _n_(42322, "self", lambda: self), "iter")):
            _l_(42329)

            if _n_(42325, "val", lambda: val) == _n_(42326, "node", lambda: node):
                _l_(42328)

                aux = True
                _l_(42327)
                return aux
        aux = False
        _l_(42330)
        return aux
items = _c_(42334, _n_(42333, "doubly_linked_list", lambda: doubly_linked_list))
_l_(42335)
_c_(42338, _a_(42337, _n_(42336, "items", lambda: items), "append_item"), 'PHP')
_l_(42339)
_c_(42342, _a_(42341, _n_(42340, "items", lambda: items), "append_item"), 'Python')
_l_(42343)
_c_(42346, _a_(42345, _n_(42344, "items", lambda: items), "append_item"), 'C#')
_l_(42347)
_c_(42350, _a_(42349, _n_(42348, "items", lambda: items), "append_item"), 'C++')
_l_(42351)
_c_(42354, _a_(42353, _n_(42352, "items", lambda: items), "append_item"), 'Java')
_l_(42355)
_c_(42358, _a_(42357, _n_(42356, "items", lambda: items), "append_item"), 'SQL')
_l_(42359)
_c_(42361, _n_(42360, "print", lambda: print), 'Original list:')
_l_(42362)
_c_(42365, _a_(42364, _n_(42363, "items", lambda: items), "print_foward"))
_l_(42366)
_c_(42368, _n_(42367, "print", lambda: print), '\n')
_l_(42369)
if _c_(42372, _a_(42371, _n_(42370, "items", lambda: items), "search_item"), 'SQL'):
    _l_(42379)

    _c_(42374, _n_(42373, "print", lambda: print), 'True')
    _l_(42375)
else:
    _c_(42377, _n_(42376, "print", lambda: print), 'False')
    _l_(42378)
if _c_(42382, _a_(42381, _n_(42380, "items", lambda: items), "search_item"), 'C+'):
    _l_(42389)

    _c_(42384, _n_(42383, "print", lambda: print), 'True')
    _l_(42385)
else:
    _c_(42387, _n_(42386, "print", lambda: print), 'False')
    _l_(42388)