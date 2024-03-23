# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node(_n_(42798, "object", lambda: object)):
    _l_(42809)


    def __init__(self, data=None, next=None, prev=None):
        _l_(42808)

        _n_(42799, "self", lambda: self).data = _n_(42800, "data", lambda: data)
        _l_(42801)
        _n_(42802, "self", lambda: self).next = _n_(42803, "next", lambda: next)
        _l_(42804)
        _n_(42805, "self", lambda: self).prev = _n_(42806, "prev", lambda: prev)
        _l_(42807)

class doubly_linked_list(_n_(42810, "object", lambda: object)):
    _l_(42877)


    def __init__(self):
        _l_(42815)

        _n_(42811, "self", lambda: self).head = None
        _l_(42812)
        _n_(42813, "self", lambda: self).count = 0
        _l_(42814)

    def append_item(self, data):
        _l_(42843)

        new_item = _c_(42818, _n_(42816, "Node", lambda: Node), _n_(42817, "data", lambda: data), None, None)
        _l_(42819)
        if _a_(42821, _n_(42820, "self", lambda: self), "head") is None:
            _l_(42840)

            _n_(42822, "self", lambda: self).head = _n_(42823, "new_item", lambda: new_item)
            _l_(42824)
            _n_(42825, "self", lambda: self).tail = _a_(42827, _n_(42826, "self", lambda: self), "head")
            _l_(42828)
        else:
            _n_(42829, "new_item", lambda: new_item).prev = _a_(42831, _n_(42830, "self", lambda: self), "tail")
            _l_(42832)
            _a_(42834, _n_(42833, "self", lambda: self), "tail").next = _n_(42835, "new_item", lambda: new_item)
            _l_(42836)
            _n_(42837, "self", lambda: self).tail = _n_(42838, "new_item", lambda: new_item)
            _l_(42839)
        _n_(42841, "self", lambda: self).count += 1
        _l_(42842)

    def iter(self):
        _l_(42857)

        current = _a_(42845, _n_(42844, "self", lambda: self), "head")
        _l_(42846)
        while _n_(42847, "current", lambda: current):
            _l_(42856)

            item_val = _a_(42849, _n_(42848, "current", lambda: current), "data")
            _l_(42850)
            current = _a_(42852, _n_(42851, "current", lambda: current), "next")
            _l_(42853)
            yield _n_(42854, "item_val", lambda: item_val)
            _l_(42855)

    def print_foward(self):
        _l_(42866)

        for node in _c_(42860, _a_(42859, _n_(42858, "self", lambda: self), "iter")):
            _l_(42865)

            _c_(42863, _n_(42861, "print", lambda: print), _n_(42862, "node", lambda: node))
            _l_(42864)

    def search_item(self, val):
        _l_(42876)

        for node in _c_(42869, _a_(42868, _n_(42867, "self", lambda: self), "iter")):
            _l_(42874)

            if _n_(42870, "val", lambda: val) == _n_(42871, "node", lambda: node):
                _l_(42873)

                aux = True
                _l_(42872)
                return aux
        aux = False
        _l_(42875)
        return aux
items = _c_(42879, _n_(42878, "doubly_linked_list", lambda: doubly_linked_list))
_l_(42880)
_c_(42883, _a_(42882, _n_(42881, "items", lambda: items), "append_item"), 'PHP')
_l_(42884)
_c_(42887, _a_(42886, _n_(42885, "items", lambda: items), "append_item"), 'Python')
_l_(42888)
_c_(42891, _a_(42890, _n_(42889, "items", lambda: items), "append_item"), 'C#')
_l_(42892)
_c_(42895, _a_(42894, _n_(42893, "items", lambda: items), "append_item"), 'C++')
_l_(42896)
_c_(42899, _a_(42898, _n_(42897, "items", lambda: items), "append_item"), 'Java')
_l_(42900)
_c_(42903, _a_(42902, _n_(42901, "items", lambda: items), "append_item"), 'SQL')
_l_(42904)
_c_(42906, _n_(42905, "print", lambda: print), 'Original list:')
_l_(42907)
_c_(42910, _a_(42909, _n_(42908, "items", lambda: items), "print_foward"))
_l_(42911)
_c_(42913, _n_(42912, "print", lambda: print), '\n')
_l_(42914)
if _c_(42917, _a_(42916, _n_(42915, "items", lambda: items), "search_item"), 'SQL'):
    _l_(42924)

    _c_(42919, _n_(42918, "print", lambda: print), 'True')
    _l_(42920)
else:
    _c_(42922, _n_(42921, "print", lambda: print), 'False')
    _l_(42923)
if _c_(42927, _a_(42926, _n_(42925, "items", lambda: items), "search_item"), 'C+'):
    _l_(42934)

    _c_(42929, _n_(42928, "print", lambda: print), 'True')
    _l_(42930)
else:
    _c_(42932, _n_(42931, "print", lambda: print), 'False')
    _l_(42933)