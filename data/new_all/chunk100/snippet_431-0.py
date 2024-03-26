# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node(_n_(115947, "object", lambda: object)):
    _l_(115958)


    def __init__(self, data=None, next=None, prev=None):
        _l_(115957)

        _n_(115948, "self", lambda: self).data = _n_(115949, "data", lambda: data)
        _l_(115950)
        _n_(115951, "self", lambda: self).next = _n_(115952, "next", lambda: next)
        _l_(115953)
        _n_(115954, "self", lambda: self).prev = _n_(115955, "prev", lambda: prev)
        _l_(115956)

class doubly_linked_list(_n_(115959, "object", lambda: object)):
    _l_(116028)


    def __init__(self):
        _l_(115966)

        _n_(115960, "self", lambda: self).head = None
        _l_(115961)
        _n_(115962, "self", lambda: self).tail = None
        _l_(115963)
        _n_(115964, "self", lambda: self).count = 0
        _l_(115965)

    def append_item(self, data):
        _l_(115994)

        new_item = _c_(115969, _n_(115967, "Node", lambda: Node), _n_(115968, "data", lambda: data), None, None)
        _l_(115970)
        if _a_(115972, _n_(115971, "self", lambda: self), "head") is None:
            _l_(115991)

            _n_(115973, "self", lambda: self).head = _n_(115974, "new_item", lambda: new_item)
            _l_(115975)
            _n_(115976, "self", lambda: self).tail = _a_(115978, _n_(115977, "self", lambda: self), "head")
            _l_(115979)
        else:
            _n_(115980, "new_item", lambda: new_item).prev = _a_(115982, _n_(115981, "self", lambda: self), "tail")
            _l_(115983)
            _a_(115985, _n_(115984, "self", lambda: self), "tail").next = _n_(115986, "new_item", lambda: new_item)
            _l_(115987)
            _n_(115988, "self", lambda: self).tail = _n_(115989, "new_item", lambda: new_item)
            _l_(115990)
        _n_(115992, "self", lambda: self).count += 1
        _l_(115993)

    def iter(self):
        _l_(116008)

        current = _a_(115996, _n_(115995, "self", lambda: self), "head")
        _l_(115997)
        while _n_(115998, "current", lambda: current):
            _l_(116007)

            item_val = _a_(116000, _n_(115999, "current", lambda: current), "data")
            _l_(116001)
            current = _a_(116003, _n_(116002, "current", lambda: current), "next")
            _l_(116004)
            yield _n_(116005, "item_val", lambda: item_val)
            _l_(116006)

    def print_foward(self):
        _l_(116017)

        for node in _c_(116011, _a_(116010, _n_(116009, "self", lambda: self), "iter")):
            _l_(116016)

            _c_(116014, _n_(116012, "print", lambda: print), _n_(116013, "node", lambda: node))
            _l_(116015)

    def search_item(self, val):
        _l_(116027)

        for node in _c_(116020, _a_(116019, _n_(116018, "self", lambda: self), "iter")):
            _l_(116025)

            if _n_(116021, "val", lambda: val) == _n_(116022, "node", lambda: node):
                _l_(116024)

                aux = True
                _l_(116023)
                return aux
        aux = False
        _l_(116026)
        return aux
_c_(116031, _a_(116030, _n_(116029, "items", lambda: items), "append_item"), 'PHP')
_l_(116032)
_c_(116035, _a_(116034, _n_(116033, "items", lambda: items), "append_item"), 'Python')
_l_(116036)
_c_(116039, _a_(116038, _n_(116037, "items", lambda: items), "append_item"), 'C#')
_l_(116040)
_c_(116043, _a_(116042, _n_(116041, "items", lambda: items), "append_item"), 'C++')
_l_(116044)
_c_(116047, _a_(116046, _n_(116045, "items", lambda: items), "append_item"), 'Java')
_l_(116048)
_c_(116051, _a_(116050, _n_(116049, "items", lambda: items), "append_item"), 'SQL')
_l_(116052)
_c_(116054, _n_(116053, "print", lambda: print), 'Original list:')
_l_(116055)
_c_(116058, _a_(116057, _n_(116056, "items", lambda: items), "print_foward"))
_l_(116059)
_c_(116061, _n_(116060, "print", lambda: print), '\n')
_l_(116062)
if _c_(116065, _a_(116064, _n_(116063, "items", lambda: items), "search_item"), 'SQL'):
    _l_(116072)

    _c_(116067, _n_(116066, "print", lambda: print), 'True')
    _l_(116068)
else:
    _c_(116070, _n_(116069, "print", lambda: print), 'False')
    _l_(116071)
if _c_(116075, _a_(116074, _n_(116073, "items", lambda: items), "search_item"), 'C+'):
    _l_(116082)

    _c_(116077, _n_(116076, "print", lambda: print), 'True')
    _l_(116078)
else:
    _c_(116080, _n_(116079, "print", lambda: print), 'False')
    _l_(116081)