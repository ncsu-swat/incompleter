# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node(_n_(43342, "object", lambda: object)):
    _l_(43353)


    def __init__(self, data=None, next=None, prev=None):
        _l_(43352)

        _n_(43343, "self", lambda: self).data = _n_(43344, "data", lambda: data)
        _l_(43345)
        _n_(43346, "self", lambda: self).next = _n_(43347, "next", lambda: next)
        _l_(43348)
        _n_(43349, "self", lambda: self).prev = _n_(43350, "prev", lambda: prev)
        _l_(43351)

class doubly_linked_list(_n_(43354, "object", lambda: object)):
    _l_(43419)


    def __init__(self):
        _l_(43361)

        _n_(43355, "self", lambda: self).head = None
        _l_(43356)
        _n_(43357, "self", lambda: self).tail = None
        _l_(43358)
        _n_(43359, "self", lambda: self).count = 0
        _l_(43360)

    def append_item(self, data):
        _l_(43385)

        new_item = _c_(43364, _n_(43362, "Node", lambda: Node), _n_(43363, "data", lambda: data), None, None)
        _l_(43365)
        if _a_(43367, _n_(43366, "self", lambda: self), "head") is None:
            _l_(43382)

            _n_(43368, "self", lambda: self).head = _n_(43369, "new_item", lambda: new_item)
            _l_(43370)
        else:
            _n_(43371, "new_item", lambda: new_item).prev = _a_(43373, _n_(43372, "self", lambda: self), "tail")
            _l_(43374)
            _a_(43376, _n_(43375, "self", lambda: self), "tail").next = _n_(43377, "new_item", lambda: new_item)
            _l_(43378)
            _n_(43379, "self", lambda: self).tail = _n_(43380, "new_item", lambda: new_item)
            _l_(43381)
        _n_(43383, "self", lambda: self).count += 1
        _l_(43384)

    def iter(self):
        _l_(43399)

        current = _a_(43387, _n_(43386, "self", lambda: self), "head")
        _l_(43388)
        while _n_(43389, "current", lambda: current):
            _l_(43398)

            item_val = _a_(43391, _n_(43390, "current", lambda: current), "data")
            _l_(43392)
            current = _a_(43394, _n_(43393, "current", lambda: current), "next")
            _l_(43395)
            yield _n_(43396, "item_val", lambda: item_val)
            _l_(43397)

    def print_foward(self):
        _l_(43408)

        for node in _c_(43402, _a_(43401, _n_(43400, "self", lambda: self), "iter")):
            _l_(43407)

            _c_(43405, _n_(43403, "print", lambda: print), _n_(43404, "node", lambda: node))
            _l_(43406)

    def search_item(self, val):
        _l_(43418)

        for node in _c_(43411, _a_(43410, _n_(43409, "self", lambda: self), "iter")):
            _l_(43416)

            if _n_(43412, "val", lambda: val) == _n_(43413, "node", lambda: node):
                _l_(43415)

                aux = True
                _l_(43414)
                return aux
        aux = False
        _l_(43417)
        return aux
items = _c_(43421, _n_(43420, "doubly_linked_list", lambda: doubly_linked_list))
_l_(43422)
_c_(43425, _a_(43424, _n_(43423, "items", lambda: items), "append_item"), 'PHP')
_l_(43426)
_c_(43429, _a_(43428, _n_(43427, "items", lambda: items), "append_item"), 'Python')
_l_(43430)
_c_(43433, _a_(43432, _n_(43431, "items", lambda: items), "append_item"), 'C#')
_l_(43434)
_c_(43437, _a_(43436, _n_(43435, "items", lambda: items), "append_item"), 'C++')
_l_(43438)
_c_(43441, _a_(43440, _n_(43439, "items", lambda: items), "append_item"), 'Java')
_l_(43442)
_c_(43445, _a_(43444, _n_(43443, "items", lambda: items), "append_item"), 'SQL')
_l_(43446)
_c_(43448, _n_(43447, "print", lambda: print), 'Original list:')
_l_(43449)
_c_(43452, _a_(43451, _n_(43450, "items", lambda: items), "print_foward"))
_l_(43453)
_c_(43455, _n_(43454, "print", lambda: print), '\n')
_l_(43456)
if _c_(43459, _a_(43458, _n_(43457, "items", lambda: items), "search_item"), 'SQL'):
    _l_(43466)

    _c_(43461, _n_(43460, "print", lambda: print), 'True')
    _l_(43462)
else:
    _c_(43464, _n_(43463, "print", lambda: print), 'False')
    _l_(43465)
if _c_(43469, _a_(43468, _n_(43467, "items", lambda: items), "search_item"), 'C+'):
    _l_(43476)

    _c_(43471, _n_(43470, "print", lambda: print), 'True')
    _l_(43472)
else:
    _c_(43474, _n_(43473, "print", lambda: print), 'False')
    _l_(43475)