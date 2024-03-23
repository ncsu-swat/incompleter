# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node(_n_(42390, "object", lambda: object)):
    _l_(42401)


    def __init__(self, data=None, next=None, prev=None):
        _l_(42400)

        _n_(42391, "self", lambda: self).data = _n_(42392, "data", lambda: data)
        _l_(42393)
        _n_(42394, "self", lambda: self).next = _n_(42395, "next", lambda: next)
        _l_(42396)
        _n_(42397, "self", lambda: self).prev = _n_(42398, "prev", lambda: prev)
        _l_(42399)

class doubly_linked_list(_n_(42402, "object", lambda: object)):
    _l_(42468)


    def __init__(self):
        _l_(42409)

        _n_(42403, "self", lambda: self).head = None
        _l_(42404)
        _n_(42405, "self", lambda: self).tail = None
        _l_(42406)
        _n_(42407, "self", lambda: self).count = 0
        _l_(42408)

    def append_item(self, data):
        _l_(42437)

        new_item = _c_(42412, _n_(42410, "Node", lambda: Node), _n_(42411, "data", lambda: data), None, None)
        _l_(42413)
        if _a_(42415, _n_(42414, "self", lambda: self), "head") is None:
            _l_(42434)

            _n_(42416, "self", lambda: self).head = _n_(42417, "new_item", lambda: new_item)
            _l_(42418)
            _n_(42419, "self", lambda: self).tail = _a_(42421, _n_(42420, "self", lambda: self), "head")
            _l_(42422)
        else:
            _n_(42423, "new_item", lambda: new_item).prev = _a_(42425, _n_(42424, "self", lambda: self), "tail")
            _l_(42426)
            _a_(42428, _n_(42427, "self", lambda: self), "tail").next = _n_(42429, "new_item", lambda: new_item)
            _l_(42430)
            _n_(42431, "self", lambda: self).tail = _n_(42432, "new_item", lambda: new_item)
            _l_(42433)
        _n_(42435, "self", lambda: self).count += 1
        _l_(42436)

    def iter(self):
        _l_(42448)

        current = _a_(42439, _n_(42438, "self", lambda: self), "head")
        _l_(42440)
        while _n_(42441, "current", lambda: current):
            _l_(42447)

            item_val = _a_(42443, _n_(42442, "current", lambda: current), "data")
            _l_(42444)
            yield _n_(42445, "item_val", lambda: item_val)
            _l_(42446)

    def print_foward(self):
        _l_(42457)

        for node in _c_(42451, _a_(42450, _n_(42449, "self", lambda: self), "iter")):
            _l_(42456)

            _c_(42454, _n_(42452, "print", lambda: print), _n_(42453, "node", lambda: node))
            _l_(42455)

    def search_item(self, val):
        _l_(42467)

        for node in _c_(42460, _a_(42459, _n_(42458, "self", lambda: self), "iter")):
            _l_(42465)

            if _n_(42461, "val", lambda: val) == _n_(42462, "node", lambda: node):
                _l_(42464)

                aux = True
                _l_(42463)
                return aux
        aux = False
        _l_(42466)
        return aux
items = _c_(42470, _n_(42469, "doubly_linked_list", lambda: doubly_linked_list))
_l_(42471)
_c_(42474, _a_(42473, _n_(42472, "items", lambda: items), "append_item"), 'PHP')
_l_(42475)
_c_(42478, _a_(42477, _n_(42476, "items", lambda: items), "append_item"), 'Python')
_l_(42479)
_c_(42482, _a_(42481, _n_(42480, "items", lambda: items), "append_item"), 'C#')
_l_(42483)
_c_(42486, _a_(42485, _n_(42484, "items", lambda: items), "append_item"), 'C++')
_l_(42487)
_c_(42490, _a_(42489, _n_(42488, "items", lambda: items), "append_item"), 'Java')
_l_(42491)
_c_(42494, _a_(42493, _n_(42492, "items", lambda: items), "append_item"), 'SQL')
_l_(42495)
_c_(42497, _n_(42496, "print", lambda: print), 'Original list:')
_l_(42498)
_c_(42501, _a_(42500, _n_(42499, "items", lambda: items), "print_foward"))
_l_(42502)
_c_(42504, _n_(42503, "print", lambda: print), '\n')
_l_(42505)
if _c_(42508, _a_(42507, _n_(42506, "items", lambda: items), "search_item"), 'SQL'):
    _l_(42515)

    _c_(42510, _n_(42509, "print", lambda: print), 'True')
    _l_(42511)
else:
    _c_(42513, _n_(42512, "print", lambda: print), 'False')
    _l_(42514)
if _c_(42518, _a_(42517, _n_(42516, "items", lambda: items), "search_item"), 'C+'):
    _l_(42525)

    _c_(42520, _n_(42519, "print", lambda: print), 'True')
    _l_(42521)
else:
    _c_(42523, _n_(42522, "print", lambda: print), 'False')
    _l_(42524)