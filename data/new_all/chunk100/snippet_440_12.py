# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node:
    _l_(44935)


    def __init__(self, data=None):
        _l_(44934)

        _n_(44929, "self", lambda: self).data = _n_(44930, "data", lambda: data)
        _l_(44931)
        _n_(44932, "self", lambda: self).next = None
        _l_(44933)

class singly_linked_list:
    _l_(45002)


    def __init__(self):
        _l_(44942)

        _n_(44936, "self", lambda: self).tail = None
        _l_(44937)
        _n_(44938, "self", lambda: self).head = None
        _l_(44939)
        _n_(44940, "self", lambda: self).count = 0
        _l_(44941)

    def append_item(self, data):
        _l_(44961)

        node = _c_(44945, _n_(44943, "Node", lambda: Node), _n_(44944, "data", lambda: data))
        _l_(44946)
        if _a_(44948, _n_(44947, "self", lambda: self), "head"):
            _l_(44958)

            _n_(44949, "self", lambda: self).head = _n_(44950, "node", lambda: node)
            _l_(44951)
        else:
            _n_(44952, "self", lambda: self).tail = _n_(44953, "node", lambda: node)
            _l_(44954)
            _n_(44955, "self", lambda: self).head = _n_(44956, "node", lambda: node)
            _l_(44957)
        _n_(44959, "self", lambda: self).count += 1
        _l_(44960)

    def __getitem__(self, index):
        _l_(44980)

        if _n_(44962, "index", lambda: index) > _a_(44964, _n_(44963, "self", lambda: self), "count") - 1:
            _l_(44966)

            aux = 'Index out of range'
            _l_(44965)
            return aux
        current_val = _a_(44968, _n_(44967, "self", lambda: self), "tail")
        _l_(44969)
        for n in _c_(44972, _n_(44970, "range", lambda: range), _n_(44971, "index", lambda: index)):
            _l_(44976)

            current_val = _a_(44974, _n_(44973, "current_val", lambda: current_val), "next")
            _l_(44975)
        aux = _a_(44978, _n_(44977, "current_val", lambda: current_val), "data")
        _l_(44979)
        return aux

    def __setitem__(self, index, value):
        _l_(45001)

        if _n_(44981, "index", lambda: index) > _a_(44983, _n_(44982, "self", lambda: self), "count") - 1:
            _l_(44987)

            raise _c_(44985, _n_(44984, "Exception", lambda: Exception), 'Index out of range.')
            _l_(44986)
        current = _a_(44989, _n_(44988, "self", lambda: self), "tail")
        _l_(44990)
        for n in _c_(44993, _n_(44991, "range", lambda: range), _n_(44992, "index", lambda: index)):
            _l_(44997)

            current = _a_(44995, _n_(44994, "current", lambda: current), "next")
            _l_(44996)
        _n_(44998, "current", lambda: current).data = _n_(44999, "value", lambda: value)
        _l_(45000)
items = _c_(45004, _n_(45003, "singly_linked_list", lambda: singly_linked_list))
_l_(45005)
_c_(45008, _a_(45007, _n_(45006, "items", lambda: items), "append_item"), 'PHP')
_l_(45009)
_c_(45012, _a_(45011, _n_(45010, "items", lambda: items), "append_item"), 'Python')
_l_(45013)
_c_(45016, _a_(45015, _n_(45014, "items", lambda: items), "append_item"), 'C#')
_l_(45017)
_c_(45020, _a_(45019, _n_(45018, "items", lambda: items), "append_item"), 'C++')
_l_(45021)
_c_(45024, _a_(45023, _n_(45022, "items", lambda: items), "append_item"), 'Java')
_l_(45025)
_c_(45027, _n_(45026, "print", lambda: print), 'Modify items by index:')
_l_(45028)
_n_(45029, "items", lambda: items)[1] = 'SQL'
_l_(45030)
_c_(45033, _n_(45031, "print", lambda: print), 'New value: ', _n_(45032, "items", lambda: items)[1])
_l_(45034)
_n_(45035, "items", lambda: items)[4] = 'Perl'
_l_(45036)
_c_(45039, _n_(45037, "print", lambda: print), 'New value: ', _n_(45038, "items", lambda: items)[4])
_l_(45040)