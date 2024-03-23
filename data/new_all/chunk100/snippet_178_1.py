# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node(_n_(12843, "object", lambda: object)):
    _l_(12851)


    def __init__(self, data=None, next=None, prev=None):
        _l_(12850)

        _n_(12844, "self", lambda: self).data = _n_(12845, "data", lambda: data)
        _l_(12846)
        _n_(12847, "self", lambda: self).next = _n_(12848, "next", lambda: next)
        _l_(12849)

class doubly_linked_list(_n_(12852, "object", lambda: object)):
    _l_(12911)


    def __init__(self):
        _l_(12859)

        _n_(12853, "self", lambda: self).head = None
        _l_(12854)
        _n_(12855, "self", lambda: self).tail = None
        _l_(12856)
        _n_(12857, "self", lambda: self).count = 0
        _l_(12858)

    def append_item(self, data):
        _l_(12887)

        new_item = _c_(12862, _n_(12860, "Node", lambda: Node), _n_(12861, "data", lambda: data), None, None)
        _l_(12863)
        if _a_(12865, _n_(12864, "self", lambda: self), "head") is None:
            _l_(12884)

            _n_(12866, "self", lambda: self).head = _n_(12867, "new_item", lambda: new_item)
            _l_(12868)
            _n_(12869, "self", lambda: self).tail = _a_(12871, _n_(12870, "self", lambda: self), "head")
            _l_(12872)
        else:
            _n_(12873, "new_item", lambda: new_item).prev = _a_(12875, _n_(12874, "self", lambda: self), "tail")
            _l_(12876)
            _a_(12878, _n_(12877, "self", lambda: self), "tail").next = _n_(12879, "new_item", lambda: new_item)
            _l_(12880)
            _n_(12881, "self", lambda: self).tail = _n_(12882, "new_item", lambda: new_item)
            _l_(12883)
        _n_(12885, "self", lambda: self).count += 1
        _l_(12886)

    def print_foward(self):
        _l_(12896)

        for node in _c_(12890, _a_(12889, _n_(12888, "self", lambda: self), "iter")):
            _l_(12895)

            _c_(12893, _n_(12891, "print", lambda: print), _n_(12892, "node", lambda: node))
            _l_(12894)

    def iter(self):
        _l_(12910)

        current = _a_(12898, _n_(12897, "self", lambda: self), "head")
        _l_(12899)
        while _n_(12900, "current", lambda: current):
            _l_(12909)

            item_val = _a_(12902, _n_(12901, "current", lambda: current), "data")
            _l_(12903)
            current = _a_(12905, _n_(12904, "current", lambda: current), "next")
            _l_(12906)
            yield _n_(12907, "item_val", lambda: item_val)
            _l_(12908)
items = _c_(12913, _n_(12912, "doubly_linked_list", lambda: doubly_linked_list))
_l_(12914)
_c_(12917, _a_(12916, _n_(12915, "items", lambda: items), "append_item"), 'PHP')
_l_(12918)
_c_(12921, _a_(12920, _n_(12919, "items", lambda: items), "append_item"), 'Python')
_l_(12922)
_c_(12925, _a_(12924, _n_(12923, "items", lambda: items), "append_item"), 'C#')
_l_(12926)
_c_(12929, _a_(12928, _n_(12927, "items", lambda: items), "append_item"), 'C++')
_l_(12930)
_c_(12933, _a_(12932, _n_(12931, "items", lambda: items), "append_item"), 'Java')
_l_(12934)
_c_(12936, _n_(12935, "print", lambda: print), 'Items in the Doubly linked list: ')
_l_(12937)
_c_(12940, _a_(12939, _n_(12938, "items", lambda: items), "print_foward"))
_l_(12941)