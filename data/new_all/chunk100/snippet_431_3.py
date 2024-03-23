# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node(_n_(43071, "object", lambda: object)):
    _l_(43082)


    def __init__(self, data=None, next=None, prev=None):
        _l_(43081)

        _n_(43072, "self", lambda: self).data = _n_(43073, "data", lambda: data)
        _l_(43074)
        _n_(43075, "self", lambda: self).next = _n_(43076, "next", lambda: next)
        _l_(43077)
        _n_(43078, "self", lambda: self).prev = _n_(43079, "prev", lambda: prev)
        _l_(43080)

class doubly_linked_list(_n_(43083, "object", lambda: object)):
    _l_(43148)


    def __init__(self):
        _l_(43090)

        _n_(43084, "self", lambda: self).head = None
        _l_(43085)
        _n_(43086, "self", lambda: self).tail = None
        _l_(43087)
        _n_(43088, "self", lambda: self).count = 0
        _l_(43089)

    def append_item(self, data):
        _l_(43114)

        if _a_(43092, _n_(43091, "self", lambda: self), "head") is None:
            _l_(43111)

            _n_(43093, "self", lambda: self).head = _n_(43094, "new_item", lambda: new_item)
            _l_(43095)
            _n_(43096, "self", lambda: self).tail = _a_(43098, _n_(43097, "self", lambda: self), "head")
            _l_(43099)
        else:
            _n_(43100, "new_item", lambda: new_item).prev = _a_(43102, _n_(43101, "self", lambda: self), "tail")
            _l_(43103)
            _a_(43105, _n_(43104, "self", lambda: self), "tail").next = _n_(43106, "new_item", lambda: new_item)
            _l_(43107)
            _n_(43108, "self", lambda: self).tail = _n_(43109, "new_item", lambda: new_item)
            _l_(43110)
        _n_(43112, "self", lambda: self).count += 1
        _l_(43113)

    def iter(self):
        _l_(43128)

        current = _a_(43116, _n_(43115, "self", lambda: self), "head")
        _l_(43117)
        while _n_(43118, "current", lambda: current):
            _l_(43127)

            item_val = _a_(43120, _n_(43119, "current", lambda: current), "data")
            _l_(43121)
            current = _a_(43123, _n_(43122, "current", lambda: current), "next")
            _l_(43124)
            yield _n_(43125, "item_val", lambda: item_val)
            _l_(43126)

    def print_foward(self):
        _l_(43137)

        for node in _c_(43131, _a_(43130, _n_(43129, "self", lambda: self), "iter")):
            _l_(43136)

            _c_(43134, _n_(43132, "print", lambda: print), _n_(43133, "node", lambda: node))
            _l_(43135)

    def search_item(self, val):
        _l_(43147)

        for node in _c_(43140, _a_(43139, _n_(43138, "self", lambda: self), "iter")):
            _l_(43145)

            if _n_(43141, "val", lambda: val) == _n_(43142, "node", lambda: node):
                _l_(43144)

                aux = True
                _l_(43143)
                return aux
        aux = False
        _l_(43146)
        return aux
items = _c_(43150, _n_(43149, "doubly_linked_list", lambda: doubly_linked_list))
_l_(43151)
_c_(43154, _a_(43153, _n_(43152, "items", lambda: items), "append_item"), 'PHP')
_l_(43155)
_c_(43158, _a_(43157, _n_(43156, "items", lambda: items), "append_item"), 'Python')
_l_(43159)
_c_(43162, _a_(43161, _n_(43160, "items", lambda: items), "append_item"), 'C#')
_l_(43163)
_c_(43166, _a_(43165, _n_(43164, "items", lambda: items), "append_item"), 'C++')
_l_(43167)
_c_(43170, _a_(43169, _n_(43168, "items", lambda: items), "append_item"), 'Java')
_l_(43171)
_c_(43174, _a_(43173, _n_(43172, "items", lambda: items), "append_item"), 'SQL')
_l_(43175)
_c_(43177, _n_(43176, "print", lambda: print), 'Original list:')
_l_(43178)
_c_(43181, _a_(43180, _n_(43179, "items", lambda: items), "print_foward"))
_l_(43182)
_c_(43184, _n_(43183, "print", lambda: print), '\n')
_l_(43185)
if _c_(43188, _a_(43187, _n_(43186, "items", lambda: items), "search_item"), 'SQL'):
    _l_(43195)

    _c_(43190, _n_(43189, "print", lambda: print), 'True')
    _l_(43191)
else:
    _c_(43193, _n_(43192, "print", lambda: print), 'False')
    _l_(43194)
if _c_(43198, _a_(43197, _n_(43196, "items", lambda: items), "search_item"), 'C+'):
    _l_(43205)

    _c_(43200, _n_(43199, "print", lambda: print), 'True')
    _l_(43201)
else:
    _c_(43203, _n_(43202, "print", lambda: print), 'False')
    _l_(43204)