# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node(_n_(13438, "object", lambda: object)):
    _l_(13449)


    def __init__(self, data=None, next=None, prev=None):
        _l_(13448)

        _n_(13439, "self", lambda: self).data = _n_(13440, "data", lambda: data)
        _l_(13441)
        _n_(13442, "self", lambda: self).next = _n_(13443, "next", lambda: next)
        _l_(13444)
        _n_(13445, "self", lambda: self).prev = _n_(13446, "prev", lambda: prev)
        _l_(13447)

class doubly_linked_list(_n_(13450, "object", lambda: object)):
    _l_(13505)


    def __init__(self):
        _l_(13457)

        _n_(13451, "self", lambda: self).head = None
        _l_(13452)
        _n_(13453, "self", lambda: self).tail = None
        _l_(13454)
        _n_(13455, "self", lambda: self).count = 0
        _l_(13456)

    def append_item(self, data):
        _l_(13481)

        if _a_(13459, _n_(13458, "self", lambda: self), "head") is None:
            _l_(13478)

            _n_(13460, "self", lambda: self).head = _n_(13461, "new_item", lambda: new_item)
            _l_(13462)
            _n_(13463, "self", lambda: self).tail = _a_(13465, _n_(13464, "self", lambda: self), "head")
            _l_(13466)
        else:
            _n_(13467, "new_item", lambda: new_item).prev = _a_(13469, _n_(13468, "self", lambda: self), "tail")
            _l_(13470)
            _a_(13472, _n_(13471, "self", lambda: self), "tail").next = _n_(13473, "new_item", lambda: new_item)
            _l_(13474)
            _n_(13475, "self", lambda: self).tail = _n_(13476, "new_item", lambda: new_item)
            _l_(13477)
        _n_(13479, "self", lambda: self).count += 1
        _l_(13480)

    def print_foward(self):
        _l_(13490)

        for node in _c_(13484, _a_(13483, _n_(13482, "self", lambda: self), "iter")):
            _l_(13489)

            _c_(13487, _n_(13485, "print", lambda: print), _n_(13486, "node", lambda: node))
            _l_(13488)

    def iter(self):
        _l_(13504)

        current = _a_(13492, _n_(13491, "self", lambda: self), "head")
        _l_(13493)
        while _n_(13494, "current", lambda: current):
            _l_(13503)

            item_val = _a_(13496, _n_(13495, "current", lambda: current), "data")
            _l_(13497)
            current = _a_(13499, _n_(13498, "current", lambda: current), "next")
            _l_(13500)
            yield _n_(13501, "item_val", lambda: item_val)
            _l_(13502)
items = _c_(13507, _n_(13506, "doubly_linked_list", lambda: doubly_linked_list))
_l_(13508)
_c_(13511, _a_(13510, _n_(13509, "items", lambda: items), "append_item"), 'PHP')
_l_(13512)
_c_(13515, _a_(13514, _n_(13513, "items", lambda: items), "append_item"), 'Python')
_l_(13516)
_c_(13519, _a_(13518, _n_(13517, "items", lambda: items), "append_item"), 'C#')
_l_(13520)
_c_(13523, _a_(13522, _n_(13521, "items", lambda: items), "append_item"), 'C++')
_l_(13524)
_c_(13527, _a_(13526, _n_(13525, "items", lambda: items), "append_item"), 'Java')
_l_(13528)
_c_(13530, _n_(13529, "print", lambda: print), 'Items in the Doubly linked list: ')
_l_(13531)
_c_(13534, _a_(13533, _n_(13532, "items", lambda: items), "print_foward"))
_l_(13535)