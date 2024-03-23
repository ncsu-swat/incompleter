# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node:
    _l_(7869)


    def __init__(self, data=None):
        _l_(7868)

        _n_(7865, "self", lambda: self).data = _n_(7866, "data", lambda: data)
        _l_(7867)

class singly_linked_list:
    _l_(7947)


    def __init__(self):
        _l_(7876)

        _n_(7870, "self", lambda: self).tail = None
        _l_(7871)
        _n_(7872, "self", lambda: self).head = None
        _l_(7873)
        _n_(7874, "self", lambda: self).count = 0
        _l_(7875)

    def append_item(self, data):
        _l_(7899)

        node = _c_(7879, _n_(7877, "Node", lambda: Node), _n_(7878, "data", lambda: data))
        _l_(7880)
        if _a_(7882, _n_(7881, "self", lambda: self), "head"):
            _l_(7896)

            _a_(7884, _n_(7883, "self", lambda: self), "head").next = _n_(7885, "node", lambda: node)
            _l_(7886)
            _n_(7887, "self", lambda: self).head = _n_(7888, "node", lambda: node)
            _l_(7889)
        else:
            _n_(7890, "self", lambda: self).tail = _n_(7891, "node", lambda: node)
            _l_(7892)
            _n_(7893, "self", lambda: self).head = _n_(7894, "node", lambda: node)
            _l_(7895)
        _n_(7897, "self", lambda: self).count += 1
        _l_(7898)

    def delete_item(self, data):
        _l_(7932)

        current = _a_(7901, _n_(7900, "self", lambda: self), "tail")
        _l_(7902)
        prev = _a_(7904, _n_(7903, "self", lambda: self), "tail")
        _l_(7905)
        while _n_(7906, "current", lambda: current):
            _l_(7931)

            if _a_(7908, _n_(7907, "current", lambda: current), "data") == _n_(7909, "data", lambda: data):
                _l_(7925)

                if _n_(7910, "current", lambda: current) == _a_(7912, _n_(7911, "self", lambda: self), "tail"):
                    _l_(7921)

                    _n_(7913, "self", lambda: self).tail = _a_(7915, _n_(7914, "current", lambda: current), "next")
                    _l_(7916)
                else:
                    _n_(7917, "prev", lambda: prev).next = _a_(7919, _n_(7918, "current", lambda: current), "next")
                    _l_(7920)
                _n_(7922, "self", lambda: self).count -= 1
                _l_(7923)
                aux = ""
                _l_(7924)
                return aux
            prev = _n_(7926, "current", lambda: current)
            _l_(7927)
            current = _a_(7929, _n_(7928, "current", lambda: current), "next")
            _l_(7930)

    def iterate_item(self):
        _l_(7946)

        current_item = _a_(7934, _n_(7933, "self", lambda: self), "tail")
        _l_(7935)
        while _n_(7936, "current_item", lambda: current_item):
            _l_(7945)

            val = _a_(7938, _n_(7937, "current_item", lambda: current_item), "data")
            _l_(7939)
            current_item = _a_(7941, _n_(7940, "current_item", lambda: current_item), "next")
            _l_(7942)
            yield _n_(7943, "val", lambda: val)
            _l_(7944)
items = _c_(7949, _n_(7948, "singly_linked_list", lambda: singly_linked_list))
_l_(7950)
_c_(7953, _a_(7952, _n_(7951, "items", lambda: items), "append_item"), 'PHP')
_l_(7954)
_c_(7957, _a_(7956, _n_(7955, "items", lambda: items), "append_item"), 'Python')
_l_(7958)
_c_(7961, _a_(7960, _n_(7959, "items", lambda: items), "append_item"), 'C#')
_l_(7962)
_c_(7965, _a_(7964, _n_(7963, "items", lambda: items), "append_item"), 'C++')
_l_(7966)
_c_(7969, _a_(7968, _n_(7967, "items", lambda: items), "append_item"), 'Java')
_l_(7970)
_c_(7972, _n_(7971, "print", lambda: print), 'Original list:')
_l_(7973)
for val in _c_(7976, _a_(7975, _n_(7974, "items", lambda: items), "iterate_item")):
    _l_(7981)

    _c_(7979, _n_(7977, "print", lambda: print), _n_(7978, "val", lambda: val))
    _l_(7980)
_c_(7983, _n_(7982, "print", lambda: print), '\nAfter removing the first item from the list:')
_l_(7984)
_c_(7987, _a_(7986, _n_(7985, "items", lambda: items), "delete_item"), 'PHP')
_l_(7988)
for val in _c_(7991, _a_(7990, _n_(7989, "items", lambda: items), "iterate_item")):
    _l_(7996)

    _c_(7994, _n_(7992, "print", lambda: print), _n_(7993, "val", lambda: val))
    _l_(7995)