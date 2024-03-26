# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Node:
    _l_(116394)


    def __init__(self, data=None):
        _l_(116393)

        _n_(116388, "self", lambda: self).data = _n_(116389, "data", lambda: data)
        _l_(116390)
        _n_(116391, "self", lambda: self).next = None
        _l_(116392)

class singly_linked_list:
    _l_(116465)


    def __init__(self):
        _l_(116401)

        _n_(116395, "self", lambda: self).tail = None
        _l_(116396)
        _n_(116397, "self", lambda: self).head = None
        _l_(116398)
        _n_(116399, "self", lambda: self).count = 0
        _l_(116400)

    def append_item(self, data):
        _l_(116424)

        node = _c_(116404, _n_(116402, "Node", lambda: Node), _n_(116403, "data", lambda: data))
        _l_(116405)
        if _a_(116407, _n_(116406, "self", lambda: self), "head"):
            _l_(116421)

            _a_(116409, _n_(116408, "self", lambda: self), "head").next = _n_(116410, "node", lambda: node)
            _l_(116411)
            _n_(116412, "self", lambda: self).head = _n_(116413, "node", lambda: node)
            _l_(116414)
        else:
            _n_(116415, "self", lambda: self).tail = _n_(116416, "node", lambda: node)
            _l_(116417)
            _n_(116418, "self", lambda: self).head = _n_(116419, "node", lambda: node)
            _l_(116420)
        _n_(116422, "self", lambda: self).count += 1
        _l_(116423)

    def __getitem__(self, index):
        _l_(116443)

        if _n_(116425, "index", lambda: index) > _a_(116427, _n_(116426, "self", lambda: self), "count") - 1:
            _l_(116429)

            aux = 'Index out of range'
            _l_(116428)
            return aux
        current_val = _a_(116431, _n_(116430, "self", lambda: self), "tail")
        _l_(116432)
        for n in _c_(116435, _n_(116433, "range", lambda: range), _n_(116434, "index", lambda: index)):
            _l_(116439)

            current_val = _a_(116437, _n_(116436, "current_val", lambda: current_val), "next")
            _l_(116438)
        aux = _a_(116441, _n_(116440, "current_val", lambda: current_val), "data")
        _l_(116442)
        return aux

    def __setitem__(self, index, value):
        _l_(116464)

        if _n_(116444, "index", lambda: index) > _a_(116446, _n_(116445, "self", lambda: self), "count") - 1:
            _l_(116450)

            raise _c_(116448, _n_(116447, "Exception", lambda: Exception), 'Index out of range.')
            _l_(116449)
        current = _a_(116452, _n_(116451, "self", lambda: self), "tail")
        _l_(116453)
        for n in _c_(116456, _n_(116454, "range", lambda: range), _n_(116455, "index", lambda: index)):
            _l_(116460)

            current = _a_(116458, _n_(116457, "current", lambda: current), "next")
            _l_(116459)
        _n_(116461, "current", lambda: current).data = _n_(116462, "value", lambda: value)
        _l_(116463)
_c_(116468, _a_(116467, _n_(116466, "items", lambda: items), "append_item"), 'PHP')
_l_(116469)
_c_(116472, _a_(116471, _n_(116470, "items", lambda: items), "append_item"), 'Python')
_l_(116473)
_c_(116476, _a_(116475, _n_(116474, "items", lambda: items), "append_item"), 'C#')
_l_(116477)
_c_(116480, _a_(116479, _n_(116478, "items", lambda: items), "append_item"), 'C++')
_l_(116481)
_c_(116484, _a_(116483, _n_(116482, "items", lambda: items), "append_item"), 'Java')
_l_(116485)
_c_(116487, _n_(116486, "print", lambda: print), 'Modify items by index:')
_l_(116488)
_n_(116489, "items", lambda: items)[1] = 'SQL'
_l_(116490)
_c_(116493, _n_(116491, "print", lambda: print), 'New value: ', _n_(116492, "items", lambda: items)[1])
_l_(116494)
_n_(116495, "items", lambda: items)[4] = 'Perl'
_l_(116496)
_c_(116499, _n_(116497, "print", lambda: print), 'New value: ', _n_(116498, "items", lambda: items)[4])
_l_(116500)