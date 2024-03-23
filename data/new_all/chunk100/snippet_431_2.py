# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node(_n_(42935, "object", lambda: object)):
    _l_(42946)


    def __init__(self, data=None, next=None, prev=None):
        _l_(42945)

        _n_(42936, "self", lambda: self).data = _n_(42937, "data", lambda: data)
        _l_(42938)
        _n_(42939, "self", lambda: self).next = _n_(42940, "next", lambda: next)
        _l_(42941)
        _n_(42942, "self", lambda: self).prev = _n_(42943, "prev", lambda: prev)
        _l_(42944)

class doubly_linked_list(_n_(42947, "object", lambda: object)):
    _l_(43013)


    def __init__(self):
        _l_(42954)

        _n_(42948, "self", lambda: self).head = None
        _l_(42949)
        _n_(42950, "self", lambda: self).tail = None
        _l_(42951)
        _n_(42952, "self", lambda: self).count = 0
        _l_(42953)

    def append_item(self, data):
        _l_(42982)

        new_item = _c_(42957, _n_(42955, "Node", lambda: Node), _n_(42956, "data", lambda: data), None, None)
        _l_(42958)
        if _a_(42960, _n_(42959, "self", lambda: self), "head") is None:
            _l_(42979)

            _n_(42961, "self", lambda: self).head = _n_(42962, "new_item", lambda: new_item)
            _l_(42963)
            _n_(42964, "self", lambda: self).tail = _a_(42966, _n_(42965, "self", lambda: self), "head")
            _l_(42967)
        else:
            _n_(42968, "new_item", lambda: new_item).prev = _a_(42970, _n_(42969, "self", lambda: self), "tail")
            _l_(42971)
            _a_(42973, _n_(42972, "self", lambda: self), "tail").next = _n_(42974, "new_item", lambda: new_item)
            _l_(42975)
            _n_(42976, "self", lambda: self).tail = _n_(42977, "new_item", lambda: new_item)
            _l_(42978)
        _n_(42980, "self", lambda: self).count += 1
        _l_(42981)

    def iter(self):
        _l_(42993)

        current = _a_(42984, _n_(42983, "self", lambda: self), "head")
        _l_(42985)
        while _n_(42986, "current", lambda: current):
            _l_(42992)

            item_val = _a_(42988, _n_(42987, "current", lambda: current), "data")
            _l_(42989)
            yield _n_(42990, "item_val", lambda: item_val)
            _l_(42991)

    def print_foward(self):
        _l_(43002)

        for node in _c_(42996, _a_(42995, _n_(42994, "self", lambda: self), "iter")):
            _l_(43001)

            _c_(42999, _n_(42997, "print", lambda: print), _n_(42998, "node", lambda: node))
            _l_(43000)

    def search_item(self, val):
        _l_(43012)

        for node in _c_(43005, _a_(43004, _n_(43003, "self", lambda: self), "iter")):
            _l_(43010)

            if _n_(43006, "val", lambda: val) == _n_(43007, "node", lambda: node):
                _l_(43009)

                aux = True
                _l_(43008)
                return aux
        aux = False
        _l_(43011)
        return aux
items = _c_(43015, _n_(43014, "doubly_linked_list", lambda: doubly_linked_list))
_l_(43016)
_c_(43019, _a_(43018, _n_(43017, "items", lambda: items), "append_item"), 'PHP')
_l_(43020)
_c_(43023, _a_(43022, _n_(43021, "items", lambda: items), "append_item"), 'Python')
_l_(43024)
_c_(43027, _a_(43026, _n_(43025, "items", lambda: items), "append_item"), 'C#')
_l_(43028)
_c_(43031, _a_(43030, _n_(43029, "items", lambda: items), "append_item"), 'C++')
_l_(43032)
_c_(43035, _a_(43034, _n_(43033, "items", lambda: items), "append_item"), 'Java')
_l_(43036)
_c_(43039, _a_(43038, _n_(43037, "items", lambda: items), "append_item"), 'SQL')
_l_(43040)
_c_(43042, _n_(43041, "print", lambda: print), 'Original list:')
_l_(43043)
_c_(43046, _a_(43045, _n_(43044, "items", lambda: items), "print_foward"))
_l_(43047)
_c_(43049, _n_(43048, "print", lambda: print), '\n')
_l_(43050)
if _c_(43053, _a_(43052, _n_(43051, "items", lambda: items), "search_item"), 'SQL'):
    _l_(43060)

    _c_(43055, _n_(43054, "print", lambda: print), 'True')
    _l_(43056)
else:
    _c_(43058, _n_(43057, "print", lambda: print), 'False')
    _l_(43059)
if _c_(43063, _a_(43062, _n_(43061, "items", lambda: items), "search_item"), 'C+'):
    _l_(43070)

    _c_(43065, _n_(43064, "print", lambda: print), 'True')
    _l_(43066)
else:
    _c_(43068, _n_(43067, "print", lambda: print), 'False')
    _l_(43069)