# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def max_length_list(input_list):
    _l_(93402)

    max_length = _c_(93392, _n_(93387, "max", lambda: max), (_c_(93390, _n_(93388, "len", lambda: len), _n_(93389, "x", lambda: x)) for x in _n_(93391, "input_list", lambda: input_list)))
    _l_(93393)
    max_list = _c_(93397, _n_(93394, "max", lambda: max), _n_(93395, "input_list", lambda: input_list), key=_n_(93396, "len", lambda: len))
    _l_(93398)
    aux = (_n_(93399, "max_length", lambda: max_length), _n_(93400, "max_list", lambda: max_list))
    _l_(93401)
    return aux

def min_length_list(input_list):
    _l_(93411)

    min_list = _c_(93406, _n_(93403, "min", lambda: min), _n_(93404, "input_list", lambda: input_list), key=_n_(93405, "len", lambda: len))
    _l_(93407)
    aux = (_n_(93408, "min_length", lambda: min_length), _n_(93409, "min_list", lambda: min_list))
    _l_(93410)
    return aux
list1 = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
_l_(93412)
_c_(93414, _n_(93413, "print", lambda: print), 'Original list:')
_l_(93415)
_c_(93418, _n_(93416, "print", lambda: print), _n_(93417, "list1", lambda: list1))
_l_(93419)
_c_(93421, _n_(93420, "print", lambda: print), '\nList with maximum length of lists:')
_l_(93422)
_c_(93427, _n_(93423, "print", lambda: print), _c_(93426, _n_(93424, "max_length_list", lambda: max_length_list), _n_(93425, "list1", lambda: list1)))
_l_(93428)
_c_(93430, _n_(93429, "print", lambda: print), '\nList with minimum length of lists:')
_l_(93431)
_c_(93436, _n_(93432, "print", lambda: print), _c_(93435, _n_(93433, "min_length_list", lambda: min_length_list), _n_(93434, "list1", lambda: list1)))
_l_(93437)
list1 = [[0], [1, 3], [5, 7], [9, 11], [3, 5, 7]]
_l_(93438)
_c_(93440, _n_(93439, "print", lambda: print), 'Original list:')
_l_(93441)
_c_(93444, _n_(93442, "print", lambda: print), _n_(93443, "list1", lambda: list1))
_l_(93445)
_c_(93447, _n_(93446, "print", lambda: print), '\nList with maximum length of lists:')
_l_(93448)
_c_(93453, _n_(93449, "print", lambda: print), _c_(93452, _n_(93450, "max_length_list", lambda: max_length_list), _n_(93451, "list1", lambda: list1)))
_l_(93454)
_c_(93456, _n_(93455, "print", lambda: print), '\nList with minimum length of lists:')
_l_(93457)
_c_(93462, _n_(93458, "print", lambda: print), _c_(93461, _n_(93459, "min_length_list", lambda: min_length_list), _n_(93460, "list1", lambda: list1)))
_l_(93463)
list1 = [[12], [1, 3], [1, 34, 5, 7], [9, 11], [3, 5, 7]]
_l_(93464)
_c_(93466, _n_(93465, "print", lambda: print), 'Original list:')
_l_(93467)
_c_(93470, _n_(93468, "print", lambda: print), _n_(93469, "list1", lambda: list1))
_l_(93471)
_c_(93473, _n_(93472, "print", lambda: print), '\nList with maximum length of lists:')
_l_(93474)
_c_(93479, _n_(93475, "print", lambda: print), _c_(93478, _n_(93476, "max_length_list", lambda: max_length_list), _n_(93477, "list1", lambda: list1)))
_l_(93480)
_c_(93482, _n_(93481, "print", lambda: print), '\nList with minimum length of lists:')
_l_(93483)
_c_(93488, _n_(93484, "print", lambda: print), _c_(93487, _n_(93485, "min_length_list", lambda: min_length_list), _n_(93486, "list1", lambda: list1)))
_l_(93489)