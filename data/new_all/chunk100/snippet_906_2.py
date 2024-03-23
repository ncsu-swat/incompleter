# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node:
    _l_(90027)


    def __init__(self, data=None):
        _l_(90026)

        _n_(90021, "self", lambda: self).data = _n_(90022, "data", lambda: data)
        _l_(90023)
        _n_(90024, "self", lambda: self).next = None
        _l_(90025)

class singly_linked_list:
    _l_(90102)


    def __init__(self):
        _l_(90034)

        _n_(90028, "self", lambda: self).tail = None
        _l_(90029)
        _n_(90030, "self", lambda: self).head = None
        _l_(90031)
        _n_(90032, "self", lambda: self).count = 0
        _l_(90033)

    def append_item(self, data):
        _l_(90054)

        node = _c_(90037, _n_(90035, "Node", lambda: Node), _n_(90036, "data", lambda: data))
        _l_(90038)
        if _a_(90040, _n_(90039, "self", lambda: self), "head"):
            _l_(90051)

            _a_(90042, _n_(90041, "self", lambda: self), "head").next = _n_(90043, "node", lambda: node)
            _l_(90044)
        else:
            _n_(90045, "self", lambda: self).tail = _n_(90046, "node", lambda: node)
            _l_(90047)
            _n_(90048, "self", lambda: self).head = _n_(90049, "node", lambda: node)
            _l_(90050)
        _n_(90052, "self", lambda: self).count += 1
        _l_(90053)

    def delete_item(self, data):
        _l_(90087)

        current = _a_(90056, _n_(90055, "self", lambda: self), "tail")
        _l_(90057)
        prev = _a_(90059, _n_(90058, "self", lambda: self), "tail")
        _l_(90060)
        while _n_(90061, "current", lambda: current):
            _l_(90086)

            if _a_(90063, _n_(90062, "current", lambda: current), "data") == _n_(90064, "data", lambda: data):
                _l_(90080)

                if _n_(90065, "current", lambda: current) == _a_(90067, _n_(90066, "self", lambda: self), "tail"):
                    _l_(90076)

                    _n_(90068, "self", lambda: self).tail = _a_(90070, _n_(90069, "current", lambda: current), "next")
                    _l_(90071)
                else:
                    _n_(90072, "prev", lambda: prev).next = _a_(90074, _n_(90073, "current", lambda: current), "next")
                    _l_(90075)
                _n_(90077, "self", lambda: self).count -= 1
                _l_(90078)
                aux = ""
                _l_(90079)
                return aux
            prev = _n_(90081, "current", lambda: current)
            _l_(90082)
            current = _a_(90084, _n_(90083, "current", lambda: current), "next")
            _l_(90085)

    def iterate_item(self):
        _l_(90101)

        current_item = _a_(90089, _n_(90088, "self", lambda: self), "tail")
        _l_(90090)
        while _n_(90091, "current_item", lambda: current_item):
            _l_(90100)

            val = _a_(90093, _n_(90092, "current_item", lambda: current_item), "data")
            _l_(90094)
            current_item = _a_(90096, _n_(90095, "current_item", lambda: current_item), "next")
            _l_(90097)
            yield _n_(90098, "val", lambda: val)
            _l_(90099)
items = _c_(90104, _n_(90103, "singly_linked_list", lambda: singly_linked_list))
_l_(90105)
_c_(90108, _a_(90107, _n_(90106, "items", lambda: items), "append_item"), 'PHP')
_l_(90109)
_c_(90112, _a_(90111, _n_(90110, "items", lambda: items), "append_item"), 'Python')
_l_(90113)
_c_(90116, _a_(90115, _n_(90114, "items", lambda: items), "append_item"), 'C#')
_l_(90117)
_c_(90120, _a_(90119, _n_(90118, "items", lambda: items), "append_item"), 'C++')
_l_(90121)
_c_(90124, _a_(90123, _n_(90122, "items", lambda: items), "append_item"), 'Java')
_l_(90125)
_c_(90127, _n_(90126, "print", lambda: print), 'Original list:')
_l_(90128)
for val in _c_(90131, _a_(90130, _n_(90129, "items", lambda: items), "iterate_item")):
    _l_(90136)

    _c_(90134, _n_(90132, "print", lambda: print), _n_(90133, "val", lambda: val))
    _l_(90135)
_c_(90138, _n_(90137, "print", lambda: print), '\nAfter removing the last item from the list:')
_l_(90139)
_c_(90142, _a_(90141, _n_(90140, "items", lambda: items), "delete_item"), 'Java')
_l_(90143)
for val in _c_(90146, _a_(90145, _n_(90144, "items", lambda: items), "iterate_item")):
    _l_(90151)

    _c_(90149, _n_(90147, "print", lambda: print), _n_(90148, "val", lambda: val))
    _l_(90150)