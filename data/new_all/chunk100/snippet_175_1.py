# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def max_length_list(input_list):
    _l_(12462)

    max_list = _c_(12457, _n_(12452, "max", lambda: max), _n_(12453, "input_list", lambda: input_list), key=lambda i: _c_(12456, _n_(12454, "len", lambda: len), _n_(12455, "i", lambda: i)))
    _l_(12458)
    aux = (_n_(12459, "max_length", lambda: max_length), _n_(12460, "max_list", lambda: max_list))
    _l_(12461)
    return aux

def min_length_list(input_list):
    _l_(12480)

    min_length = _c_(12468, _n_(12463, "min", lambda: min), (_c_(12466, _n_(12464, "len", lambda: len), _n_(12465, "x", lambda: x)) for x in _n_(12467, "input_list", lambda: input_list)))
    _l_(12469)
    min_list = _c_(12475, _n_(12470, "min", lambda: min), _n_(12471, "input_list", lambda: input_list), key=lambda i: _c_(12474, _n_(12472, "len", lambda: len), _n_(12473, "i", lambda: i)))
    _l_(12476)
    aux = (_n_(12477, "min_length", lambda: min_length), _n_(12478, "min_list", lambda: min_list))
    _l_(12479)
    return aux
list1 = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
_l_(12481)
_c_(12483, _n_(12482, "print", lambda: print), 'Original list:')
_l_(12484)
_c_(12487, _n_(12485, "print", lambda: print), _n_(12486, "list1", lambda: list1))
_l_(12488)
_c_(12490, _n_(12489, "print", lambda: print), '\nList with maximum length of lists:')
_l_(12491)
_c_(12496, _n_(12492, "print", lambda: print), _c_(12495, _n_(12493, "max_length_list", lambda: max_length_list), _n_(12494, "list1", lambda: list1)))
_l_(12497)
_c_(12499, _n_(12498, "print", lambda: print), '\nList with minimum length of lists:')
_l_(12500)
_c_(12505, _n_(12501, "print", lambda: print), _c_(12504, _n_(12502, "min_length_list", lambda: min_length_list), _n_(12503, "list1", lambda: list1)))
_l_(12506)