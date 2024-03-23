# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node:
    _l_(7345)


    def __init__(self, data=None):
        _l_(7344)

        _n_(7339, "self", lambda: self).data = _n_(7340, "data", lambda: data)
        _l_(7341)
        _n_(7342, "self", lambda: self).next = None
        _l_(7343)

class singly_linked_list:
    _l_(7420)


    def __init__(self):
        _l_(7352)

        _n_(7346, "self", lambda: self).tail = None
        _l_(7347)
        _n_(7348, "self", lambda: self).head = None
        _l_(7349)
        _n_(7350, "self", lambda: self).count = 0
        _l_(7351)

    def append_item(self, data):
        _l_(7375)

        node = _c_(7355, _n_(7353, "Node", lambda: Node), _n_(7354, "data", lambda: data))
        _l_(7356)
        if _a_(7358, _n_(7357, "self", lambda: self), "head"):
            _l_(7372)

            _a_(7360, _n_(7359, "self", lambda: self), "head").next = _n_(7361, "node", lambda: node)
            _l_(7362)
            _n_(7363, "self", lambda: self).head = _n_(7364, "node", lambda: node)
            _l_(7365)
        else:
            _n_(7366, "self", lambda: self).tail = _n_(7367, "node", lambda: node)
            _l_(7368)
            _n_(7369, "self", lambda: self).head = _n_(7370, "node", lambda: node)
            _l_(7371)
        _n_(7373, "self", lambda: self).count += 1
        _l_(7374)

    def delete_item(self, data):
        _l_(7405)

        current = _a_(7377, _n_(7376, "self", lambda: self), "tail")
        _l_(7378)
        while _n_(7379, "current", lambda: current):
            _l_(7404)

            if _a_(7381, _n_(7380, "current", lambda: current), "data") == _n_(7382, "data", lambda: data):
                _l_(7398)

                if _n_(7383, "current", lambda: current) == _a_(7385, _n_(7384, "self", lambda: self), "tail"):
                    _l_(7394)

                    _n_(7386, "self", lambda: self).tail = _a_(7388, _n_(7387, "current", lambda: current), "next")
                    _l_(7389)
                else:
                    _n_(7390, "prev", lambda: prev).next = _a_(7392, _n_(7391, "current", lambda: current), "next")
                    _l_(7393)
                _n_(7395, "self", lambda: self).count -= 1
                _l_(7396)
                aux = ""
                _l_(7397)
                return aux
            prev = _n_(7399, "current", lambda: current)
            _l_(7400)
            current = _a_(7402, _n_(7401, "current", lambda: current), "next")
            _l_(7403)

    def iterate_item(self):
        _l_(7419)

        current_item = _a_(7407, _n_(7406, "self", lambda: self), "tail")
        _l_(7408)
        while _n_(7409, "current_item", lambda: current_item):
            _l_(7418)

            val = _a_(7411, _n_(7410, "current_item", lambda: current_item), "data")
            _l_(7412)
            current_item = _a_(7414, _n_(7413, "current_item", lambda: current_item), "next")
            _l_(7415)
            yield _n_(7416, "val", lambda: val)
            _l_(7417)
items = _c_(7422, _n_(7421, "singly_linked_list", lambda: singly_linked_list))
_l_(7423)
_c_(7426, _a_(7425, _n_(7424, "items", lambda: items), "append_item"), 'PHP')
_l_(7427)
_c_(7430, _a_(7429, _n_(7428, "items", lambda: items), "append_item"), 'Python')
_l_(7431)
_c_(7434, _a_(7433, _n_(7432, "items", lambda: items), "append_item"), 'C#')
_l_(7435)
_c_(7438, _a_(7437, _n_(7436, "items", lambda: items), "append_item"), 'C++')
_l_(7439)
_c_(7442, _a_(7441, _n_(7440, "items", lambda: items), "append_item"), 'Java')
_l_(7443)
_c_(7445, _n_(7444, "print", lambda: print), 'Original list:')
_l_(7446)
for val in _c_(7449, _a_(7448, _n_(7447, "items", lambda: items), "iterate_item")):
    _l_(7454)

    _c_(7452, _n_(7450, "print", lambda: print), _n_(7451, "val", lambda: val))
    _l_(7453)
_c_(7456, _n_(7455, "print", lambda: print), '\nAfter removing the first item from the list:')
_l_(7457)
_c_(7460, _a_(7459, _n_(7458, "items", lambda: items), "delete_item"), 'PHP')
_l_(7461)
for val in _c_(7464, _a_(7463, _n_(7462, "items", lambda: items), "iterate_item")):
    _l_(7469)

    _c_(7467, _n_(7465, "print", lambda: print), _n_(7466, "val", lambda: val))
    _l_(7468)