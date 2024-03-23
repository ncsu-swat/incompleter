# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node:
    _l_(7214)


    def __init__(self, data=None):
        _l_(7213)

        _n_(7208, "self", lambda: self).data = _n_(7209, "data", lambda: data)
        _l_(7210)
        _n_(7211, "self", lambda: self).next = None
        _l_(7212)

class singly_linked_list:
    _l_(7289)


    def __init__(self):
        _l_(7221)

        _n_(7215, "self", lambda: self).tail = None
        _l_(7216)
        _n_(7217, "self", lambda: self).head = None
        _l_(7218)
        _n_(7219, "self", lambda: self).count = 0
        _l_(7220)

    def append_item(self, data):
        _l_(7241)

        node = _c_(7224, _n_(7222, "Node", lambda: Node), _n_(7223, "data", lambda: data))
        _l_(7225)
        if _a_(7227, _n_(7226, "self", lambda: self), "head"):
            _l_(7238)

            _a_(7229, _n_(7228, "self", lambda: self), "head").next = _n_(7230, "node", lambda: node)
            _l_(7231)
        else:
            _n_(7232, "self", lambda: self).tail = _n_(7233, "node", lambda: node)
            _l_(7234)
            _n_(7235, "self", lambda: self).head = _n_(7236, "node", lambda: node)
            _l_(7237)
        _n_(7239, "self", lambda: self).count += 1
        _l_(7240)

    def delete_item(self, data):
        _l_(7274)

        current = _a_(7243, _n_(7242, "self", lambda: self), "tail")
        _l_(7244)
        prev = _a_(7246, _n_(7245, "self", lambda: self), "tail")
        _l_(7247)
        while _n_(7248, "current", lambda: current):
            _l_(7273)

            if _a_(7250, _n_(7249, "current", lambda: current), "data") == _n_(7251, "data", lambda: data):
                _l_(7267)

                if _n_(7252, "current", lambda: current) == _a_(7254, _n_(7253, "self", lambda: self), "tail"):
                    _l_(7263)

                    _n_(7255, "self", lambda: self).tail = _a_(7257, _n_(7256, "current", lambda: current), "next")
                    _l_(7258)
                else:
                    _n_(7259, "prev", lambda: prev).next = _a_(7261, _n_(7260, "current", lambda: current), "next")
                    _l_(7262)
                _n_(7264, "self", lambda: self).count -= 1
                _l_(7265)
                aux = ""
                _l_(7266)
                return aux
            prev = _n_(7268, "current", lambda: current)
            _l_(7269)
            current = _a_(7271, _n_(7270, "current", lambda: current), "next")
            _l_(7272)

    def iterate_item(self):
        _l_(7288)

        current_item = _a_(7276, _n_(7275, "self", lambda: self), "tail")
        _l_(7277)
        while _n_(7278, "current_item", lambda: current_item):
            _l_(7287)

            val = _a_(7280, _n_(7279, "current_item", lambda: current_item), "data")
            _l_(7281)
            current_item = _a_(7283, _n_(7282, "current_item", lambda: current_item), "next")
            _l_(7284)
            yield _n_(7285, "val", lambda: val)
            _l_(7286)
items = _c_(7291, _n_(7290, "singly_linked_list", lambda: singly_linked_list))
_l_(7292)
_c_(7295, _a_(7294, _n_(7293, "items", lambda: items), "append_item"), 'PHP')
_l_(7296)
_c_(7299, _a_(7298, _n_(7297, "items", lambda: items), "append_item"), 'Python')
_l_(7300)
_c_(7303, _a_(7302, _n_(7301, "items", lambda: items), "append_item"), 'C#')
_l_(7304)
_c_(7307, _a_(7306, _n_(7305, "items", lambda: items), "append_item"), 'C++')
_l_(7308)
_c_(7311, _a_(7310, _n_(7309, "items", lambda: items), "append_item"), 'Java')
_l_(7312)
_c_(7314, _n_(7313, "print", lambda: print), 'Original list:')
_l_(7315)
for val in _c_(7318, _a_(7317, _n_(7316, "items", lambda: items), "iterate_item")):
    _l_(7323)

    _c_(7321, _n_(7319, "print", lambda: print), _n_(7320, "val", lambda: val))
    _l_(7322)
_c_(7325, _n_(7324, "print", lambda: print), '\nAfter removing the first item from the list:')
_l_(7326)
_c_(7329, _a_(7328, _n_(7327, "items", lambda: items), "delete_item"), 'PHP')
_l_(7330)
for val in _c_(7333, _a_(7332, _n_(7331, "items", lambda: items), "iterate_item")):
    _l_(7338)

    _c_(7336, _n_(7334, "print", lambda: print), _n_(7335, "val", lambda: val))
    _l_(7337)