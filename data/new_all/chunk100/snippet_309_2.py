# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node(_n_(27936, "object", lambda: object)):
    _l_(27947)


    def __init__(self, value=None, next=None, prev=None):
        _l_(27946)

        _n_(27937, "self", lambda: self).value = _n_(27938, "value", lambda: value)
        _l_(27939)
        _n_(27940, "self", lambda: self).next = _n_(27941, "next", lambda: next)
        _l_(27942)
        _n_(27943, "self", lambda: self).prev = _n_(27944, "prev", lambda: prev)
        _l_(27945)

class doubly_linked_list(_n_(27948, "object", lambda: object)):
    _l_(28072)


    def __init__(self):
        _l_(27955)

        _n_(27949, "self", lambda: self).head = None
        _l_(27950)
        _n_(27951, "self", lambda: self).tail = None
        _l_(27952)
        _n_(27953, "self", lambda: self).count = 0
        _l_(27954)

    def append_item(self, value):
        _l_(27983)

        new_item = _c_(27958, _n_(27956, "Node", lambda: Node), _n_(27957, "value", lambda: value), None, None)
        _l_(27959)
        if _a_(27961, _n_(27960, "self", lambda: self), "head") is None:
            _l_(27980)

            _n_(27962, "self", lambda: self).head = _n_(27963, "new_item", lambda: new_item)
            _l_(27964)
            _n_(27965, "self", lambda: self).tail = _a_(27967, _n_(27966, "self", lambda: self), "head")
            _l_(27968)
        else:
            _n_(27969, "new_item", lambda: new_item).prev = _a_(27971, _n_(27970, "self", lambda: self), "tail")
            _l_(27972)
            _a_(27974, _n_(27973, "self", lambda: self), "tail").next = _n_(27975, "new_item", lambda: new_item)
            _l_(27976)
            _n_(27977, "self", lambda: self).tail = _n_(27978, "new_item", lambda: new_item)
            _l_(27979)
        _n_(27981, "self", lambda: self).count += 1
        _l_(27982)

    def iter(self):
        _l_(27994)

        current = _a_(27985, _n_(27984, "self", lambda: self), "head")
        _l_(27986)
        while _n_(27987, "current", lambda: current):
            _l_(27993)

            item_val = _a_(27989, _n_(27988, "current", lambda: current), "value")
            _l_(27990)
            yield _n_(27991, "item_val", lambda: item_val)
            _l_(27992)

    def print_foward(self):
        _l_(28003)

        for node in _c_(27997, _a_(27996, _n_(27995, "self", lambda: self), "iter")):
            _l_(28002)

            _c_(28000, _n_(27998, "print", lambda: print), _n_(27999, "node", lambda: node))
            _l_(28001)

    def search_item(self, val):
        _l_(28013)

        for node in _c_(28006, _a_(28005, _n_(28004, "self", lambda: self), "iter")):
            _l_(28011)

            if _n_(28007, "val", lambda: val) == _n_(28008, "node", lambda: node):
                _l_(28010)

                aux = True
                _l_(28009)
                return aux
        aux = False
        _l_(28012)
        return aux

    def delete(self, value):
        _l_(28071)

        current = _a_(28015, _n_(28014, "self", lambda: self), "head")
        _l_(28016)
        node_deleted = False
        _l_(28017)
        if _n_(28018, "current", lambda: current) is None:
            _l_(28066)

            node_deleted = False
            _l_(28019)
        elif _a_(28021, _n_(28020, "current", lambda: current), "value") == _n_(28022, "value", lambda: value):
            _l_(28065)

            _n_(28023, "self", lambda: self).head = _a_(28025, _n_(28024, "current", lambda: current), "next")
            _l_(28026)
            _a_(28028, _n_(28027, "self", lambda: self), "head").prev = None
            _l_(28029)
            node_deleted = True
            _l_(28030)
        elif _a_(28033, _a_(28032, _n_(28031, "self", lambda: self), "tail"), "value") == _n_(28034, "value", lambda: value):
            _l_(28064)

            _n_(28035, "self", lambda: self).tail = _a_(28038, _a_(28037, _n_(28036, "self", lambda: self), "tail"), "prev")
            _l_(28039)
            _a_(28041, _n_(28040, "self", lambda: self), "tail").next = None
            _l_(28042)
            node_deleted = True
            _l_(28043)
        else:
            while _n_(28044, "current", lambda: current):
                _l_(28063)

                if _a_(28046, _n_(28045, "current", lambda: current), "value") == _n_(28047, "value", lambda: value):
                    _l_(28059)

                    _a_(28049, _n_(28048, "current", lambda: current), "prev").next = _a_(28051, _n_(28050, "current", lambda: current), "next")
                    _l_(28052)
                    _a_(28054, _n_(28053, "current", lambda: current), "next").prev = _a_(28056, _n_(28055, "current", lambda: current), "prev")
                    _l_(28057)
                    node_deleted = True
                    _l_(28058)
                current = _a_(28061, _n_(28060, "current", lambda: current), "next")
                _l_(28062)
        if _n_(28067, "node_deleted", lambda: node_deleted):
            _l_(28070)

            _n_(28068, "self", lambda: self).count -= 1
            _l_(28069)
items = _c_(28074, _n_(28073, "doubly_linked_list", lambda: doubly_linked_list))
_l_(28075)
_c_(28078, _a_(28077, _n_(28076, "items", lambda: items), "append_item"), 'PHP')
_l_(28079)
_c_(28082, _a_(28081, _n_(28080, "items", lambda: items), "append_item"), 'Python')
_l_(28083)
_c_(28086, _a_(28085, _n_(28084, "items", lambda: items), "append_item"), 'C#')
_l_(28087)
_c_(28090, _a_(28089, _n_(28088, "items", lambda: items), "append_item"), 'C++')
_l_(28091)
_c_(28094, _a_(28093, _n_(28092, "items", lambda: items), "append_item"), 'Java')
_l_(28095)
_c_(28098, _a_(28097, _n_(28096, "items", lambda: items), "append_item"), 'SQL')
_l_(28099)
_c_(28101, _n_(28100, "print", lambda: print), 'Original list:')
_l_(28102)
_c_(28105, _a_(28104, _n_(28103, "items", lambda: items), "print_foward"))
_l_(28106)
_c_(28109, _a_(28108, _n_(28107, "items", lambda: items), "delete"), 'Java')
_l_(28110)
_c_(28113, _a_(28112, _n_(28111, "items", lambda: items), "delete"), 'Python')
_l_(28114)
_c_(28116, _n_(28115, "print", lambda: print), '\nList after deleting two items:')
_l_(28117)
_c_(28120, _a_(28119, _n_(28118, "items", lambda: items), "print_foward"))
_l_(28121)