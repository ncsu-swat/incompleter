# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node(_n_(43613, "object", lambda: object)):
    _l_(43624)


    def __init__(self, data=None, next=None, prev=None):
        _l_(43623)

        _n_(43614, "self", lambda: self).data = _n_(43615, "data", lambda: data)
        _l_(43616)
        _n_(43617, "self", lambda: self).next = _n_(43618, "next", lambda: next)
        _l_(43619)
        _n_(43620, "self", lambda: self).prev = _n_(43621, "prev", lambda: prev)
        _l_(43622)

class doubly_linked_list(_n_(43625, "object", lambda: object)):
    _l_(43692)


    def __init__(self):
        _l_(43630)

        _n_(43626, "self", lambda: self).tail = None
        _l_(43627)
        _n_(43628, "self", lambda: self).count = 0
        _l_(43629)

    def append_item(self, data):
        _l_(43658)

        new_item = _c_(43633, _n_(43631, "Node", lambda: Node), _n_(43632, "data", lambda: data), None, None)
        _l_(43634)
        if _a_(43636, _n_(43635, "self", lambda: self), "head") is None:
            _l_(43655)

            _n_(43637, "self", lambda: self).head = _n_(43638, "new_item", lambda: new_item)
            _l_(43639)
            _n_(43640, "self", lambda: self).tail = _a_(43642, _n_(43641, "self", lambda: self), "head")
            _l_(43643)
        else:
            _n_(43644, "new_item", lambda: new_item).prev = _a_(43646, _n_(43645, "self", lambda: self), "tail")
            _l_(43647)
            _a_(43649, _n_(43648, "self", lambda: self), "tail").next = _n_(43650, "new_item", lambda: new_item)
            _l_(43651)
            _n_(43652, "self", lambda: self).tail = _n_(43653, "new_item", lambda: new_item)
            _l_(43654)
        _n_(43656, "self", lambda: self).count += 1
        _l_(43657)

    def iter(self):
        _l_(43672)

        current = _a_(43660, _n_(43659, "self", lambda: self), "head")
        _l_(43661)
        while _n_(43662, "current", lambda: current):
            _l_(43671)

            item_val = _a_(43664, _n_(43663, "current", lambda: current), "data")
            _l_(43665)
            current = _a_(43667, _n_(43666, "current", lambda: current), "next")
            _l_(43668)
            yield _n_(43669, "item_val", lambda: item_val)
            _l_(43670)

    def print_foward(self):
        _l_(43681)

        for node in _c_(43675, _a_(43674, _n_(43673, "self", lambda: self), "iter")):
            _l_(43680)

            _c_(43678, _n_(43676, "print", lambda: print), _n_(43677, "node", lambda: node))
            _l_(43679)

    def search_item(self, val):
        _l_(43691)

        for node in _c_(43684, _a_(43683, _n_(43682, "self", lambda: self), "iter")):
            _l_(43689)

            if _n_(43685, "val", lambda: val) == _n_(43686, "node", lambda: node):
                _l_(43688)

                aux = True
                _l_(43687)
                return aux
        aux = False
        _l_(43690)
        return aux
items = _c_(43694, _n_(43693, "doubly_linked_list", lambda: doubly_linked_list))
_l_(43695)
_c_(43698, _a_(43697, _n_(43696, "items", lambda: items), "append_item"), 'PHP')
_l_(43699)
_c_(43702, _a_(43701, _n_(43700, "items", lambda: items), "append_item"), 'Python')
_l_(43703)
_c_(43706, _a_(43705, _n_(43704, "items", lambda: items), "append_item"), 'C#')
_l_(43707)
_c_(43710, _a_(43709, _n_(43708, "items", lambda: items), "append_item"), 'C++')
_l_(43711)
_c_(43714, _a_(43713, _n_(43712, "items", lambda: items), "append_item"), 'Java')
_l_(43715)
_c_(43718, _a_(43717, _n_(43716, "items", lambda: items), "append_item"), 'SQL')
_l_(43719)
_c_(43721, _n_(43720, "print", lambda: print), 'Original list:')
_l_(43722)
_c_(43725, _a_(43724, _n_(43723, "items", lambda: items), "print_foward"))
_l_(43726)
_c_(43728, _n_(43727, "print", lambda: print), '\n')
_l_(43729)
if _c_(43732, _a_(43731, _n_(43730, "items", lambda: items), "search_item"), 'SQL'):
    _l_(43739)

    _c_(43734, _n_(43733, "print", lambda: print), 'True')
    _l_(43735)
else:
    _c_(43737, _n_(43736, "print", lambda: print), 'False')
    _l_(43738)
if _c_(43742, _a_(43741, _n_(43740, "items", lambda: items), "search_item"), 'C+'):
    _l_(43749)

    _c_(43744, _n_(43743, "print", lambda: print), 'True')
    _l_(43745)
else:
    _c_(43747, _n_(43746, "print", lambda: print), 'False')
    _l_(43748)