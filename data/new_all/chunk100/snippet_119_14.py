# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node:
    _l_(6949)


    def __init__(self, data=None):
        _l_(6948)

        _n_(6946, "self", lambda: self).next = None
        _l_(6947)

class singly_linked_list:
    _l_(7027)


    def __init__(self):
        _l_(6956)

        _n_(6950, "self", lambda: self).tail = None
        _l_(6951)
        _n_(6952, "self", lambda: self).head = None
        _l_(6953)
        _n_(6954, "self", lambda: self).count = 0
        _l_(6955)

    def append_item(self, data):
        _l_(6979)

        node = _c_(6959, _n_(6957, "Node", lambda: Node), _n_(6958, "data", lambda: data))
        _l_(6960)
        if _a_(6962, _n_(6961, "self", lambda: self), "head"):
            _l_(6976)

            _a_(6964, _n_(6963, "self", lambda: self), "head").next = _n_(6965, "node", lambda: node)
            _l_(6966)
            _n_(6967, "self", lambda: self).head = _n_(6968, "node", lambda: node)
            _l_(6969)
        else:
            _n_(6970, "self", lambda: self).tail = _n_(6971, "node", lambda: node)
            _l_(6972)
            _n_(6973, "self", lambda: self).head = _n_(6974, "node", lambda: node)
            _l_(6975)
        _n_(6977, "self", lambda: self).count += 1
        _l_(6978)

    def delete_item(self, data):
        _l_(7012)

        current = _a_(6981, _n_(6980, "self", lambda: self), "tail")
        _l_(6982)
        prev = _a_(6984, _n_(6983, "self", lambda: self), "tail")
        _l_(6985)
        while _n_(6986, "current", lambda: current):
            _l_(7011)

            if _a_(6988, _n_(6987, "current", lambda: current), "data") == _n_(6989, "data", lambda: data):
                _l_(7005)

                if _n_(6990, "current", lambda: current) == _a_(6992, _n_(6991, "self", lambda: self), "tail"):
                    _l_(7001)

                    _n_(6993, "self", lambda: self).tail = _a_(6995, _n_(6994, "current", lambda: current), "next")
                    _l_(6996)
                else:
                    _n_(6997, "prev", lambda: prev).next = _a_(6999, _n_(6998, "current", lambda: current), "next")
                    _l_(7000)
                _n_(7002, "self", lambda: self).count -= 1
                _l_(7003)
                aux = ""
                _l_(7004)
                return aux
            prev = _n_(7006, "current", lambda: current)
            _l_(7007)
            current = _a_(7009, _n_(7008, "current", lambda: current), "next")
            _l_(7010)

    def iterate_item(self):
        _l_(7026)

        current_item = _a_(7014, _n_(7013, "self", lambda: self), "tail")
        _l_(7015)
        while _n_(7016, "current_item", lambda: current_item):
            _l_(7025)

            val = _a_(7018, _n_(7017, "current_item", lambda: current_item), "data")
            _l_(7019)
            current_item = _a_(7021, _n_(7020, "current_item", lambda: current_item), "next")
            _l_(7022)
            yield _n_(7023, "val", lambda: val)
            _l_(7024)
items = _c_(7029, _n_(7028, "singly_linked_list", lambda: singly_linked_list))
_l_(7030)
_c_(7033, _a_(7032, _n_(7031, "items", lambda: items), "append_item"), 'PHP')
_l_(7034)
_c_(7037, _a_(7036, _n_(7035, "items", lambda: items), "append_item"), 'Python')
_l_(7038)
_c_(7041, _a_(7040, _n_(7039, "items", lambda: items), "append_item"), 'C#')
_l_(7042)
_c_(7045, _a_(7044, _n_(7043, "items", lambda: items), "append_item"), 'C++')
_l_(7046)
_c_(7049, _a_(7048, _n_(7047, "items", lambda: items), "append_item"), 'Java')
_l_(7050)
_c_(7052, _n_(7051, "print", lambda: print), 'Original list:')
_l_(7053)
for val in _c_(7056, _a_(7055, _n_(7054, "items", lambda: items), "iterate_item")):
    _l_(7061)

    _c_(7059, _n_(7057, "print", lambda: print), _n_(7058, "val", lambda: val))
    _l_(7060)
_c_(7063, _n_(7062, "print", lambda: print), '\nAfter removing the first item from the list:')
_l_(7064)
_c_(7067, _a_(7066, _n_(7065, "items", lambda: items), "delete_item"), 'PHP')
_l_(7068)
for val in _c_(7071, _a_(7070, _n_(7069, "items", lambda: items), "iterate_item")):
    _l_(7076)

    _c_(7074, _n_(7072, "print", lambda: print), _n_(7073, "val", lambda: val))
    _l_(7075)