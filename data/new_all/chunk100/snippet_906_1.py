# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node:
    _l_(88980)


    def __init__(self, data=None):
        _l_(88979)

        _n_(88974, "self", lambda: self).data = _n_(88975, "data", lambda: data)
        _l_(88976)
        _n_(88977, "self", lambda: self).next = None
        _l_(88978)

class singly_linked_list:
    _l_(89054)


    def __init__(self):
        _l_(88987)

        _n_(88981, "self", lambda: self).tail = None
        _l_(88982)
        _n_(88983, "self", lambda: self).head = None
        _l_(88984)
        _n_(88985, "self", lambda: self).count = 0
        _l_(88986)

    def append_item(self, data):
        _l_(89006)

        if _a_(88989, _n_(88988, "self", lambda: self), "head"):
            _l_(89003)

            _a_(88991, _n_(88990, "self", lambda: self), "head").next = _n_(88992, "node", lambda: node)
            _l_(88993)
            _n_(88994, "self", lambda: self).head = _n_(88995, "node", lambda: node)
            _l_(88996)
        else:
            _n_(88997, "self", lambda: self).tail = _n_(88998, "node", lambda: node)
            _l_(88999)
            _n_(89000, "self", lambda: self).head = _n_(89001, "node", lambda: node)
            _l_(89002)
        _n_(89004, "self", lambda: self).count += 1
        _l_(89005)

    def delete_item(self, data):
        _l_(89039)

        current = _a_(89008, _n_(89007, "self", lambda: self), "tail")
        _l_(89009)
        prev = _a_(89011, _n_(89010, "self", lambda: self), "tail")
        _l_(89012)
        while _n_(89013, "current", lambda: current):
            _l_(89038)

            if _a_(89015, _n_(89014, "current", lambda: current), "data") == _n_(89016, "data", lambda: data):
                _l_(89032)

                if _n_(89017, "current", lambda: current) == _a_(89019, _n_(89018, "self", lambda: self), "tail"):
                    _l_(89028)

                    _n_(89020, "self", lambda: self).tail = _a_(89022, _n_(89021, "current", lambda: current), "next")
                    _l_(89023)
                else:
                    _n_(89024, "prev", lambda: prev).next = _a_(89026, _n_(89025, "current", lambda: current), "next")
                    _l_(89027)
                _n_(89029, "self", lambda: self).count -= 1
                _l_(89030)
                aux = ""
                _l_(89031)
                return aux
            prev = _n_(89033, "current", lambda: current)
            _l_(89034)
            current = _a_(89036, _n_(89035, "current", lambda: current), "next")
            _l_(89037)

    def iterate_item(self):
        _l_(89053)

        current_item = _a_(89041, _n_(89040, "self", lambda: self), "tail")
        _l_(89042)
        while _n_(89043, "current_item", lambda: current_item):
            _l_(89052)

            val = _a_(89045, _n_(89044, "current_item", lambda: current_item), "data")
            _l_(89046)
            current_item = _a_(89048, _n_(89047, "current_item", lambda: current_item), "next")
            _l_(89049)
            yield _n_(89050, "val", lambda: val)
            _l_(89051)
items = _c_(89056, _n_(89055, "singly_linked_list", lambda: singly_linked_list))
_l_(89057)
_c_(89060, _a_(89059, _n_(89058, "items", lambda: items), "append_item"), 'PHP')
_l_(89061)
_c_(89064, _a_(89063, _n_(89062, "items", lambda: items), "append_item"), 'Python')
_l_(89065)
_c_(89068, _a_(89067, _n_(89066, "items", lambda: items), "append_item"), 'C#')
_l_(89069)
_c_(89072, _a_(89071, _n_(89070, "items", lambda: items), "append_item"), 'C++')
_l_(89073)
_c_(89076, _a_(89075, _n_(89074, "items", lambda: items), "append_item"), 'Java')
_l_(89077)
_c_(89079, _n_(89078, "print", lambda: print), 'Original list:')
_l_(89080)
for val in _c_(89083, _a_(89082, _n_(89081, "items", lambda: items), "iterate_item")):
    _l_(89088)

    _c_(89086, _n_(89084, "print", lambda: print), _n_(89085, "val", lambda: val))
    _l_(89087)
_c_(89090, _n_(89089, "print", lambda: print), '\nAfter removing the last item from the list:')
_l_(89091)
_c_(89094, _a_(89093, _n_(89092, "items", lambda: items), "delete_item"), 'Java')
_l_(89095)
for val in _c_(89098, _a_(89097, _n_(89096, "items", lambda: items), "iterate_item")):
    _l_(89103)

    _c_(89101, _n_(89099, "print", lambda: print), _n_(89100, "val", lambda: val))
    _l_(89102)