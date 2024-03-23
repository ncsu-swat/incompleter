# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node(_n_(42662, "object", lambda: object)):
    _l_(42670)


    def __init__(self, data=None, next=None, prev=None):
        _l_(42669)

        _n_(42663, "self", lambda: self).next = _n_(42664, "next", lambda: next)
        _l_(42665)
        _n_(42666, "self", lambda: self).prev = _n_(42667, "prev", lambda: prev)
        _l_(42668)

class doubly_linked_list(_n_(42671, "object", lambda: object)):
    _l_(42740)


    def __init__(self):
        _l_(42678)

        _n_(42672, "self", lambda: self).head = None
        _l_(42673)
        _n_(42674, "self", lambda: self).tail = None
        _l_(42675)
        _n_(42676, "self", lambda: self).count = 0
        _l_(42677)

    def append_item(self, data):
        _l_(42706)

        new_item = _c_(42681, _n_(42679, "Node", lambda: Node), _n_(42680, "data", lambda: data), None, None)
        _l_(42682)
        if _a_(42684, _n_(42683, "self", lambda: self), "head") is None:
            _l_(42703)

            _n_(42685, "self", lambda: self).head = _n_(42686, "new_item", lambda: new_item)
            _l_(42687)
            _n_(42688, "self", lambda: self).tail = _a_(42690, _n_(42689, "self", lambda: self), "head")
            _l_(42691)
        else:
            _n_(42692, "new_item", lambda: new_item).prev = _a_(42694, _n_(42693, "self", lambda: self), "tail")
            _l_(42695)
            _a_(42697, _n_(42696, "self", lambda: self), "tail").next = _n_(42698, "new_item", lambda: new_item)
            _l_(42699)
            _n_(42700, "self", lambda: self).tail = _n_(42701, "new_item", lambda: new_item)
            _l_(42702)
        _n_(42704, "self", lambda: self).count += 1
        _l_(42705)

    def iter(self):
        _l_(42720)

        current = _a_(42708, _n_(42707, "self", lambda: self), "head")
        _l_(42709)
        while _n_(42710, "current", lambda: current):
            _l_(42719)

            item_val = _a_(42712, _n_(42711, "current", lambda: current), "data")
            _l_(42713)
            current = _a_(42715, _n_(42714, "current", lambda: current), "next")
            _l_(42716)
            yield _n_(42717, "item_val", lambda: item_val)
            _l_(42718)

    def print_foward(self):
        _l_(42729)

        for node in _c_(42723, _a_(42722, _n_(42721, "self", lambda: self), "iter")):
            _l_(42728)

            _c_(42726, _n_(42724, "print", lambda: print), _n_(42725, "node", lambda: node))
            _l_(42727)

    def search_item(self, val):
        _l_(42739)

        for node in _c_(42732, _a_(42731, _n_(42730, "self", lambda: self), "iter")):
            _l_(42737)

            if _n_(42733, "val", lambda: val) == _n_(42734, "node", lambda: node):
                _l_(42736)

                aux = True
                _l_(42735)
                return aux
        aux = False
        _l_(42738)
        return aux
items = _c_(42742, _n_(42741, "doubly_linked_list", lambda: doubly_linked_list))
_l_(42743)
_c_(42746, _a_(42745, _n_(42744, "items", lambda: items), "append_item"), 'PHP')
_l_(42747)
_c_(42750, _a_(42749, _n_(42748, "items", lambda: items), "append_item"), 'Python')
_l_(42751)
_c_(42754, _a_(42753, _n_(42752, "items", lambda: items), "append_item"), 'C#')
_l_(42755)
_c_(42758, _a_(42757, _n_(42756, "items", lambda: items), "append_item"), 'C++')
_l_(42759)
_c_(42762, _a_(42761, _n_(42760, "items", lambda: items), "append_item"), 'Java')
_l_(42763)
_c_(42766, _a_(42765, _n_(42764, "items", lambda: items), "append_item"), 'SQL')
_l_(42767)
_c_(42769, _n_(42768, "print", lambda: print), 'Original list:')
_l_(42770)
_c_(42773, _a_(42772, _n_(42771, "items", lambda: items), "print_foward"))
_l_(42774)
_c_(42776, _n_(42775, "print", lambda: print), '\n')
_l_(42777)
if _c_(42780, _a_(42779, _n_(42778, "items", lambda: items), "search_item"), 'SQL'):
    _l_(42787)

    _c_(42782, _n_(42781, "print", lambda: print), 'True')
    _l_(42783)
else:
    _c_(42785, _n_(42784, "print", lambda: print), 'False')
    _l_(42786)
if _c_(42790, _a_(42789, _n_(42788, "items", lambda: items), "search_item"), 'C+'):
    _l_(42797)

    _c_(42792, _n_(42791, "print", lambda: print), 'True')
    _l_(42793)
else:
    _c_(42795, _n_(42794, "print", lambda: print), 'False')
    _l_(42796)