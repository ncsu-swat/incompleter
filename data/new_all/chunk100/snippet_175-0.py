# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def max_length_list(input_list):
    _l_(103553)

    max_length = _c_(103541, _n_(103536, "max", lambda: max), (_c_(103539, _n_(103537, "len", lambda: len), _n_(103538, "x", lambda: x)) for x in _n_(103540, "input_list", lambda: input_list)))
    _l_(103542)
    max_list = _c_(103548, _n_(103543, "max", lambda: max), _n_(103544, "input_list", lambda: input_list), key=lambda i: _c_(103547, _n_(103545, "len", lambda: len), _n_(103546, "i", lambda: i)))
    _l_(103549)
    aux = (_n_(103550, "max_length", lambda: max_length), _n_(103551, "max_list", lambda: max_list))
    _l_(103552)
    return aux

def min_length_list(input_list):
    _l_(103571)

    min_length = _c_(103559, _n_(103554, "min", lambda: min), (_c_(103557, _n_(103555, "len", lambda: len), _n_(103556, "x", lambda: x)) for x in _n_(103558, "input_list", lambda: input_list)))
    _l_(103560)
    min_list = _c_(103566, _n_(103561, "min", lambda: min), _n_(103562, "input_list", lambda: input_list), key=lambda i: _c_(103565, _n_(103563, "len", lambda: len), _n_(103564, "i", lambda: i)))
    _l_(103567)
    aux = (_n_(103568, "min_length", lambda: min_length), _n_(103569, "min_list", lambda: min_list))
    _l_(103570)
    return aux
_c_(103573, _n_(103572, "print", lambda: print), 'Original list:')
_l_(103574)
_c_(103577, _n_(103575, "print", lambda: print), _n_(103576, "list1", lambda: list1))
_l_(103578)
_c_(103580, _n_(103579, "print", lambda: print), '\nList with maximum length of lists:')
_l_(103581)
_c_(103586, _n_(103582, "print", lambda: print), _c_(103585, _n_(103583, "max_length_list", lambda: max_length_list), _n_(103584, "list1", lambda: list1)))
_l_(103587)
_c_(103589, _n_(103588, "print", lambda: print), '\nList with minimum length of lists:')
_l_(103590)
_c_(103595, _n_(103591, "print", lambda: print), _c_(103594, _n_(103592, "min_length_list", lambda: min_length_list), _n_(103593, "list1", lambda: list1)))
_l_(103596)