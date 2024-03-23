# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node:
    _l_(90948)


    def __init__(self, data=None):
        _l_(90947)

        _n_(90942, "self", lambda: self).data = _n_(90943, "data", lambda: data)
        _l_(90944)
        _n_(90945, "self", lambda: self).next = None
        _l_(90946)

class singly_linked_list:
    _l_(91023)


    def __init__(self):
        _l_(90955)

        _n_(90949, "self", lambda: self).tail = None
        _l_(90950)
        _n_(90951, "self", lambda: self).head = None
        _l_(90952)
        _n_(90953, "self", lambda: self).count = 0
        _l_(90954)

    def append_item(self, data):
        _l_(90978)

        node = _c_(90958, _n_(90956, "Node", lambda: Node), _n_(90957, "data", lambda: data))
        _l_(90959)
        if _a_(90961, _n_(90960, "self", lambda: self), "head"):
            _l_(90975)

            _a_(90963, _n_(90962, "self", lambda: self), "head").next = _n_(90964, "node", lambda: node)
            _l_(90965)
            _n_(90966, "self", lambda: self).head = _n_(90967, "node", lambda: node)
            _l_(90968)
        else:
            _n_(90969, "self", lambda: self).tail = _n_(90970, "node", lambda: node)
            _l_(90971)
            _n_(90972, "self", lambda: self).head = _n_(90973, "node", lambda: node)
            _l_(90974)
        _n_(90976, "self", lambda: self).count += 1
        _l_(90977)

    def delete_item(self, data):
        _l_(91011)

        current = _a_(90980, _n_(90979, "self", lambda: self), "tail")
        _l_(90981)
        prev = _a_(90983, _n_(90982, "self", lambda: self), "tail")
        _l_(90984)
        while _n_(90985, "current", lambda: current):
            _l_(91010)

            if _a_(90987, _n_(90986, "current", lambda: current), "data") == _n_(90988, "data", lambda: data):
                _l_(91004)

                if _n_(90989, "current", lambda: current) == _a_(90991, _n_(90990, "self", lambda: self), "tail"):
                    _l_(91000)

                    _n_(90992, "self", lambda: self).tail = _a_(90994, _n_(90993, "current", lambda: current), "next")
                    _l_(90995)
                else:
                    _n_(90996, "prev", lambda: prev).next = _a_(90998, _n_(90997, "current", lambda: current), "next")
                    _l_(90999)
                _n_(91001, "self", lambda: self).count -= 1
                _l_(91002)
                aux = ""
                _l_(91003)
                return aux
            prev = _n_(91005, "current", lambda: current)
            _l_(91006)
            current = _a_(91008, _n_(91007, "current", lambda: current), "next")
            _l_(91009)

    def iterate_item(self):
        _l_(91022)

        current_item = _a_(91013, _n_(91012, "self", lambda: self), "tail")
        _l_(91014)
        while _n_(91015, "current_item", lambda: current_item):
            _l_(91021)

            current_item = _a_(91017, _n_(91016, "current_item", lambda: current_item), "next")
            _l_(91018)
            yield _n_(91019, "val", lambda: val)
            _l_(91020)
items = _c_(91025, _n_(91024, "singly_linked_list", lambda: singly_linked_list))
_l_(91026)
_c_(91029, _a_(91028, _n_(91027, "items", lambda: items), "append_item"), 'PHP')
_l_(91030)
_c_(91033, _a_(91032, _n_(91031, "items", lambda: items), "append_item"), 'Python')
_l_(91034)
_c_(91037, _a_(91036, _n_(91035, "items", lambda: items), "append_item"), 'C#')
_l_(91038)
_c_(91041, _a_(91040, _n_(91039, "items", lambda: items), "append_item"), 'C++')
_l_(91042)
_c_(91045, _a_(91044, _n_(91043, "items", lambda: items), "append_item"), 'Java')
_l_(91046)
_c_(91048, _n_(91047, "print", lambda: print), 'Original list:')
_l_(91049)
for val in _c_(91052, _a_(91051, _n_(91050, "items", lambda: items), "iterate_item")):
    _l_(91057)

    _c_(91055, _n_(91053, "print", lambda: print), _n_(91054, "val", lambda: val))
    _l_(91056)
_c_(91059, _n_(91058, "print", lambda: print), '\nAfter removing the last item from the list:')
_l_(91060)
_c_(91063, _a_(91062, _n_(91061, "items", lambda: items), "delete_item"), 'Java')
_l_(91064)
for val in _c_(91067, _a_(91066, _n_(91065, "items", lambda: items), "iterate_item")):
    _l_(91072)

    _c_(91070, _n_(91068, "print", lambda: print), _n_(91069, "val", lambda: val))
    _l_(91071)