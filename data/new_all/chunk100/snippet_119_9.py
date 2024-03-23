# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node:
    _l_(8003)


    def __init__(self, data=None):
        _l_(8002)

        _n_(7997, "self", lambda: self).data = _n_(7998, "data", lambda: data)
        _l_(7999)
        _n_(8000, "self", lambda: self).next = None
        _l_(8001)

class singly_linked_list:
    _l_(8078)


    def __init__(self):
        _l_(8010)

        _n_(8004, "self", lambda: self).tail = None
        _l_(8005)
        _n_(8006, "self", lambda: self).head = None
        _l_(8007)
        _n_(8008, "self", lambda: self).count = 0
        _l_(8009)

    def append_item(self, data):
        _l_(8033)

        node = _c_(8013, _n_(8011, "Node", lambda: Node), _n_(8012, "data", lambda: data))
        _l_(8014)
        if _a_(8016, _n_(8015, "self", lambda: self), "head"):
            _l_(8030)

            _a_(8018, _n_(8017, "self", lambda: self), "head").next = _n_(8019, "node", lambda: node)
            _l_(8020)
            _n_(8021, "self", lambda: self).head = _n_(8022, "node", lambda: node)
            _l_(8023)
        else:
            _n_(8024, "self", lambda: self).tail = _n_(8025, "node", lambda: node)
            _l_(8026)
            _n_(8027, "self", lambda: self).head = _n_(8028, "node", lambda: node)
            _l_(8029)
        _n_(8031, "self", lambda: self).count += 1
        _l_(8032)

    def delete_item(self, data):
        _l_(8066)

        current = _a_(8035, _n_(8034, "self", lambda: self), "tail")
        _l_(8036)
        prev = _a_(8038, _n_(8037, "self", lambda: self), "tail")
        _l_(8039)
        while _n_(8040, "current", lambda: current):
            _l_(8065)

            if _a_(8042, _n_(8041, "current", lambda: current), "data") == _n_(8043, "data", lambda: data):
                _l_(8059)

                if _n_(8044, "current", lambda: current) == _a_(8046, _n_(8045, "self", lambda: self), "tail"):
                    _l_(8055)

                    _n_(8047, "self", lambda: self).tail = _a_(8049, _n_(8048, "current", lambda: current), "next")
                    _l_(8050)
                else:
                    _n_(8051, "prev", lambda: prev).next = _a_(8053, _n_(8052, "current", lambda: current), "next")
                    _l_(8054)
                _n_(8056, "self", lambda: self).count -= 1
                _l_(8057)
                aux = ""
                _l_(8058)
                return aux
            prev = _n_(8060, "current", lambda: current)
            _l_(8061)
            current = _a_(8063, _n_(8062, "current", lambda: current), "next")
            _l_(8064)

    def iterate_item(self):
        _l_(8077)

        current_item = _a_(8068, _n_(8067, "self", lambda: self), "tail")
        _l_(8069)
        while _n_(8070, "current_item", lambda: current_item):
            _l_(8076)

            current_item = _a_(8072, _n_(8071, "current_item", lambda: current_item), "next")
            _l_(8073)
            yield _n_(8074, "val", lambda: val)
            _l_(8075)
items = _c_(8080, _n_(8079, "singly_linked_list", lambda: singly_linked_list))
_l_(8081)
_c_(8084, _a_(8083, _n_(8082, "items", lambda: items), "append_item"), 'PHP')
_l_(8085)
_c_(8088, _a_(8087, _n_(8086, "items", lambda: items), "append_item"), 'Python')
_l_(8089)
_c_(8092, _a_(8091, _n_(8090, "items", lambda: items), "append_item"), 'C#')
_l_(8093)
_c_(8096, _a_(8095, _n_(8094, "items", lambda: items), "append_item"), 'C++')
_l_(8097)
_c_(8100, _a_(8099, _n_(8098, "items", lambda: items), "append_item"), 'Java')
_l_(8101)
_c_(8103, _n_(8102, "print", lambda: print), 'Original list:')
_l_(8104)
for val in _c_(8107, _a_(8106, _n_(8105, "items", lambda: items), "iterate_item")):
    _l_(8112)

    _c_(8110, _n_(8108, "print", lambda: print), _n_(8109, "val", lambda: val))
    _l_(8111)
_c_(8114, _n_(8113, "print", lambda: print), '\nAfter removing the first item from the list:')
_l_(8115)
_c_(8118, _a_(8117, _n_(8116, "items", lambda: items), "delete_item"), 'PHP')
_l_(8119)
for val in _c_(8122, _a_(8121, _n_(8120, "items", lambda: items), "iterate_item")):
    _l_(8127)

    _c_(8125, _n_(8123, "print", lambda: print), _n_(8124, "val", lambda: val))
    _l_(8126)