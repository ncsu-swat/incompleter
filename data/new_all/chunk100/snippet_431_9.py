# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node(_n_(43886, "object", lambda: object)):
    _l_(43894)


    def __init__(self, data=None, next=None, prev=None):
        _l_(43893)

        _n_(43887, "self", lambda: self).data = _n_(43888, "data", lambda: data)
        _l_(43889)
        _n_(43890, "self", lambda: self).prev = _n_(43891, "prev", lambda: prev)
        _l_(43892)

class doubly_linked_list(_n_(43895, "object", lambda: object)):
    _l_(43964)


    def __init__(self):
        _l_(43902)

        _n_(43896, "self", lambda: self).head = None
        _l_(43897)
        _n_(43898, "self", lambda: self).tail = None
        _l_(43899)
        _n_(43900, "self", lambda: self).count = 0
        _l_(43901)

    def append_item(self, data):
        _l_(43930)

        new_item = _c_(43905, _n_(43903, "Node", lambda: Node), _n_(43904, "data", lambda: data), None, None)
        _l_(43906)
        if _a_(43908, _n_(43907, "self", lambda: self), "head") is None:
            _l_(43927)

            _n_(43909, "self", lambda: self).head = _n_(43910, "new_item", lambda: new_item)
            _l_(43911)
            _n_(43912, "self", lambda: self).tail = _a_(43914, _n_(43913, "self", lambda: self), "head")
            _l_(43915)
        else:
            _n_(43916, "new_item", lambda: new_item).prev = _a_(43918, _n_(43917, "self", lambda: self), "tail")
            _l_(43919)
            _a_(43921, _n_(43920, "self", lambda: self), "tail").next = _n_(43922, "new_item", lambda: new_item)
            _l_(43923)
            _n_(43924, "self", lambda: self).tail = _n_(43925, "new_item", lambda: new_item)
            _l_(43926)
        _n_(43928, "self", lambda: self).count += 1
        _l_(43929)

    def iter(self):
        _l_(43944)

        current = _a_(43932, _n_(43931, "self", lambda: self), "head")
        _l_(43933)
        while _n_(43934, "current", lambda: current):
            _l_(43943)

            item_val = _a_(43936, _n_(43935, "current", lambda: current), "data")
            _l_(43937)
            current = _a_(43939, _n_(43938, "current", lambda: current), "next")
            _l_(43940)
            yield _n_(43941, "item_val", lambda: item_val)
            _l_(43942)

    def print_foward(self):
        _l_(43953)

        for node in _c_(43947, _a_(43946, _n_(43945, "self", lambda: self), "iter")):
            _l_(43952)

            _c_(43950, _n_(43948, "print", lambda: print), _n_(43949, "node", lambda: node))
            _l_(43951)

    def search_item(self, val):
        _l_(43963)

        for node in _c_(43956, _a_(43955, _n_(43954, "self", lambda: self), "iter")):
            _l_(43961)

            if _n_(43957, "val", lambda: val) == _n_(43958, "node", lambda: node):
                _l_(43960)

                aux = True
                _l_(43959)
                return aux
        aux = False
        _l_(43962)
        return aux
items = _c_(43966, _n_(43965, "doubly_linked_list", lambda: doubly_linked_list))
_l_(43967)
_c_(43970, _a_(43969, _n_(43968, "items", lambda: items), "append_item"), 'PHP')
_l_(43971)
_c_(43974, _a_(43973, _n_(43972, "items", lambda: items), "append_item"), 'Python')
_l_(43975)
_c_(43978, _a_(43977, _n_(43976, "items", lambda: items), "append_item"), 'C#')
_l_(43979)
_c_(43982, _a_(43981, _n_(43980, "items", lambda: items), "append_item"), 'C++')
_l_(43983)
_c_(43986, _a_(43985, _n_(43984, "items", lambda: items), "append_item"), 'Java')
_l_(43987)
_c_(43990, _a_(43989, _n_(43988, "items", lambda: items), "append_item"), 'SQL')
_l_(43991)
_c_(43993, _n_(43992, "print", lambda: print), 'Original list:')
_l_(43994)
_c_(43997, _a_(43996, _n_(43995, "items", lambda: items), "print_foward"))
_l_(43998)
_c_(44000, _n_(43999, "print", lambda: print), '\n')
_l_(44001)
if _c_(44004, _a_(44003, _n_(44002, "items", lambda: items), "search_item"), 'SQL'):
    _l_(44011)

    _c_(44006, _n_(44005, "print", lambda: print), 'True')
    _l_(44007)
else:
    _c_(44009, _n_(44008, "print", lambda: print), 'False')
    _l_(44010)
if _c_(44014, _a_(44013, _n_(44012, "items", lambda: items), "search_item"), 'C+'):
    _l_(44021)

    _c_(44016, _n_(44015, "print", lambda: print), 'True')
    _l_(44017)
else:
    _c_(44019, _n_(44018, "print", lambda: print), 'False')
    _l_(44020)