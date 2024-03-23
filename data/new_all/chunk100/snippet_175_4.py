# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def max_length_list(input_list):
    _l_(12634)

    max_length = _c_(12622, _n_(12617, "max", lambda: max), (_c_(12620, _n_(12618, "len", lambda: len), _n_(12619, "x", lambda: x)) for x in _n_(12621, "input_list", lambda: input_list)))
    _l_(12623)
    max_list = _c_(12629, _n_(12624, "max", lambda: max), _n_(12625, "input_list", lambda: input_list), key=lambda i: _c_(12628, _n_(12626, "len", lambda: len), _n_(12627, "i", lambda: i)))
    _l_(12630)
    aux = (_n_(12631, "max_length", lambda: max_length), _n_(12632, "max_list", lambda: max_list))
    _l_(12633)
    return aux

def min_length_list(input_list):
    _l_(12652)

    min_length = _c_(12640, _n_(12635, "min", lambda: min), (_c_(12638, _n_(12636, "len", lambda: len), _n_(12637, "x", lambda: x)) for x in _n_(12639, "input_list", lambda: input_list)))
    _l_(12641)
    min_list = _c_(12647, _n_(12642, "min", lambda: min), _n_(12643, "input_list", lambda: input_list), key=lambda i: _c_(12646, _n_(12644, "len", lambda: len), _n_(12645, "i", lambda: i)))
    _l_(12648)
    aux = (_n_(12649, "min_length", lambda: min_length), _n_(12650, "min_list", lambda: min_list))
    _l_(12651)
    return aux
_c_(12654, _n_(12653, "print", lambda: print), 'Original list:')
_l_(12655)
_c_(12658, _n_(12656, "print", lambda: print), _n_(12657, "list1", lambda: list1))
_l_(12659)
_c_(12661, _n_(12660, "print", lambda: print), '\nList with maximum length of lists:')
_l_(12662)
_c_(12667, _n_(12663, "print", lambda: print), _c_(12666, _n_(12664, "max_length_list", lambda: max_length_list), _n_(12665, "list1", lambda: list1)))
_l_(12668)
_c_(12670, _n_(12669, "print", lambda: print), '\nList with minimum length of lists:')
_l_(12671)
_c_(12676, _n_(12672, "print", lambda: print), _c_(12675, _n_(12673, "min_length_list", lambda: min_length_list), _n_(12674, "list1", lambda: list1)))
_l_(12677)