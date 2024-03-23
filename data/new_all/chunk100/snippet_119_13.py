# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node:
    _l_(6822)


    def __init__(self, data=None):
        _l_(6821)

        _n_(6816, "self", lambda: self).data = _n_(6817, "data", lambda: data)
        _l_(6818)
        _n_(6819, "self", lambda: self).next = None
        _l_(6820)

class singly_linked_list:
    _l_(6896)


    def __init__(self):
        _l_(6829)

        _n_(6823, "self", lambda: self).tail = None
        _l_(6824)
        _n_(6825, "self", lambda: self).head = None
        _l_(6826)
        _n_(6827, "self", lambda: self).count = 0
        _l_(6828)

    def append_item(self, data):
        _l_(6848)

        node = _c_(6832, _n_(6830, "Node", lambda: Node), _n_(6831, "data", lambda: data))
        _l_(6833)
        if _a_(6835, _n_(6834, "self", lambda: self), "head"):
            _l_(6845)

            _n_(6836, "self", lambda: self).head = _n_(6837, "node", lambda: node)
            _l_(6838)
        else:
            _n_(6839, "self", lambda: self).tail = _n_(6840, "node", lambda: node)
            _l_(6841)
            _n_(6842, "self", lambda: self).head = _n_(6843, "node", lambda: node)
            _l_(6844)
        _n_(6846, "self", lambda: self).count += 1
        _l_(6847)

    def delete_item(self, data):
        _l_(6881)

        current = _a_(6850, _n_(6849, "self", lambda: self), "tail")
        _l_(6851)
        prev = _a_(6853, _n_(6852, "self", lambda: self), "tail")
        _l_(6854)
        while _n_(6855, "current", lambda: current):
            _l_(6880)

            if _a_(6857, _n_(6856, "current", lambda: current), "data") == _n_(6858, "data", lambda: data):
                _l_(6874)

                if _n_(6859, "current", lambda: current) == _a_(6861, _n_(6860, "self", lambda: self), "tail"):
                    _l_(6870)

                    _n_(6862, "self", lambda: self).tail = _a_(6864, _n_(6863, "current", lambda: current), "next")
                    _l_(6865)
                else:
                    _n_(6866, "prev", lambda: prev).next = _a_(6868, _n_(6867, "current", lambda: current), "next")
                    _l_(6869)
                _n_(6871, "self", lambda: self).count -= 1
                _l_(6872)
                aux = ""
                _l_(6873)
                return aux
            prev = _n_(6875, "current", lambda: current)
            _l_(6876)
            current = _a_(6878, _n_(6877, "current", lambda: current), "next")
            _l_(6879)

    def iterate_item(self):
        _l_(6895)

        current_item = _a_(6883, _n_(6882, "self", lambda: self), "tail")
        _l_(6884)
        while _n_(6885, "current_item", lambda: current_item):
            _l_(6894)

            val = _a_(6887, _n_(6886, "current_item", lambda: current_item), "data")
            _l_(6888)
            current_item = _a_(6890, _n_(6889, "current_item", lambda: current_item), "next")
            _l_(6891)
            yield _n_(6892, "val", lambda: val)
            _l_(6893)
items = _c_(6898, _n_(6897, "singly_linked_list", lambda: singly_linked_list))
_l_(6899)
_c_(6902, _a_(6901, _n_(6900, "items", lambda: items), "append_item"), 'PHP')
_l_(6903)
_c_(6906, _a_(6905, _n_(6904, "items", lambda: items), "append_item"), 'Python')
_l_(6907)
_c_(6910, _a_(6909, _n_(6908, "items", lambda: items), "append_item"), 'C#')
_l_(6911)
_c_(6914, _a_(6913, _n_(6912, "items", lambda: items), "append_item"), 'C++')
_l_(6915)
_c_(6918, _a_(6917, _n_(6916, "items", lambda: items), "append_item"), 'Java')
_l_(6919)
_c_(6921, _n_(6920, "print", lambda: print), 'Original list:')
_l_(6922)
for val in _c_(6925, _a_(6924, _n_(6923, "items", lambda: items), "iterate_item")):
    _l_(6930)

    _c_(6928, _n_(6926, "print", lambda: print), _n_(6927, "val", lambda: val))
    _l_(6929)
_c_(6932, _n_(6931, "print", lambda: print), '\nAfter removing the first item from the list:')
_l_(6933)
_c_(6936, _a_(6935, _n_(6934, "items", lambda: items), "delete_item"), 'PHP')
_l_(6937)
for val in _c_(6940, _a_(6939, _n_(6938, "items", lambda: items), "iterate_item")):
    _l_(6945)

    _c_(6943, _n_(6941, "print", lambda: print), _n_(6942, "val", lambda: val))
    _l_(6944)