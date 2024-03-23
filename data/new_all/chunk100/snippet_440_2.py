# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node:
    _l_(45160)


    def __init__(self, data=None):
        _l_(45159)

        _n_(45154, "self", lambda: self).data = _n_(45155, "data", lambda: data)
        _l_(45156)
        _n_(45157, "self", lambda: self).next = None
        _l_(45158)

class singly_linked_list:
    _l_(45227)


    def __init__(self):
        _l_(45167)

        _n_(45161, "self", lambda: self).tail = None
        _l_(45162)
        _n_(45163, "self", lambda: self).head = None
        _l_(45164)
        _n_(45165, "self", lambda: self).count = 0
        _l_(45166)

    def append_item(self, data):
        _l_(45186)

        if _a_(45169, _n_(45168, "self", lambda: self), "head"):
            _l_(45183)

            _a_(45171, _n_(45170, "self", lambda: self), "head").next = _n_(45172, "node", lambda: node)
            _l_(45173)
            _n_(45174, "self", lambda: self).head = _n_(45175, "node", lambda: node)
            _l_(45176)
        else:
            _n_(45177, "self", lambda: self).tail = _n_(45178, "node", lambda: node)
            _l_(45179)
            _n_(45180, "self", lambda: self).head = _n_(45181, "node", lambda: node)
            _l_(45182)
        _n_(45184, "self", lambda: self).count += 1
        _l_(45185)

    def __getitem__(self, index):
        _l_(45205)

        if _n_(45187, "index", lambda: index) > _a_(45189, _n_(45188, "self", lambda: self), "count") - 1:
            _l_(45191)

            aux = 'Index out of range'
            _l_(45190)
            return aux
        current_val = _a_(45193, _n_(45192, "self", lambda: self), "tail")
        _l_(45194)
        for n in _c_(45197, _n_(45195, "range", lambda: range), _n_(45196, "index", lambda: index)):
            _l_(45201)

            current_val = _a_(45199, _n_(45198, "current_val", lambda: current_val), "next")
            _l_(45200)
        aux = _a_(45203, _n_(45202, "current_val", lambda: current_val), "data")
        _l_(45204)
        return aux

    def __setitem__(self, index, value):
        _l_(45226)

        if _n_(45206, "index", lambda: index) > _a_(45208, _n_(45207, "self", lambda: self), "count") - 1:
            _l_(45212)

            raise _c_(45210, _n_(45209, "Exception", lambda: Exception), 'Index out of range.')
            _l_(45211)
        current = _a_(45214, _n_(45213, "self", lambda: self), "tail")
        _l_(45215)
        for n in _c_(45218, _n_(45216, "range", lambda: range), _n_(45217, "index", lambda: index)):
            _l_(45222)

            current = _a_(45220, _n_(45219, "current", lambda: current), "next")
            _l_(45221)
        _n_(45223, "current", lambda: current).data = _n_(45224, "value", lambda: value)
        _l_(45225)
items = _c_(45229, _n_(45228, "singly_linked_list", lambda: singly_linked_list))
_l_(45230)
_c_(45233, _a_(45232, _n_(45231, "items", lambda: items), "append_item"), 'PHP')
_l_(45234)
_c_(45237, _a_(45236, _n_(45235, "items", lambda: items), "append_item"), 'Python')
_l_(45238)
_c_(45241, _a_(45240, _n_(45239, "items", lambda: items), "append_item"), 'C#')
_l_(45242)
_c_(45245, _a_(45244, _n_(45243, "items", lambda: items), "append_item"), 'C++')
_l_(45246)
_c_(45249, _a_(45248, _n_(45247, "items", lambda: items), "append_item"), 'Java')
_l_(45250)
_c_(45252, _n_(45251, "print", lambda: print), 'Modify items by index:')
_l_(45253)
_n_(45254, "items", lambda: items)[1] = 'SQL'
_l_(45255)
_c_(45258, _n_(45256, "print", lambda: print), 'New value: ', _n_(45257, "items", lambda: items)[1])
_l_(45259)
_n_(45260, "items", lambda: items)[4] = 'Perl'
_l_(45261)
_c_(45264, _n_(45262, "print", lambda: print), 'New value: ', _n_(45263, "items", lambda: items)[4])
_l_(45265)