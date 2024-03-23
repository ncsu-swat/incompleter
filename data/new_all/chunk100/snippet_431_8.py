# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node(_n_(43750, "object", lambda: object)):
    _l_(43761)


    def __init__(self, data=None, next=None, prev=None):
        _l_(43760)

        _n_(43751, "self", lambda: self).data = _n_(43752, "data", lambda: data)
        _l_(43753)
        _n_(43754, "self", lambda: self).next = _n_(43755, "next", lambda: next)
        _l_(43756)
        _n_(43757, "self", lambda: self).prev = _n_(43758, "prev", lambda: prev)
        _l_(43759)

class doubly_linked_list(_n_(43762, "object", lambda: object)):
    _l_(43831)


    def __init__(self):
        _l_(43769)

        _n_(43763, "self", lambda: self).head = None
        _l_(43764)
        _n_(43765, "self", lambda: self).tail = None
        _l_(43766)
        _n_(43767, "self", lambda: self).count = 0
        _l_(43768)

    def append_item(self, data):
        _l_(43797)

        new_item = _c_(43772, _n_(43770, "Node", lambda: Node), _n_(43771, "data", lambda: data), None, None)
        _l_(43773)
        if _a_(43775, _n_(43774, "self", lambda: self), "head") is None:
            _l_(43794)

            _n_(43776, "self", lambda: self).head = _n_(43777, "new_item", lambda: new_item)
            _l_(43778)
            _n_(43779, "self", lambda: self).tail = _a_(43781, _n_(43780, "self", lambda: self), "head")
            _l_(43782)
        else:
            _n_(43783, "new_item", lambda: new_item).prev = _a_(43785, _n_(43784, "self", lambda: self), "tail")
            _l_(43786)
            _a_(43788, _n_(43787, "self", lambda: self), "tail").next = _n_(43789, "new_item", lambda: new_item)
            _l_(43790)
            _n_(43791, "self", lambda: self).tail = _n_(43792, "new_item", lambda: new_item)
            _l_(43793)
        _n_(43795, "self", lambda: self).count += 1
        _l_(43796)

    def iter(self):
        _l_(43811)

        current = _a_(43799, _n_(43798, "self", lambda: self), "head")
        _l_(43800)
        while _n_(43801, "current", lambda: current):
            _l_(43810)

            item_val = _a_(43803, _n_(43802, "current", lambda: current), "data")
            _l_(43804)
            current = _a_(43806, _n_(43805, "current", lambda: current), "next")
            _l_(43807)
            yield _n_(43808, "item_val", lambda: item_val)
            _l_(43809)

    def print_foward(self):
        _l_(43820)

        for node in _c_(43814, _a_(43813, _n_(43812, "self", lambda: self), "iter")):
            _l_(43819)

            _c_(43817, _n_(43815, "print", lambda: print), _n_(43816, "node", lambda: node))
            _l_(43818)

    def search_item(self, val):
        _l_(43830)

        for node in _c_(43823, _a_(43822, _n_(43821, "self", lambda: self), "iter")):
            _l_(43828)

            if _n_(43824, "val", lambda: val) == _n_(43825, "node", lambda: node):
                _l_(43827)

                aux = True
                _l_(43826)
                return aux
        aux = False
        _l_(43829)
        return aux
_c_(43834, _a_(43833, _n_(43832, "items", lambda: items), "append_item"), 'PHP')
_l_(43835)
_c_(43838, _a_(43837, _n_(43836, "items", lambda: items), "append_item"), 'Python')
_l_(43839)
_c_(43842, _a_(43841, _n_(43840, "items", lambda: items), "append_item"), 'C#')
_l_(43843)
_c_(43846, _a_(43845, _n_(43844, "items", lambda: items), "append_item"), 'C++')
_l_(43847)
_c_(43850, _a_(43849, _n_(43848, "items", lambda: items), "append_item"), 'Java')
_l_(43851)
_c_(43854, _a_(43853, _n_(43852, "items", lambda: items), "append_item"), 'SQL')
_l_(43855)
_c_(43857, _n_(43856, "print", lambda: print), 'Original list:')
_l_(43858)
_c_(43861, _a_(43860, _n_(43859, "items", lambda: items), "print_foward"))
_l_(43862)
_c_(43864, _n_(43863, "print", lambda: print), '\n')
_l_(43865)
if _c_(43868, _a_(43867, _n_(43866, "items", lambda: items), "search_item"), 'SQL'):
    _l_(43875)

    _c_(43870, _n_(43869, "print", lambda: print), 'True')
    _l_(43871)
else:
    _c_(43873, _n_(43872, "print", lambda: print), 'False')
    _l_(43874)
if _c_(43878, _a_(43877, _n_(43876, "items", lambda: items), "search_item"), 'C+'):
    _l_(43885)

    _c_(43880, _n_(43879, "print", lambda: print), 'True')
    _l_(43881)
else:
    _c_(43883, _n_(43882, "print", lambda: print), 'False')
    _l_(43884)