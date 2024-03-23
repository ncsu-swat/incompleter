# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def max_length_list(input_list):
    _l_(12572)

    max_length = _c_(12567, _n_(12562, "max", lambda: max), (_c_(12565, _n_(12563, "len", lambda: len), _n_(12564, "x", lambda: x)) for x in _n_(12566, "input_list", lambda: input_list)))
    _l_(12568)
    aux = (_n_(12569, "max_length", lambda: max_length), _n_(12570, "max_list", lambda: max_list))
    _l_(12571)
    return aux

def min_length_list(input_list):
    _l_(12590)

    min_length = _c_(12578, _n_(12573, "min", lambda: min), (_c_(12576, _n_(12574, "len", lambda: len), _n_(12575, "x", lambda: x)) for x in _n_(12577, "input_list", lambda: input_list)))
    _l_(12579)
    min_list = _c_(12585, _n_(12580, "min", lambda: min), _n_(12581, "input_list", lambda: input_list), key=lambda i: _c_(12584, _n_(12582, "len", lambda: len), _n_(12583, "i", lambda: i)))
    _l_(12586)
    aux = (_n_(12587, "min_length", lambda: min_length), _n_(12588, "min_list", lambda: min_list))
    _l_(12589)
    return aux
list1 = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
_l_(12591)
_c_(12593, _n_(12592, "print", lambda: print), 'Original list:')
_l_(12594)
_c_(12597, _n_(12595, "print", lambda: print), _n_(12596, "list1", lambda: list1))
_l_(12598)
_c_(12600, _n_(12599, "print", lambda: print), '\nList with maximum length of lists:')
_l_(12601)
_c_(12606, _n_(12602, "print", lambda: print), _c_(12605, _n_(12603, "max_length_list", lambda: max_length_list), _n_(12604, "list1", lambda: list1)))
_l_(12607)
_c_(12609, _n_(12608, "print", lambda: print), '\nList with minimum length of lists:')
_l_(12610)
_c_(12615, _n_(12611, "print", lambda: print), _c_(12614, _n_(12612, "min_length_list", lambda: min_length_list), _n_(12613, "list1", lambda: list1)))
_l_(12616)