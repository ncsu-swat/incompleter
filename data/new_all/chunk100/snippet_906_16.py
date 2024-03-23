# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node:
    _l_(89896)


    def __init__(self, data=None):
        _l_(89895)

        _n_(89890, "self", lambda: self).data = _n_(89891, "data", lambda: data)
        _l_(89892)
        _n_(89893, "self", lambda: self).next = None
        _l_(89894)

class singly_linked_list:
    _l_(89971)


    def __init__(self):
        _l_(89903)

        _n_(89897, "self", lambda: self).tail = None
        _l_(89898)
        _n_(89899, "self", lambda: self).head = None
        _l_(89900)
        _n_(89901, "self", lambda: self).count = 0
        _l_(89902)

    def append_item(self, data):
        _l_(89926)

        node = _c_(89906, _n_(89904, "Node", lambda: Node), _n_(89905, "data", lambda: data))
        _l_(89907)
        if _a_(89909, _n_(89908, "self", lambda: self), "head"):
            _l_(89923)

            _a_(89911, _n_(89910, "self", lambda: self), "head").next = _n_(89912, "node", lambda: node)
            _l_(89913)
            _n_(89914, "self", lambda: self).head = _n_(89915, "node", lambda: node)
            _l_(89916)
        else:
            _n_(89917, "self", lambda: self).tail = _n_(89918, "node", lambda: node)
            _l_(89919)
            _n_(89920, "self", lambda: self).head = _n_(89921, "node", lambda: node)
            _l_(89922)
        _n_(89924, "self", lambda: self).count += 1
        _l_(89925)

    def delete_item(self, data):
        _l_(89959)

        current = _a_(89928, _n_(89927, "self", lambda: self), "tail")
        _l_(89929)
        prev = _a_(89931, _n_(89930, "self", lambda: self), "tail")
        _l_(89932)
        while _n_(89933, "current", lambda: current):
            _l_(89958)

            if _a_(89935, _n_(89934, "current", lambda: current), "data") == _n_(89936, "data", lambda: data):
                _l_(89952)

                if _n_(89937, "current", lambda: current) == _a_(89939, _n_(89938, "self", lambda: self), "tail"):
                    _l_(89948)

                    _n_(89940, "self", lambda: self).tail = _a_(89942, _n_(89941, "current", lambda: current), "next")
                    _l_(89943)
                else:
                    _n_(89944, "prev", lambda: prev).next = _a_(89946, _n_(89945, "current", lambda: current), "next")
                    _l_(89947)
                _n_(89949, "self", lambda: self).count -= 1
                _l_(89950)
                aux = ""
                _l_(89951)
                return aux
            prev = _n_(89953, "current", lambda: current)
            _l_(89954)
            current = _a_(89956, _n_(89955, "current", lambda: current), "next")
            _l_(89957)

    def iterate_item(self):
        _l_(89970)

        while _n_(89960, "current_item", lambda: current_item):
            _l_(89969)

            val = _a_(89962, _n_(89961, "current_item", lambda: current_item), "data")
            _l_(89963)
            current_item = _a_(89965, _n_(89964, "current_item", lambda: current_item), "next")
            _l_(89966)
            yield _n_(89967, "val", lambda: val)
            _l_(89968)
items = _c_(89973, _n_(89972, "singly_linked_list", lambda: singly_linked_list))
_l_(89974)
_c_(89977, _a_(89976, _n_(89975, "items", lambda: items), "append_item"), 'PHP')
_l_(89978)
_c_(89981, _a_(89980, _n_(89979, "items", lambda: items), "append_item"), 'Python')
_l_(89982)
_c_(89985, _a_(89984, _n_(89983, "items", lambda: items), "append_item"), 'C#')
_l_(89986)
_c_(89989, _a_(89988, _n_(89987, "items", lambda: items), "append_item"), 'C++')
_l_(89990)
_c_(89993, _a_(89992, _n_(89991, "items", lambda: items), "append_item"), 'Java')
_l_(89994)
_c_(89996, _n_(89995, "print", lambda: print), 'Original list:')
_l_(89997)
for val in _c_(90000, _a_(89999, _n_(89998, "items", lambda: items), "iterate_item")):
    _l_(90005)

    _c_(90003, _n_(90001, "print", lambda: print), _n_(90002, "val", lambda: val))
    _l_(90004)
_c_(90007, _n_(90006, "print", lambda: print), '\nAfter removing the last item from the list:')
_l_(90008)
_c_(90011, _a_(90010, _n_(90009, "items", lambda: items), "delete_item"), 'Java')
_l_(90012)
for val in _c_(90015, _a_(90014, _n_(90013, "items", lambda: items), "iterate_item")):
    _l_(90020)

    _c_(90018, _n_(90016, "print", lambda: print), _n_(90017, "val", lambda: val))
    _l_(90019)