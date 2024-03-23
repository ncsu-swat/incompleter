# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node:
    _l_(6167)


    def __init__(self, data=None):
        _l_(6166)

        _n_(6161, "self", lambda: self).data = _n_(6162, "data", lambda: data)
        _l_(6163)
        _n_(6164, "self", lambda: self).next = None
        _l_(6165)

class singly_linked_list:
    _l_(6242)


    def __init__(self):
        _l_(6174)

        _n_(6168, "self", lambda: self).tail = None
        _l_(6169)
        _n_(6170, "self", lambda: self).head = None
        _l_(6171)
        _n_(6172, "self", lambda: self).count = 0
        _l_(6173)

    def append_item(self, data):
        _l_(6197)

        node = _c_(6177, _n_(6175, "Node", lambda: Node), _n_(6176, "data", lambda: data))
        _l_(6178)
        if _a_(6180, _n_(6179, "self", lambda: self), "head"):
            _l_(6194)

            _a_(6182, _n_(6181, "self", lambda: self), "head").next = _n_(6183, "node", lambda: node)
            _l_(6184)
            _n_(6185, "self", lambda: self).head = _n_(6186, "node", lambda: node)
            _l_(6187)
        else:
            _n_(6188, "self", lambda: self).tail = _n_(6189, "node", lambda: node)
            _l_(6190)
            _n_(6191, "self", lambda: self).head = _n_(6192, "node", lambda: node)
            _l_(6193)
        _n_(6195, "self", lambda: self).count += 1
        _l_(6196)

    def delete_item(self, data):
        _l_(6230)

        current = _a_(6199, _n_(6198, "self", lambda: self), "tail")
        _l_(6200)
        prev = _a_(6202, _n_(6201, "self", lambda: self), "tail")
        _l_(6203)
        while _n_(6204, "current", lambda: current):
            _l_(6229)

            if _a_(6206, _n_(6205, "current", lambda: current), "data") == _n_(6207, "data", lambda: data):
                _l_(6223)

                if _n_(6208, "current", lambda: current) == _a_(6210, _n_(6209, "self", lambda: self), "tail"):
                    _l_(6219)

                    _n_(6211, "self", lambda: self).tail = _a_(6213, _n_(6212, "current", lambda: current), "next")
                    _l_(6214)
                else:
                    _n_(6215, "prev", lambda: prev).next = _a_(6217, _n_(6216, "current", lambda: current), "next")
                    _l_(6218)
                _n_(6220, "self", lambda: self).count -= 1
                _l_(6221)
                aux = ""
                _l_(6222)
                return aux
            prev = _n_(6224, "current", lambda: current)
            _l_(6225)
            current = _a_(6227, _n_(6226, "current", lambda: current), "next")
            _l_(6228)

    def iterate_item(self):
        _l_(6241)

        current_item = _a_(6232, _n_(6231, "self", lambda: self), "tail")
        _l_(6233)
        while _n_(6234, "current_item", lambda: current_item):
            _l_(6240)

            val = _a_(6236, _n_(6235, "current_item", lambda: current_item), "data")
            _l_(6237)
            yield _n_(6238, "val", lambda: val)
            _l_(6239)
items = _c_(6244, _n_(6243, "singly_linked_list", lambda: singly_linked_list))
_l_(6245)
_c_(6248, _a_(6247, _n_(6246, "items", lambda: items), "append_item"), 'PHP')
_l_(6249)
_c_(6252, _a_(6251, _n_(6250, "items", lambda: items), "append_item"), 'Python')
_l_(6253)
_c_(6256, _a_(6255, _n_(6254, "items", lambda: items), "append_item"), 'C#')
_l_(6257)
_c_(6260, _a_(6259, _n_(6258, "items", lambda: items), "append_item"), 'C++')
_l_(6261)
_c_(6264, _a_(6263, _n_(6262, "items", lambda: items), "append_item"), 'Java')
_l_(6265)
_c_(6267, _n_(6266, "print", lambda: print), 'Original list:')
_l_(6268)
for val in _c_(6271, _a_(6270, _n_(6269, "items", lambda: items), "iterate_item")):
    _l_(6276)

    _c_(6274, _n_(6272, "print", lambda: print), _n_(6273, "val", lambda: val))
    _l_(6275)
_c_(6278, _n_(6277, "print", lambda: print), '\nAfter removing the first item from the list:')
_l_(6279)
_c_(6282, _a_(6281, _n_(6280, "items", lambda: items), "delete_item"), 'PHP')
_l_(6283)
for val in _c_(6286, _a_(6285, _n_(6284, "items", lambda: items), "iterate_item")):
    _l_(6291)

    _c_(6289, _n_(6287, "print", lambda: print), _n_(6288, "val", lambda: val))
    _l_(6290)