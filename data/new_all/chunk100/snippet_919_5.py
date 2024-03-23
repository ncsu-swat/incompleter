# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def max_length_list(input_list):
    _l_(93505)

    max_length = _c_(93495, _n_(93490, "max", lambda: max), (_c_(93493, _n_(93491, "len", lambda: len), _n_(93492, "x", lambda: x)) for x in _n_(93494, "input_list", lambda: input_list)))
    _l_(93496)
    max_list = _c_(93500, _n_(93497, "max", lambda: max), _n_(93498, "input_list", lambda: input_list), key=_n_(93499, "len", lambda: len))
    _l_(93501)
    aux = (_n_(93502, "max_length", lambda: max_length), _n_(93503, "max_list", lambda: max_list))
    _l_(93504)
    return aux

def min_length_list(input_list):
    _l_(93516)

    min_length = _c_(93511, _n_(93506, "min", lambda: min), (_c_(93509, _n_(93507, "len", lambda: len), _n_(93508, "x", lambda: x)) for x in _n_(93510, "input_list", lambda: input_list)))
    _l_(93512)
    aux = (_n_(93513, "min_length", lambda: min_length), _n_(93514, "min_list", lambda: min_list))
    _l_(93515)
    return aux
list1 = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
_l_(93517)
_c_(93519, _n_(93518, "print", lambda: print), 'Original list:')
_l_(93520)
_c_(93523, _n_(93521, "print", lambda: print), _n_(93522, "list1", lambda: list1))
_l_(93524)
_c_(93526, _n_(93525, "print", lambda: print), '\nList with maximum length of lists:')
_l_(93527)
_c_(93532, _n_(93528, "print", lambda: print), _c_(93531, _n_(93529, "max_length_list", lambda: max_length_list), _n_(93530, "list1", lambda: list1)))
_l_(93533)
_c_(93535, _n_(93534, "print", lambda: print), '\nList with minimum length of lists:')
_l_(93536)
_c_(93541, _n_(93537, "print", lambda: print), _c_(93540, _n_(93538, "min_length_list", lambda: min_length_list), _n_(93539, "list1", lambda: list1)))
_l_(93542)
list1 = [[0], [1, 3], [5, 7], [9, 11], [3, 5, 7]]
_l_(93543)
_c_(93545, _n_(93544, "print", lambda: print), 'Original list:')
_l_(93546)
_c_(93549, _n_(93547, "print", lambda: print), _n_(93548, "list1", lambda: list1))
_l_(93550)
_c_(93552, _n_(93551, "print", lambda: print), '\nList with maximum length of lists:')
_l_(93553)
_c_(93558, _n_(93554, "print", lambda: print), _c_(93557, _n_(93555, "max_length_list", lambda: max_length_list), _n_(93556, "list1", lambda: list1)))
_l_(93559)
_c_(93561, _n_(93560, "print", lambda: print), '\nList with minimum length of lists:')
_l_(93562)
_c_(93567, _n_(93563, "print", lambda: print), _c_(93566, _n_(93564, "min_length_list", lambda: min_length_list), _n_(93565, "list1", lambda: list1)))
_l_(93568)
list1 = [[12], [1, 3], [1, 34, 5, 7], [9, 11], [3, 5, 7]]
_l_(93569)
_c_(93571, _n_(93570, "print", lambda: print), 'Original list:')
_l_(93572)
_c_(93575, _n_(93573, "print", lambda: print), _n_(93574, "list1", lambda: list1))
_l_(93576)
_c_(93578, _n_(93577, "print", lambda: print), '\nList with maximum length of lists:')
_l_(93579)
_c_(93584, _n_(93580, "print", lambda: print), _c_(93583, _n_(93581, "max_length_list", lambda: max_length_list), _n_(93582, "list1", lambda: list1)))
_l_(93585)
_c_(93587, _n_(93586, "print", lambda: print), '\nList with minimum length of lists:')
_l_(93588)
_c_(93593, _n_(93589, "print", lambda: print), _c_(93592, _n_(93590, "min_length_list", lambda: min_length_list), _n_(93591, "list1", lambda: list1)))
_l_(93594)