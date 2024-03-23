# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node:
    _l_(45840)


    def __init__(self, data=None):
        _l_(45839)

        _n_(45834, "self", lambda: self).data = _n_(45835, "data", lambda: data)
        _l_(45836)
        _n_(45837, "self", lambda: self).next = None
        _l_(45838)

class singly_linked_list:
    _l_(45911)


    def __init__(self):
        _l_(45847)

        _n_(45841, "self", lambda: self).tail = None
        _l_(45842)
        _n_(45843, "self", lambda: self).head = None
        _l_(45844)
        _n_(45845, "self", lambda: self).count = 0
        _l_(45846)

    def append_item(self, data):
        _l_(45870)

        node = _c_(45850, _n_(45848, "Node", lambda: Node), _n_(45849, "data", lambda: data))
        _l_(45851)
        if _a_(45853, _n_(45852, "self", lambda: self), "head"):
            _l_(45867)

            _a_(45855, _n_(45854, "self", lambda: self), "head").next = _n_(45856, "node", lambda: node)
            _l_(45857)
            _n_(45858, "self", lambda: self).head = _n_(45859, "node", lambda: node)
            _l_(45860)
        else:
            _n_(45861, "self", lambda: self).tail = _n_(45862, "node", lambda: node)
            _l_(45863)
            _n_(45864, "self", lambda: self).head = _n_(45865, "node", lambda: node)
            _l_(45866)
        _n_(45868, "self", lambda: self).count += 1
        _l_(45869)

    def __getitem__(self, index):
        _l_(45889)

        if _n_(45871, "index", lambda: index) > _a_(45873, _n_(45872, "self", lambda: self), "count") - 1:
            _l_(45875)

            aux = 'Index out of range'
            _l_(45874)
            return aux
        current_val = _a_(45877, _n_(45876, "self", lambda: self), "tail")
        _l_(45878)
        for n in _c_(45881, _n_(45879, "range", lambda: range), _n_(45880, "index", lambda: index)):
            _l_(45885)

            current_val = _a_(45883, _n_(45882, "current_val", lambda: current_val), "next")
            _l_(45884)
        aux = _a_(45887, _n_(45886, "current_val", lambda: current_val), "data")
        _l_(45888)
        return aux

    def __setitem__(self, index, value):
        _l_(45910)

        if _n_(45890, "index", lambda: index) > _a_(45892, _n_(45891, "self", lambda: self), "count") - 1:
            _l_(45896)

            raise _c_(45894, _n_(45893, "Exception", lambda: Exception), 'Index out of range.')
            _l_(45895)
        current = _a_(45898, _n_(45897, "self", lambda: self), "tail")
        _l_(45899)
        for n in _c_(45902, _n_(45900, "range", lambda: range), _n_(45901, "index", lambda: index)):
            _l_(45906)

            current = _a_(45904, _n_(45903, "current", lambda: current), "next")
            _l_(45905)
        _n_(45907, "current", lambda: current).data = _n_(45908, "value", lambda: value)
        _l_(45909)
_c_(45914, _a_(45913, _n_(45912, "items", lambda: items), "append_item"), 'PHP')
_l_(45915)
_c_(45918, _a_(45917, _n_(45916, "items", lambda: items), "append_item"), 'Python')
_l_(45919)
_c_(45922, _a_(45921, _n_(45920, "items", lambda: items), "append_item"), 'C#')
_l_(45923)
_c_(45926, _a_(45925, _n_(45924, "items", lambda: items), "append_item"), 'C++')
_l_(45927)
_c_(45930, _a_(45929, _n_(45928, "items", lambda: items), "append_item"), 'Java')
_l_(45931)
_c_(45933, _n_(45932, "print", lambda: print), 'Modify items by index:')
_l_(45934)
_n_(45935, "items", lambda: items)[1] = 'SQL'
_l_(45936)
_c_(45939, _n_(45937, "print", lambda: print), 'New value: ', _n_(45938, "items", lambda: items)[1])
_l_(45940)
_n_(45941, "items", lambda: items)[4] = 'Perl'
_l_(45942)
_c_(45945, _n_(45943, "print", lambda: print), 'New value: ', _n_(45944, "items", lambda: items)[4])
_l_(45946)