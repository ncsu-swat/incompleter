# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def max_length_list(input_list):
    _l_(12524)

    max_length = _c_(12512, _n_(12507, "max", lambda: max), (_c_(12510, _n_(12508, "len", lambda: len), _n_(12509, "x", lambda: x)) for x in _n_(12511, "input_list", lambda: input_list)))
    _l_(12513)
    max_list = _c_(12519, _n_(12514, "max", lambda: max), _n_(12515, "input_list", lambda: input_list), key=lambda i: _c_(12518, _n_(12516, "len", lambda: len), _n_(12517, "i", lambda: i)))
    _l_(12520)
    aux = (_n_(12521, "max_length", lambda: max_length), _n_(12522, "max_list", lambda: max_list))
    _l_(12523)
    return aux

def min_length_list(input_list):
    _l_(12535)

    min_list = _c_(12530, _n_(12525, "min", lambda: min), _n_(12526, "input_list", lambda: input_list), key=lambda i: _c_(12529, _n_(12527, "len", lambda: len), _n_(12528, "i", lambda: i)))
    _l_(12531)
    aux = (_n_(12532, "min_length", lambda: min_length), _n_(12533, "min_list", lambda: min_list))
    _l_(12534)
    return aux
list1 = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
_l_(12536)
_c_(12538, _n_(12537, "print", lambda: print), 'Original list:')
_l_(12539)
_c_(12542, _n_(12540, "print", lambda: print), _n_(12541, "list1", lambda: list1))
_l_(12543)
_c_(12545, _n_(12544, "print", lambda: print), '\nList with maximum length of lists:')
_l_(12546)
_c_(12551, _n_(12547, "print", lambda: print), _c_(12550, _n_(12548, "max_length_list", lambda: max_length_list), _n_(12549, "list1", lambda: list1)))
_l_(12552)
_c_(12554, _n_(12553, "print", lambda: print), '\nList with minimum length of lists:')
_l_(12555)
_c_(12560, _n_(12556, "print", lambda: print), _c_(12559, _n_(12557, "min_length_list", lambda: min_length_list), _n_(12558, "list1", lambda: list1)))
_l_(12561)