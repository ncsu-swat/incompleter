# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node:
    _l_(7083)


    def __init__(self, data=None):
        _l_(7082)

        _n_(7077, "self", lambda: self).data = _n_(7078, "data", lambda: data)
        _l_(7079)
        _n_(7080, "self", lambda: self).next = None
        _l_(7081)

class singly_linked_list:
    _l_(7158)


    def __init__(self):
        _l_(7090)

        _n_(7084, "self", lambda: self).tail = None
        _l_(7085)
        _n_(7086, "self", lambda: self).head = None
        _l_(7087)
        _n_(7088, "self", lambda: self).count = 0
        _l_(7089)

    def append_item(self, data):
        _l_(7113)

        node = _c_(7093, _n_(7091, "Node", lambda: Node), _n_(7092, "data", lambda: data))
        _l_(7094)
        if _a_(7096, _n_(7095, "self", lambda: self), "head"):
            _l_(7110)

            _a_(7098, _n_(7097, "self", lambda: self), "head").next = _n_(7099, "node", lambda: node)
            _l_(7100)
            _n_(7101, "self", lambda: self).head = _n_(7102, "node", lambda: node)
            _l_(7103)
        else:
            _n_(7104, "self", lambda: self).tail = _n_(7105, "node", lambda: node)
            _l_(7106)
            _n_(7107, "self", lambda: self).head = _n_(7108, "node", lambda: node)
            _l_(7109)
        _n_(7111, "self", lambda: self).count += 1
        _l_(7112)

    def delete_item(self, data):
        _l_(7146)

        current = _a_(7115, _n_(7114, "self", lambda: self), "tail")
        _l_(7116)
        prev = _a_(7118, _n_(7117, "self", lambda: self), "tail")
        _l_(7119)
        while _n_(7120, "current", lambda: current):
            _l_(7145)

            if _a_(7122, _n_(7121, "current", lambda: current), "data") == _n_(7123, "data", lambda: data):
                _l_(7139)

                if _n_(7124, "current", lambda: current) == _a_(7126, _n_(7125, "self", lambda: self), "tail"):
                    _l_(7135)

                    _n_(7127, "self", lambda: self).tail = _a_(7129, _n_(7128, "current", lambda: current), "next")
                    _l_(7130)
                else:
                    _n_(7131, "prev", lambda: prev).next = _a_(7133, _n_(7132, "current", lambda: current), "next")
                    _l_(7134)
                _n_(7136, "self", lambda: self).count -= 1
                _l_(7137)
                aux = ""
                _l_(7138)
                return aux
            prev = _n_(7140, "current", lambda: current)
            _l_(7141)
            current = _a_(7143, _n_(7142, "current", lambda: current), "next")
            _l_(7144)

    def iterate_item(self):
        _l_(7157)

        while _n_(7147, "current_item", lambda: current_item):
            _l_(7156)

            val = _a_(7149, _n_(7148, "current_item", lambda: current_item), "data")
            _l_(7150)
            current_item = _a_(7152, _n_(7151, "current_item", lambda: current_item), "next")
            _l_(7153)
            yield _n_(7154, "val", lambda: val)
            _l_(7155)
items = _c_(7160, _n_(7159, "singly_linked_list", lambda: singly_linked_list))
_l_(7161)
_c_(7164, _a_(7163, _n_(7162, "items", lambda: items), "append_item"), 'PHP')
_l_(7165)
_c_(7168, _a_(7167, _n_(7166, "items", lambda: items), "append_item"), 'Python')
_l_(7169)
_c_(7172, _a_(7171, _n_(7170, "items", lambda: items), "append_item"), 'C#')
_l_(7173)
_c_(7176, _a_(7175, _n_(7174, "items", lambda: items), "append_item"), 'C++')
_l_(7177)
_c_(7180, _a_(7179, _n_(7178, "items", lambda: items), "append_item"), 'Java')
_l_(7181)
_c_(7183, _n_(7182, "print", lambda: print), 'Original list:')
_l_(7184)
for val in _c_(7187, _a_(7186, _n_(7185, "items", lambda: items), "iterate_item")):
    _l_(7192)

    _c_(7190, _n_(7188, "print", lambda: print), _n_(7189, "val", lambda: val))
    _l_(7191)
_c_(7194, _n_(7193, "print", lambda: print), '\nAfter removing the first item from the list:')
_l_(7195)
_c_(7198, _a_(7197, _n_(7196, "items", lambda: items), "delete_item"), 'PHP')
_l_(7199)
for val in _c_(7202, _a_(7201, _n_(7200, "items", lambda: items), "iterate_item")):
    _l_(7207)

    _c_(7205, _n_(7203, "print", lambda: print), _n_(7204, "val", lambda: val))
    _l_(7206)